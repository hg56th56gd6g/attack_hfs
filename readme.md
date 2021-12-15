# 介绍

attack_hfs,攻击好分数,向好分数一直发送验证码请求,众所周知,发验证码是要钱的,~~但或许攻击的人多了也就变成了ddos~~

# 系统和软件要求

### 所有系统通用

"python2.7.18"以及"requests"库

### 如果你没有达到软件要求并且你的系统是windows64

可以下载"attack_hfs_windows64.7z"

### 如果你没有达到软件要求并且你的系统是windows86

可以下载attack_hfs_windows86.7z

# 使用方法

### 所有系统通用

解压后打开控制台/命令行,进入解压目录,输入运行指令

# 指令格式

### 所有系统通用

##### 全是默认参数

python main.py

##### 自定义参数

python main.py  poolsize=[int] roleType=[byte] chrome_version=[str] threads=[int] logfile=[str] print=[bool]

# 参数介绍

### 总体规则

参数不必按顺序输入,将中括号(包括中括号)替换成值,所有参数都是可选的,不填就是默认参数,可重复,但后面的覆盖前面的

### poolsize

连接池大小,指定了requests可最多创建多少长连接,是**<u>int,数字</u>**类型,默认255

### roleType

发送的请求中的roleType,好分数疑似用来判断是学生还是家长,但只要是一个字节都可以,是**<u>byte,字节</u>**类型,默认"1"(学生)

### chrome_version

chrome版本,在请求头里有用,但一般没啥影响,不用管,是**<u>str,字符串</u>**类型,默认"96.0.4664.93"

### threads

发送请求的线程数,直接决定了你的攻击速度,一般半组就够了,多了反而会慢,是**<u>int,数字</u>**类型,默认1

### logfile

日志文件路径,类型是**<u>str,字符串</u>**,默认是输出到控制台,但可在print选项中设置不输出

### print

是否输出到控制台,即使logfile不是输出到控制台,只要print为True就会向控制台输出,类型是**<u>bool,只能输入"True"或"false"</u>**,默认是True

# 下载

### 所有系统通用

可以下载"attack_hfs_all.7z"

### 如果你连指令都不想输入,并且是windows64系统

可以下载"lazy_windows64_run.7z"

解压后直接运行"run.bat"

### 如果你连指令都不想输入,并且是windows86系统

可以下载"lazy_windows86_run.7z"

解压后直接运行"run.bat"

### 链接0

https://jiditaitan.lanzoup.com/b01132vwb
密码:fjeu

### 链接1

https://github.com/hg56th56gd6g/attack_hfs/releases/tag/1
