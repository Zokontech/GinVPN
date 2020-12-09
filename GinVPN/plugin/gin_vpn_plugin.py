#Alexander Krasny
from typing import Optional, Dict
from proxy.common.utils import build_http_response
from proxy.common.utils import bytes_
from proxy.http.parser import HttpParser
from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.methods import httpMethods
from GinVPN.AES import AES
import sys, json
from typing import Optional, Any
from urllib import parse as urlparse

class GinVPNPlugin(HttpProxyBasePlugin):
   
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        try:
            import GinVPN.GinSettings
            key=GinVPN.GinSettings.key
            server=GinVPN.GinSettings.server_adr
            port=GinVPN.GinSettings.server_port
        except ModuleNotFoundError:
            print("Config Not Found, Quit The Proxy and Run GinConfig") #prompts user to run config
            sys.exit()
        self.server=server
        self.port=port
        self.serverurl=urlparse.SplitResultBytes(scheme="http", netloc=self.server+':'+str(self.port), path="/", query="",fragment="")
        self.aes=AES.AES(key)
        self.decrypt=False
    """
    Run every time the proxy receives an HTTP/S request. 
    On HTTP requests, this method creates a bytestring of the url, headers, and request body. 
    It runs AES.encrypt() and then modifies the request to send to server. 
    """
    def before_upstream_connection(
            self, request: HttpParser) -> Optional[HttpParser]:
        if request.method != httpMethods.CONNECT and request.method != httpMethods.TRACE:
            request_string=request.method 
            if request.port==80 or request.port==8080:
                request_string=request_string+b" "+b'http://' +request.host+request.path+request.url.query+request.url.fragment+b' '
            else:
                request_string=request_string+b" "+b'http://' +request.host+b':'+bytes(str(request.port),'utf-8')+request.path+request.url.query+request.url.fragment+b' '
            headers_to_delete=[]
            for h in request.headers:
                headers_to_delete.append(h)
                request_string=request_string+request.headers[h][0]+b':'+request.headers[h][1]+b'\r\n'
            for h in headers_to_delete: #remove headers from new request to GinVPN server
                request.del_header(h)
            if request.body!=None:
                request_string=request_string+b'\r\n'
                request_string=request_string+request.body
            request.body=self.aes.encrypt(request_string, False) #encrypt request_string
            if not request.is_chunked_encoded():
                request.add_header(b'Content-Length',
                                   bytes_(len(request.body))) #specify body length as a header
            #set new request properties to redirect to GinVPN server
            request.port=self.port
            request.host=bytes(self.server,'utf-8')
            request.url=self.serverurl
            request.method=httpMethods.POST
            request.path=b"/"
        return request
    #Not modified as part of this plugin, but runs for every chunk of data sent by client.
    def handle_client_request(
            self, request: HttpParser) -> Optional[HttpParser]:
        return request
    """
    called whenever a chunk is received from the server.
    Parses request into an Http response object. If the header’s contain ‘zander-approved’, it means the next chunk it receives is encrypted text.
    When it receives this encrypted text, it runs AES.decrypt(), and then parses the result into its constituent parts, and constructs it into a response object to send back to the client.
    """
    def handle_upstream_chunk(self, chunk: memoryview) -> memoryview:
        #print("msg recieved")
        res=HttpParser.response(chunk)
        if(res.has_header(b'zander-approved') and res.code==b'200'):
            self.decrypt=True #set flag to decrypt next chunk
            return memoryview(b'')
        if self.decrypt:
            self.decrypt=False
            res=self.aes.decrypt(bytes(chunk))
            status_code=int.from_bytes(res[0:2], "big") #encrypt status code as 2 bytes, because it can exceed 256, and encrypting as 2 bytes is cheaper than the 3 bytes the characters would take. 
            res_url=res.split(b' ')[1].decode('utf-8')
            r=b' '.join(res.split(b' ')[2:]).split(b'\r\n\r\n')
            try:
                res_headers=r[0].split(b'\r\n')[0:-1]
            except IndexError:
                res_headers=[]
            res_body=b''.join(r[1:])
            headers_dict={}
            for h in res_headers:
                headers_dict[h.split(b':')[0]]=h.split(b':')[1]
            headers_dict[b'Content-Length']=bytes(str(len(res_body)), 'utf-8')
            try:
                del headers_dict[b'Transfer-Encoding']
            except KeyError:
                pass
            return memoryview(build_http_response( #imported from common utils. Creates a response object compatabile with proxy.py
            status_code,body=bytes(res_body),headers=headers_dict))
        return chunk

    def on_upstream_connection_close(self) -> None:
        pass