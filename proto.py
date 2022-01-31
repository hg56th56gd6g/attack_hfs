#-*- coding:utf-8 -*-
import socket
from ssl import wrap_socket
from struct import pack
from get_svg_captcha import join
class getmethod:
    method=lambda:None
getmethod=type(getmethod().method)
addmethod=lambda object,name,method:setattr(object,name,getmethod(method,object))
def srwc(self):
    self.shutdown(socket.SHUT_RDWR)
    self.close()
def recvall(recv,size):
    a=""
    while len(a)<size:
        b=recv(size-len(a))
        if not b:
            raise Exception("proxy server closed")
        a=a+b
    return a
#创建tcp客户端
def tcp(addr,blocking=True,localaddr=("",0)):#远程地址((ipv4,port)),本地地址((ipv4,port)),阻塞模式(True or False or timeout)
    clientobj=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
    if blocking==True:
        clientobj.setblocking(True)
    elif blocking==False:
        clientobj.setblocking(False)
    elif (type(blocking)==int or type(blocking)==float) and 0<blocking:
        clientobj.settimeout(blocking)
    else:
        raise AssertionError("wrong blocking")
    clientobj.bind(localaddr)
    clientobj.connect(addr)
    return clientobj
#给tcp套一层ssl/tls
def ssl_tls(socketobj):
    socketobj=wrap_socket(socketobj,do_handshake_on_connect=False)
    socketobj.do_handshake()
    return socketobj
#协议部分,不带a的host本地解析,带a的让代理去解析,给免费代理写的,只支持不认证
#本地解析的参数:远程ipv4,远程端口,代理地址((ipv4,port)),本地地址((ipv4,port)),阻塞模式(True or False or timeout)
#代理解析的参数:远程host,远程端口,代理地址((ipv4,port)),本地地址((ipv4,port)),阻塞模式(True or False or timeout)
def socks4(host,port,proxyaddr,blocking=True):
    clientobj=tcp(proxyaddr,blocking)
    clientobj.sendall(join(("\x04\x01",pack("!H",port),socket.gethostbyname(socket.inet_aton(host)),"\x00")))
    if recvall(clientobj.recv,2)=="\x00\x5a":
        recvall(clientobj.recv,6)
        return clientobj
    clientobj.shutdown(socket.SHUT_RDWR)
    clientobj.close()
def socks4a(host,port,proxyaddr,blocking=True):
    clientobj=tcp(proxyaddr,blocking)
    clientobj.sendall(join(("\x04\x01",pack("!H",port),"\x00\x00\x00\x01\x00",host,"\x00")))
    if recvall(clientobj.recv,2)=="\x00\x5a":
        recvall(clientobj.recv,6)
        return clientobj
    clientobj.shutdown(socket.SHUT_RDWR)
    clientobj.close()
def socks5(host,port,proxyaddr,blocking=True):
    clientobj=tcp(proxyaddr,blocking)
    clientobj.sendall("\x05\x01\x00")
    if recvall(clientobj.recv,2)=="\x05\x00":
        clientobj.sendall(join(("\x05\x01\x00\x01",socket.gethostbyname(socket.inet_aton(host)),pack("!H",port))))
        if recvall(clientobj.recv,3)=="\x05\x00\x00":
            a=recvall(clientobj.recv,1)
            if a=="\x01":
                recvall(clientobj.recv,6)
                return clientobj
            elif a=="\x03":
                recvall(clientobj.recv,ord(recvall(clientobj.recv,1))+2)
                return clientobj
            elif a=="\x04":
                recvall(clientobj.recv,18)
                return clientobj
    clientobj.shutdown(socket.SHUT_RDWR)
    clientobj.close()
def socks5a(host,port,proxyaddr,blocking=True):
    clientobj=tcp(proxyaddr,blocking)
    clientobj.sendall("\x05\x01\x00")
    if recvall(clientobj.recv,2)=="\x05\x00":
        clientobj.sendall(join(("\x05\x01\x00\x03",chr(len(host)),host,pack("!H",port))))
        if recvall(clientobj.recv,3)=="\x05\x00\x00":
            a=recvall(clientobj.recv,1)
            if a=="\x01":
                recvall(clientobj.recv,6)
                return clientobj
            elif a=="\x03":
                recvall(clientobj.recv,ord(recvall(clientobj.recv,1))+2)
                return clientobj
            elif a=="\x04":
                recvall(clientobj.recv,18)
                return clientobj
    clientobj.shutdown(socket.SHUT_RDWR)
    clientobj.close()
def http(host,port,proxyaddr,headers,blocking=True):#这个不分本地和代理解析了,这个只是host处有区别,传参换一下就行,新加了headers参数
    clientobj=tcp(proxyaddr,blocking)
    clientobj.sendall(join(("CONNECT ",host,":",str(port)," HTTP/1.1\r\n",headers,"\r\n")))
    a=recvall(clientobj.recv,1)
    while a:
        if a==" ":
            if recvall(clientobj.recv,3)=="200":
                a=recvall(clientobj.recv,1)
                while a:
                    a=recvall(clientobj.recv,1)
                return clientobj
            clientobj.shutdown(socket.SHUT_RDWR)
            clientobj.close()
    clientobj.shutdown(socket.SHUT_RDWR)
    clientobj.close()