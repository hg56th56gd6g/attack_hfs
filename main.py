#-*- coding:utf-8 -*-
if __name__=="__main__" and __file__=="main.py":
    from json import loads
    from goto import with_goto
    from traceback import format_exc
    from get_svg_captcha import get_svg_captcha,join
    from sys import argv,stdout
    from thread import get_ident
    from proxy import int32
    import proto
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
    "connection":"keep-alive",
    "host":"hfs-be.yunxiao.com"}
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
    "connection":match_headers["connection"],
    "host":match_headers["host"]}
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
    "connection":captcha0_headers["connection"],
    "host":captcha0_headers["host"]}
    match_str=join(("GET /v2/users/matched-users?roleType=",roleType,"&account=%s HTTP/1.1\r\n",join((join((a,": ",match_headers[a],"\r\n")) for a in match_headers)),"\r\n"))
    captcha0_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha0_headers[a],"\r\n")) for a in captcha0_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,"}"))
    captcha1_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha1_headers[a],"\r\n")) for a in captcha1_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,",\"code\":\"%s\"}"))
    #roleType:????????????(???????????????????????????????????????,????????????????????????????????????)
    #account:?????????
    #occupied:???????????????????????????
    #unionId:?????????"?????????",??????????????????null??????????????????
    #boundWechat,boundApple:???chrome???via?????????false(????????????/???????????????/??????(safari?))
    #code:0,??????,??????connect
    #code:1001,????????????,????????????match??????????????????,???match??????????????????????????????,???match?????????????????????????????????,?????????????????????????????????????????????,????????????match,???????????????,??????connect
    #code:4048,?????????????????????,????????????,??????captcha1
    #code:4049,60s?????????????????????,??????connect????????????,(???????????????)
    getapi=lambda a:(lambda:proto.srwc(a),a.sendall,a.recv)
    getcnct=lambda:getapi(proto.ssl_tls(proto.tcp(("hfs-be.yunxiao.com",443),blocking=timeout)))
    def getdata(a):
        b=a(1)
        c=""
        while b:
            c=c+b
            b=a(1)
        return c
    timeout=True
    @with_goto
    def send_loop():
        try:
            ident=str(get_ident())
            write(ident+" start\n")
            label.tag_connect
            srwc,send,recv=getcnct()
            label.tag_match
            phone=join(("1",phone_header[int32()%49],str(int32()%100000000).zfill(8)))
            send(match_str%phone)
            response=getdata(recv)
            json=loads(response.split("\r\n\r\n",1)[1])
            #?????????????????????
            if json["data"]["occupied"]:
                goto.tag_match
            if json["code"]==0:
                #???????????????,????????????????????????????????????
                send(captcha0_str%phone)
                response=getdata(recv)
                json=loads(response.split("\r\n\r\n",1)[1])
                code=json["code"]
                if code==0 or code==1001 or code==4049:
                    srwc()
                    goto.tag_connect
                elif code==4048:
                    label.tag_captcha1
                    #??????????????????????????????
                    send(captcha1_str%(phone,get_svg_captcha(json["data"]["pic"])))
                    response=getdata(recv)
                    json=loads(response.split("\r\n\r\n",1)[1])
                    code=json["code"]
                    if code==0 or code==1001 or code==4049:
                        srwc()
                        goto.tag_connect
                    elif code==4048:
                        goto.tag_captcha1
            else:
                goto.tag_match
        except:
            write(join((ident," error\n",format_exc(),"\n================\n")))
        finally:
            try:
                write(join((ident," end\n",response,"\n================\n")))
            except:
                write(ident+" end\nget response error\n================\n")
    if len(argv)==1:
        del argv,roleType,chrome_version0,chrome_version1,match_headers,captcha0_headers,captcha1_headers
        write=stdout.write
        while True:
            send_loop()
    else:
        from get_svg_captcha import compile
        from sys import stderr,executable
        console=True
        threads=1
        sleep_time=1
        logfile=None
        processes=1
        debug=False
        proxy=False
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
            elif key=="debug":
                debug=value
            elif key=="proxy":
                proxy=value
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
            captcha1_str=join(("POST /v2/native-users/verification-msg-with-captcha HTTP1.1\r\n",join((join((a,": ",captcha1_headers[a],"\r\n")) for a in captcha1_headers)),"\r\n{\"phoneNumber\":\"%s\",\"roleType\":",roleType,",\"code\":\"%s\"}"))
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
            sleep_time=float(sleep_time)
        if console!=True:
            if console=="True":
                console=True
            elif console=="False":
                console=False
            else:
                raise AssertionError("print is not bool")
        if timeout!=True and timeout!="True":
            if timeout==False or timeout=="False":
                timeout=False
            else:
                a=ufloat(timeout)
                assert a and a.group()==timeout,"timeout is not ufloat or bool"
                args.append("timeout="+timeout)
                timeout=float(timeout)
        if debug!=False:
            if debug=="True":
                args.append("debug=True")
                def getdata(a):
                    b=a(1)
                    c=""
                    while b:
                        c=c+b
                        b=a(1)
                    write(join(("********",str(get_ident()),"********\n",c,"\n********debug********\n")))
                    return c
            elif debug!="False":
                raise AssertionError("debug is not bool")
        if proxy!=False:
            if proxy=="True":
                from proxy import getproxy
                args.append("proxy=True")
                proxy_data={"user-agent":captcha1_headers["user-agent"],
                "proxy-connection":captcha1_headers["connection"],
                "host":"hfs-be.yunxiao.com:443"}
                proxy_data=join((join((a,": ",proxy_data[a],"\r\n")) for a in proxy_data))
                def getcnct():
                    while True:
                        a,b,c=getproxy()
                        if a=="socks4":
                            a=proto.socks4("hfs-be.yunxiao.com",443,b,c if c else timeout)
                            if a:
                                return getapi(a)
                        elif a=="socks4a":
                            a=proto.socks4a("hfs-be.yunxiao.com",443,b,c if c else timeout)
                            if a:
                                return getapi(a)
                        elif a=="socks5":
                            a=proto.socks5("hfs-be.yunxiao.com",443,b,c if c else timeout)
                            if a:
                                return getapi(a)
                        elif a=="socks5a":
                            a=proto.socks5a("hfs-be.yunxiao.com",443,b,c if c else timeout)
                            if a:
                                return getapi(a)
                        elif a=="http":
                            a=proto.http("hfs-be.yunxiao.com",443,b,proxy_data,c if c else timeout)
                            if a:
                                return getapi(a)
            elif proxy!="False":
                raise AssertionError("proxy is not bool")
        if logfile:
            args.append("logfile="+logfile)
            logfile=open(logfile,"ab")
            if console:
                from sys import __stdout__
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
        del console,logfile,key,value,version,argv,compile,ufloat,uint,roleType,chrome_version0,chrome_version1,executable,match_headers,captcha0_headers,captcha1_headers,debug,proxy
        if processes==1:
            del processes,args
            if threads==1:
                del threads,a,sleep_time
                while True:
                    send_loop()
            else:
                from time import sleep
                from thread import start_new_thread
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