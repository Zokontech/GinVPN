import asyncio
from aiohttp import web
import requests
import os
import socket
import time
import sys
from GinVPN.AES import AES
import socket, string, random, requests,threading, queue
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

aes=None
def format_response(r):
    byte_string=b''
    byte_string+=r.status_code.to_bytes(2, byteorder='big')+b' '
    byte_string+=r.url.encode('utf-8')+b' '
    for h in r.headers:
        #print(h, r.headers[h])
        byte_string+=b'<h>'+h.encode('utf-8')+b':'+ r.headers[h].encode('utf-8')
    byte_string+=b'<b>'+r.content
    return byte_string
def make_request(req_type, req_url, headers_dict, req_body):
    r=None
    print("making request")
    try:
        if(req_type==b'GET'):
            r = requests.get(req_url, data=req_body,headers=headers_dict)
        elif(req_type==b'POST'):
            r = requests.post(req_url, data=req_body,headers=headers_dict)
        elif(req_type==b'HEAD'):
            r = requests.head(req_url, headers=headers_dict)
        elif(req_type==b'PUT'):
            r = requests.put(req_url, data=req_body,headers=headers_dict)
        elif(req_type==b'DELETE'):
            r = requests.delete(req_url, data=req_body,headers=headers_dict)
        elif(req_type==b'OPTIONS'):
            r = requests.options(req_url, data=req_body,headers=headers_dict)
        print("done with request")
    except Exception as e:
        return r,e
    return r,''
async def recv_msg(request):
    msg=await request.read()
    req=aes.decrypt(msg)
    print(req)
    req_type=req.split(b' ')[0]
    req_url=req.split(b' ')[1].decode('utf-8')
    r=b''.join(req.split(b' ')[2:]).split(b'<b>')
    req_headers=r[0].split(b'<h>')[1:]
    req_body=b''.join(r[1:])
    headers_dict={}
    for h in req_headers:
        headers_dict[h.split(b':')[0]]=h.split(b':')[1]
    r,e=make_request(req_type, req_url, headers_dict, req_body)
    if r!=None:
        b=aes.encrypt(format_response(r),False)
        print(len(b))
        return web.Response(status=200,body=bytes(b), headers={'zander-approved':'yes', 'Content-Length':str(len(b))})
    else:
        return web.Response(status=500,text=str(e))

    #return web.Response(status=500, text='GinVPN has encountered an error')
        

def main():
    try:
        import GinVPN.GinSettings
        key=GinVPN.GinSettings.key
        port=GinVPN.GinSettings.server_port
    except ModuleNotFoundError:
        print("Config Not Found, run GinConfig")
        return
    global aes
    aes=AES.AES(key,14)
    app = web.Application()
    app.router.add_route('POST', '/', recv_msg)
    loop = asyncio.get_event_loop()
    f = loop.create_server(app.make_handler(), '0.0.0.0', os.environ.get('PORT', str(port)))
    srv = loop.run_until_complete(f)
    print('serving on', srv.sockets[0].getsockname())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
if __name__ == "__main__":
    main()
