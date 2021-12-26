#-*- coding:utf-8 -*-
if __name__=="__main__" and __file__=="main.py":
    from socket import socket,AF_INET,SOCK_STREAM
    from ssl import wrap_socket
    from json import loads
    from goto import with_goto
    from traceback import format_exc
    from time import time
    from get_svg_captcha import get_svg_captcha,Decimal,compile,join
    from sys import argv,stdout
    from thread import get_ident
    index=1
    state=[int(time())&4294967295]+[None]*623
    while index<624:
        state[index]=(1812433253*(state[index-1]^(state[index-1]>>30))+index)&4294967295
        index=index+1
    def int32():
        global index,state
        a=0
        if 624<=index:
            b=0
            while b<227:
                a=(state[b]&2147483648)|(state[b+1]&2147483647)
                state[b]=state[b+397]^(a>>1)^((a&1)*2567483615)
                b=b+1
            while b<623:
                a=(state[b]&2147483648)|(state[b+1]&2147483647)
                state[b]=state[b-227]^(a>>1)^((a&1)*2567483615)
                b=b+1
            a=(state[623]&2147483648)|(state[0]&2147483647)
            state[623]=state[396]^(a>>1)^((a&1)*2567483615)
            index=1
            return state[1]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
        index=index+1
        return state[index]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
    phone_header=("30","31","32","33","35","36","37","38","39","50","51","52","53","55","56","57","58","59","62","65","66","67","70","71","72","73","75","76","77","78","80","81","82","83","84","85","86","87","88","89","90","91","92","93","95","96","97","98","99")
    roleType="1"
    chrome_version0="96.0.4664.93"
    chrome_version1=chrome_version0.split(".")[0]
    match_headers={"accept":"application/json",
    "accept-charset":"utf-8",
    "accept-language":"zh-CN",
    "origin":"https://www.haofenshu.com",
    "referer":"https://www.haofenshu.com/",
    "sec-ch-ua":join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\"")),
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"cross-site",
    "user-agent":join(("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",chrome_version0," Safari/537.36")),
    "Connection":"keep-alive",
    "Host":"hfs-be.yunxiao.com"}
    captcha0_headers={"accept":match_headers["accept"],
    "accept-charset":match_headers["accept-charset"],
    "accept-language":match_headers["accept-language"],
    "content-length":"42",
    "content-type":"application/json;charset=utf-8",
    "origin":match_headers["origin"],
    "referer":match_headers["referer"],
    "sec-ch-ua":match_headers["sec-ch-ua"],
    "sec-ch-ua-mobile":match_headers["sec-ch-ua-mobile"],
    "sec-ch-ua-platform":match_headers["sec-ch-ua-platform"],
    "sec-fetch-dest":match_headers["sec-fetch-dest"],
    "sec-fetch-mode":match_headers["sec-fetch-mode"],
    "sec-fetch-site":match_headers["sec-fetch-site"],
    "user-agent":match_headers["user-agent"],
    "Connection":match_headers["Connection"],
    "Host":match_headers["Host"]}
    captcha1_headers={"accept":captcha0_headers["accept"],
    "accept-charset":captcha0_headers["accept-charset"],
    "accept-language":captcha0_headers["accept-language"],
    "content-length":"56",
    "content-type":captcha0_headers["content-type"],
    "origin":captcha0_headers["origin"],
    "referer":captcha0_headers["referer"],
    "sec-ch-ua":captcha0_headers["sec-ch-ua"],
    "sec-ch-ua-mobile":captcha0_headers["sec-ch-ua-mobile"],
    "sec-ch-ua-platform":captcha0_headers["sec-ch-ua-platform"],
    "sec-fetch-dest":captcha0_headers["sec-fetch-dest"],
    "sec-fetch-mode":captcha0_headers["sec-fetch-mode"],
    "sec-fetch-site":captcha0_headers["sec-fetch-site"],
    "user-agent":captcha0_headers["user-agent"],
    "Connection":captcha0_headers["Connection"],
    "Host":captcha0_headers["Host"]}
    match_str=join(("GET /v2/users/matched-users?roleType=",roleType,"&account=%s HTTP/1.1\r\n",join((join((a,": ",match_headers[a],"\r\n")) for a in match_headers)),"\r\n"))
    captcha0_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha0_headers[a],"\r\n")) for a in captcha0_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,"}"))
    captcha0_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha1_headers[a],"\r\n")) for a in captcha1_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,",\"code\":\"%s\"}"))
    #roleType:角色类型(疑似区分家长帐号和学生帐号,但目前来看输入什么都可以)
    #account:手机号
    #occupied:手机号是否已被注册
    #unionId:翻译为"统一号",但返回值只有null不知道有啥用
    #boundWechat,boundApple:在chrome和via上只有false(疑似来自/跳转至微信/苹果(safari?))
    #code:0,成功
    #code:1001,参数错误,出现在没match就请求的时候,与match的请求不是同一个连接,与match的请求不是同一个手机号,或者就是字面意思比如长度不对等,需要重新match
    #code:4048,需要图形验证码,发送失败
    #code:4049,60s后才能重新发送,需要重新connect
    @with_goto
    def send_loop():
        try:
            write(str(get_ident())+" start\n")
            label.tag_connect
            connect=wrap_socket(socket(AF_INET,SOCK_STREAM))
            connect.settimeout(timeout)
            connect.connect(("hfs-be.yunxiao.com",443))
            send=connect.sendall
            recv=connect.recv
            label.tag_match
            phone=join(("1",phone_header[int32()%49],str(int32()%100000000).zfill(8)))
            #match和captcha共用一个连接
            #match,否则不能发送验证码,手机号重复,手机号错误(不是11位等)等情况貌似不会使匹配失败,目前已知失败的情况只有手机号已被注册
            send(match_str%phone)
            a=recv(1)
            response=""
            b={}
            while a:
                response=response+a
                a=recv(1)
            a=response.split("\r\n\r\n",1)
            for c in a[0].split("\r\n")[1::]:
                c=c.split(":")
                b[c[0]]=c[1].lstrip()
            json=loads(a[1])
            if json["data"]["occupied"]:
                goto.tag_match
            if json["code"]==0:
                #第一次请求,判断是否需要填图形验证码
                send(captcha0_str%phone)
                a=recv(1)
                response=""
                b={}
                while a:
                    response=response+a
                    a=recv(1)
                a=response.split("\r\n\r\n",1)
                for c in a[0].split("\r\n")[1::]:
                    c=c.split(":")
                    b[c[0]]=c[1].lstrip()
                json=loads(a[1])
                code=json["code"]
                if code==0 or code==1001 or code==4049:
                    connect.close()
                    goto.tag_connect
                elif code==4048:
                    label.tag_captcha1
                    #要填图形验证码的请求
                    send(captcha1_str%(phone,get_svg_captcha(json["data"]["pic"])))
                    a=recv(1)
                    response=""
                    b={}
                    while a:
                        response=response+a
                        a=recv(1)
                    a=response.split("\r\n\r\n",1)
                    for c in a[0].split("\r\n")[1::]:
                        c=c.split(":")
                        b[c[0]]=c[1].lstrip()
                    json=loads(a[1])
                    code=json["code"]
                    if code==0 or code==1001 or code==4049:
                        connect.close()
                        goto.tag_connect
                    elif code==4048:
                        goto.tag_captcha1
            else:
                goto.tag_match
        except:
            write(join((str(get_ident())," error\n",format_exc(),"\n================\n")))
        finally:
            write(join((str(get_ident())," end\n",response,"\n================\n")))
    if len(argv)==1:
        del Decimal,compile,argv,roleType,chrome_version0,chrome_version1,time,match_headers,captcha0_headers,captcha1_headers
        timeout=1
        write=stdout.write
        while True:
            send_loop()
    else:
        from sys import __stdout__,stderr,executable
        console=True
        threads=1
        sleep_time=1
        logfile=None
        processes=1
        timeout=1
        args=[executable,"main.py"]
        uint=compile(r"[\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{0,}").match
        ufloat=compile(r"[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}(?:\.[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}){0,1}").match
        version=compile(r"[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}(?:\.[\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39]{1,}){0,}").match
        for a in argv[1::]:
            assert a.count("=")==1,"wrong param format"
            a=a.split("=")
            key=a[0].strip()
            value=a[1].strip()
            if key=="roleType":
                roleType=value
            elif key=="chrome_version":
                chrome_version0=value
            elif key=="threads":
                threads=value
            elif key=="logfile":
                logfile=value
            elif key=="print":
                console=value
            elif key=="sleep_time":
                sleep_time=value
            elif key=="processes":
                processes=value
            elif key=="timeout":
                timeout=value
            else:
                raise AssertionError("unknown param:"+key)
        if roleType!="1":
            assert len(roleType)==1,"roleType is not byte"
            args.append("roleType="+roleType)
            a=True
        if chrome_version0!="96.0.4664.93":
            a=version(chrome_version0)
            assert a and a.group()==chrome_version0,"wrong chrome_version format"
            args.append("chrome_version="+chrome_version0)
            a=True
        if a:
            chrome_version1=chrome_version0.split(".")[0]
            match_headers["user-agent"]=captcha0_headers["user-agent"]=captcha1_headers["user-agent"]=join(("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",chrome_version0," Safari/537.36"))
            match_headers["sec-ch-ua"]=captcha0_headers["sec-ch-ua"]=captcha1_headers["sec-ch-ua"]=join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\""))
            match_str=join(("GET /v2/users/matched-users?roleType=",roleType,"&account=%s HTTP/1.1\r\n",join((join((a,": ",match_headers[a],"\r\n")) for a in match_headers)),"\r\n"))
            captcha0_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha0_headers[a],"\r\n")) for a in captcha0_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,"}"))
            captcha0_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha1_headers[a],"\r\n")) for a in captcha1_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,",\"code\":\"%s\"}"))
        if threads!=1:
            a=uint(threads)
            assert a and a.group()==threads,"threads is not uint"
            args.append("threads="+threads)
            threads=int(threads)
        if processes!=1:
            a=uint(processes)
            assert a and a.group()==processes,"processes is not uint"
            processes=int(processes)
        if sleep_time!=1:
            a=ufloat(sleep_time)
            assert a and a.group()==sleep_time,"sleep_time is not ufloat"
            args.append("sleep_time="+sleep_time)
            sleep_time=Decimal(sleep_time)
        if console!=True:
            if console=="True":
                console=True
            elif console=="False":
                console=False
            else:
                raise AssertionError("print is not bool")
        if timeout!=1:
            a=ufloat(timeout)
            assert a and a.group()==timeout,"timeout is not ufloat"
            args.append("timeout="+timeout)
            timeout=Decimal(timeout)
        if logfile:
            args.append("logfile="+logfile)
            logfile=open(logfile,"ab")
            if console:
                write_logfile=logfile.write
                write_console=__stdout__.write
                class write:
                    def write(self,data=""):
                        write_console(data)
                        write_logfile(data)
                stdout=stderr=write()
            else:
                args.append("print=False")
                stdout=stderr=logfile
        elif not console:
            args.append("print=False")
            class write:
                write=lambda self,data=None:None
            stdout=stderr=write()
        write=stdout.write
        del console,logfile,key,value,version,argv,Decimal,compile,ufloat,uint,roleType,chrome_version0,chrome_version1,time,executable,match_headers,captcha0_headers,captcha1_headers
        if processes==1:
            del processes,args
            if threads==1:
                del threads,a,sleep_time
                while True:
                    send_loop()
            else:
                from thread import start_new_thread
                from time import sleep
                class thread:
                    start=False
                    stop=False
                    def reset(self):
                        self.start=False
                        self.stop=False
                    def run(self):
                        try:
                            self.start=True
                            send_loop()
                        finally:
                            self.stop=True
                thread_list=[]
                while 0<threads:
                    thread_list.append(thread())
                    threads=threads-1
                del threads,thread
                thread_list=tuple(thread_list)
                while True:
                    for a in thread_list:
                        if not (a.start and (not a.stop)):
                            a.reset()
                            start_new_thread(a.run,())
                    sleep(sleep_time)
        else:
            from subprocess import Popen
            from time import sleep
            process_list=[]
            while 0<processes:
                process_list.append(Popen(args=args,bufsize=0))
                processes=processes-1
            process_list=tuple(process_list)
            a=0
            while True:
                while a<processes:
                    if process_list[a].poll()!=None:
                        process_list[a]=Popen(args=args,bufsize=0)
                sleep(sleep_time)