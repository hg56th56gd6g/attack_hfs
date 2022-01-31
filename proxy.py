#-*- coding:utf-8 -*-
#本来随机函数是在main.py里的,但是这里也要用,所以就定义在这里了
from time import time
from get_svg_captcha import join
state=[int(time())&4294967295,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
time=0
index=1
while index<624:
    state[index]=(1812433253*(state[time]^(state[time]>>30))+index)&4294967295
    time=time+1
    index=index+1
def int32():
    global index,state
    a=0
    if 624<=index:
        b=0
        c=1
        d=397
        while b<227:
            a=(state[b]&2147483648)|(state[c]&2147483647)
            state[b]=state[d]^(a>>1)^((a&1)*2567483615)
            b=b+1
            c=c+1
            d=d+1
        d=0
        while b<623:
            a=(state[b]&2147483648)|(state[c]&2147483647)
            state[b]=state[d]^(a>>1)^((a&1)*2567483615)
            b=b+1
            c=c+1
            d=d+1
        a=(state[623]&2147483648)|(state[0]&2147483647)
        state[623]=state[396]^(a>>1)^((a&1)*2567483615)
        index=1
        a=state[1]
        a=a^(a>>11)
        a=a^(a<<7)&2636928640
        a=a^(a<<15)&4022730752
        return a^(a>>18)
    a=state[index]
    index=index+1
    a=a^(a>>11)
    a=a^(a<<7)&2636928640
    a=a^(a<<15)&4022730752
    return a^(a>>18)
del time
#从proxies.txt读取,此处可以自定义代理池写入proxies.txt或直接对proxies进行操作
#格式,proto:host:port:timeout;...,timeout可以根据代理不同来设置超时,没有则使用全局timeout,支持socks4,socks5,http隧道代理,除了http,后面可以加个a,代表让代理去解析host
def reload():
    global proxies
    a=open("proxies.txt","rb")
    proxies=[(c[0],(c[1],int(c[2])),float(c[3]) if c[3] else False) for c in frozenset(tuple(b.split(":")) for b in a.read().split(";")[:-1:])]
    a.close()
#随机获取代理
def getproxy():
    if proxies:
        return proxies[int(((int32()>>5)*67108864+(int32()>>6))/9007199254740992.0*len(proxies))]
    else:#随机分配一个幸运ip
        return ("socks4","socks4a","socks5","socks5a","http","httpa")[int32()%6],(join((str(int32()%256),".",str(int32()%256),".",str(int32()%256),".",str(int32()%256))),int32()%65536)
reload()