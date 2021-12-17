#-*- coding:utf-8 -*-
if __name__=="__main__":#命令行调用,"python main.py"或"python main.py poolsize=[int] roleType=[byte] chrome_version=[str] threads=[int] logfile=[str] print=[bool] sleep_time=[rational]",每个参数都是可选的,如有重复后面的会覆盖前面的,poolsize连接池大小默认255,roleType默认"1",chrome_version默认"96.0.4664.93",threads线程数量默认1,logfile日志文件路径默认打印到控制台,print默认将log打印到控制台即使logfile不是默认,sleep_time每次检查线程的循环sleep多少秒默认1秒
    import requests
    Session=requests.Session
    requests.adapters.DEFAULT_POOLSIZE=255
    from _random import Random
    Random=Random().getrandbits
    from goto import with_goto
    from traceback import format_exc
    from time import sleep
    from get_svg_captcha import get_svg_captcha,Fraction
    from sys import argv,__stdout__,__stderr__,stdout,stderr
    from thread import start_new_thread,get_ident
    nothing=lambda data=None:None
    join="".join
    phone_header=("30","31","32","33","35","36","37","38","39","50","51","52","53","55","56","57","58","59","62","65","66","67","70","71","72","73","75","76","77","78","80","81","82","83","84","85","86","87","88","89","90","91","92","93","95","96","97","98","99")
    default_roleType="1"
    default_chrome_version="96.0.4664.93"
    roleType="1"
    chrome_version0="96.0.4664.93"
    chrome_version1=chrome_version0.split(".")[0]
    match_url=join(("https://hfs-be.yunxiao.com/v2/users/matched-users?roleType=",roleType,"&account="))
    match_headers={"accept":"application/json, text/plain, */*",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
    "origin":"https://www.haofenshu.com",
    "referer":"https://www.haofenshu.com/",
    "sec-ch-ua":join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\"")),
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"cross-site",
    "user-agent":join(("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",chrome_version0," Safari/537.36"))}
    captcha0_headers={"accept":match_headers["accept"],
    "accept-encoding":match_headers["accept-encoding"],
    "accept-language":match_headers["accept-language"],
    "content-length":"42",
    "content-type":"application/json;charset=UTF-8",
    "origin":match_headers["origin"],
    "referer":match_headers["referer"],
    "sec-ch-ua":match_headers["sec-ch-ua"],
    "sec-ch-ua-mobile":match_headers["sec-ch-ua-mobile"],
    "sec-ch-ua-platform":match_headers["sec-ch-ua-platform"],
    "sec-fetch-dest":match_headers["sec-fetch-dest"],
    "sec-fetch-mode":match_headers["sec-fetch-mode"],
    "sec-fetch-site":match_headers["sec-fetch-site"],
    "user-agent":match_headers["user-agent"]}
    captcha1_headers={"accept":captcha0_headers["accept"],
    "accept-encoding":captcha0_headers["accept-encoding"],
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
    "user-agent":captcha0_headers["user-agent"]}
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
    def send_loop(write,unlock=nothing):
        try:
            write(join((str(get_ident())," start\n")))
            label.tag_connect
            connect=Session()
            label.tag_match
            phone=join(("1",phone_header[Random(6)%49],str(Random(27)%100000000).zfill(8)))
            #match和captcha共用一个连接
            #match,否则不能发送验证码,手机号重复,手机号错误(不是11位等)等情况貌似不会使匹配失败,目前已知失败的情况只有手机号已被注册
            response=connect.get(match_url+phone,headers=match_headers)
            json=response.json()
            if json["data"]["occupied"]:
                goto.tag_match
            if json["code"]==0:
                label.tag_captcha0
                #第一次请求,判断是否需要填图形验证码
                response=connect.post("https://hfs-be.yunxiao.com/v2/native-users/verification-msg-with-captcha",headers=captcha0_headers,data=join(("{\"phoneNumber\":\"",phone,"\",\"roleType\":",roleType,"}")))
                json=response.json()
                code=json["code"]
                if code==0:
                    goto.tag_captcha0
                elif code==1001:
                    goto.tag_match
                elif code==4048:
                    label.tag_captcha1
                    #要填图形验证码的请求
                    response=connect.post("https://hfs-be.yunxiao.com/v2/native-users/verification-msg-with-captcha",headers=captcha1_headers,data=join(("{\"phoneNumber\":\"",phone,"\",\"roleType\":",roleType,",\"code\":\"",get_svg_captcha(json["data"]["pic"]),"\"}")))
                    json=response.json()
                    code=json["code"]
                    if code==0:
                        goto.tag_captcha0
                    elif code==1001:
                        goto.tag_match
                    elif code==4048:
                        goto.tag_captcha1
                    elif code==4049:
                        connect.close()
                        goto.tag_connect
                elif code==4049:
                    connect.close()
                    goto.tag_connect
            else:
                goto.tag_match
        except:
            write(join((str(get_ident())," error\n",format_exc(),"\n================\n")))
        finally:
            write(join((str(get_ident())," end\n",response.text.encode(response.encoding),"\n================\n")))
            unlock()
            return
    ################
    if len(argv)==1:
        del requests,default_roleType,default_chrome_version
        write=stdout.write
        while True:
            send_loop(write)
    else:
        console=True
        threads=1
        sleep_time=1
        logfile=None
        numbers=frozenset(("0","1","2","3","4","5","6","7","8","9"))
        for a in argv[1::]:
            assert "=" in a,"unknown param"
            a=a.split("=")
            key=a[0].strip()
            value=a[1].strip()
            if key=="poolsize":
                for a in value:
                    assert a in numbers,"poolsize is not int"
                requests.adapters.DEFAULT_POOLSIZE=int(value)
                assert 0<requests.adapters.DEFAULT_POOLSIZE,"poolsize<=0"
            elif key=="roleType":
                assert len(value)==1,"roleType is not byte"
                roleType=value
            elif key=="chrome_version":
                chrome_version0=value
            elif key=="threads":
                for a in value:
                    assert a in numbers,"threads is not int"
                threads=int(value)
            elif key=="logfile":
                if logfile:
                    logfile.close()
                logfile=open(value,"ab")
            elif key=="print":
                if value=="True":
                    console=True
                elif value=="False":
                    console=False
                else:
                    assert False,"print is not bool"
            elif key=="sleep_time":
                sleep_time=Fraction(value)
            else:
                assert False,"unknown param"
        ################
        if roleType!=default_roleType:
            match_url=join(("https://hfs-be.yunxiao.com/v2/users/matched-users?roleType=",roleType,"&account="))
        if chrome_version0!=default_chrome_version:
            chrome_version1=chrome_version0.split(".")[0]
            match_headers["user-agent"]=captcha0_headers["user-agent"]=captcha1_headers["user-agent"]=join(("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",chrome_version0," Safari/537.36"))
            match_headers["sec-ch-ua"]=captcha0_headers["sec-ch-ua"]=captcha1_headers["sec-ch-ua"]=join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\""))
        if logfile:
            stdout=stderr=logfile
        if __stdout__==stdout and __stderr__==stderr:   
            if console:
                write=stdout.write
            else:
                write=nothing
        else:
            if console:
                write_console=__stdout__.write
                write_logfile=stdout.write
                def write(data):
                    write_console(data)
                    write_logfile(data)
            else:
                write=stdout.write
        del numbers,console,requests,logfile,key,value,default_roleType,default_chrome_version
        #给每个线程一把锁,线程退出会解锁,主进程一直判断锁是否被锁定,来保证主进程在子线程之后退出并补充可能因报错或未知原因退出的子线程,每次循环sleep,不然主进程占cpu太多,线程不要开太多,差不多半组就够了,多了速度会慢
        if threads==1:
            del threads,a,sleep_time
            while True:
                send_loop(write)
        assert 1<threads,"threads<=0"
        class get_lock:
            locked=False
            def onlock(self):
                assert not self.locked,"onlock a locked lock"
                self.locked=True
            def unlock(self):
                assert self.locked,"unlock a unlocked lock"
                self.locked=False
        locks=[]
        for a in range(threads):
            lock=get_lock()
            lock.onlock()
            locks.append(lock)
            start_new_thread(send_loop,(write,lock.unlock))
        del threads
        locks=tuple(locks)
        while True:
            for a in locks:
                if not a.locked:
                    a.onlock()
                    start_new_thread(send_loop,(write,a.unlock))
            sleep(sleep_time)