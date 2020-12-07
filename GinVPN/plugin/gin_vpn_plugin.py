  
# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.
    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.
"""
from typing import Optional, Dict

from proxy.common.utils import build_http_response
from proxy.common.utils import bytes_
from proxy.http.parser import HttpParser
from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.methods import httpMethods
from GinVPN.AES import AES
import sys
from typing import Optional, Any
from urllib import parse as urlparse

class GinVPNPlugin(HttpProxyBasePlugin):
   
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        key="Vrz19NDnmgmqvJw0fm4R3Zadi7OLLVoA"
        self.server='127.0.0.1'
        self.port=5000
        self.serverurl=urlparse.SplitResultBytes(scheme="http", netloc=self.server+':'+str(self.port), path="/", query="",fragment="")
        self.aes=AES.AES(key,14)
        self.decrypt=False

    def before_upstream_connection(
            self, request: HttpParser) -> Optional[HttpParser]:
        print(request.method, request.url)
        if request.method != httpMethods.CONNECT and request.method != httpMethods.TRACE:
            request_string=request.method
            if request.port==80 or request.port==8080:
                request_string=request_string+b" "+b'http://' +request.host+request.path+request.url.query+request.url.fragment+b' '
            else:
                request_string=request_string+b" "+b'http://' +request.host+b':'+bytes(str(request.port),'utf-8')+request.path+request.url.query+request.url.fragment+b' '
            headers_to_delete=[]
            for h in request.headers:
                headers_to_delete.append(h)
                request_string=request_string+b"<h>"+request.headers[h][0]+b':'+request.headers[h][1]
            for h in headers_to_delete:
                request.del_header(h)
            
            if request.body!=None:
                request_string=request_string+b"<b>"
                request_string=request_string+request.body
            request.body=self.aes.encrypt(request_string, False)
            if not request.is_chunked_encoded():
                request.add_header(b'Content-Length',
                                   bytes_(len(request.body)))
            request.port=self.port
            request.host=bytes(self.server,'utf-8')
            request.url=self.serverurl
            request.method=httpMethods.POST
        return request

    def handle_client_request(
            self, request: HttpParser) -> Optional[HttpParser]:
        return request

    def handle_upstream_chunk(self, chunk: memoryview) -> memoryview:
        #print("msg recieved")
        res=HttpParser.response(chunk)
        if(res.has_header(b'zander-approved') and res.code==b'200'):
            self.decrypt=True
            return memoryview(b'')
        if self.decrypt:
            self.decrypt=False
            res=self.aes.decrypt(bytes(chunk))
            status_code=int.from_bytes(res[0:2], "big")
            res_url=res.split(b' ')[1].decode('utf-8')
            r=b' '.join(res.split(b' ')[2:]).split(b'<b>')
            res_headers=r[0].split(b'<h>')[1:]
            res_body=b''.join(r[1:])
            headers_dict={}
            for h in res_headers:
                headers_dict[h.split(b':')[0]]=h.split(b':')[1]
            headers_dict[b'Content-Length']=bytes(str(len(res_body)), 'utf-8')
            try:
                del headers_dict[b'Transfer-Encoding']
            except KeyError:
                pass
            print(headers_dict, '\n',bytes(res_body))
            return memoryview(build_http_response(
            status_code,body=bytes(res_body),headers=headers_dict))
        return chunk

    def on_upstream_connection_close(self) -> None:
        pass