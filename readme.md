# 介绍

attack_hfs,攻击好分数,向好分数一直发送验证码请求,众所周知,发验证码是要钱的,~~但或许攻击的人多了也就变成了ddos~~

# 重大更新

### v3

##### 省流(回复TD进行退订,请不要回复TMD,TNND等)

log部分加了线程标识符且信息更美观

添加了"sleep_time"选项,去参数介绍看

单线程优化

启动速度换运行速度

##### 完整

重构了log部分,即使它不是线程安全的,会乱序输出,也可以解读了,因为每条信息前面加了线程标识符

log更加美观,性能更好(减少大量"."运算)

改写大量变量名

添加了"sleep_time"选项,可以自定义每次遍历线程列表的间隔,详见参数介绍

对单线程的优化,现在不用新开子进程了,当然sleep_time对单线程也不起作用了

启动时间稍微变长,但运行速度加快

以后可能会加jit,但要考虑一下兼容性

以后可能会加协程,但在每个线程内每个请求需要上一个请求的结果,所以可能会采用递归线程函数的方式(可以理解为实际并行请求数=线程数*协程数)

# 注意

### 1.

如果打开print线程一直报错,可以看看你是不是被hfs拉黑了,打开chrome f12看看请求是不是红的403

### 2.

不用担心你的电脑,这个程序占用的cpu,内存都不多,网络占用和log文件大小(如果有)看你开多少线程了,开4个线程的同时玩两个联网游戏完全没问题,在忽略多线程对性能的影响时,cpu为intel i7,主进程占用0.1%cpu,19.8mb内存,主进程不进行网络请求,如果线程数==1,可以近似的把主进程看做一个子线程,每个线程大约占用0.2%cpu,0.7mb内存,450-520kb/s上传,2.1-2.5mb/s下载

### 4.

如果线程因报错或其他未知原因退出,会新开一个线程的,不用担心攻击力度逐渐变小

### 5.

你可能会发现没有3,如果没发现,请回去发现一下再来看这条

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

python main.py  poolsize=[int] roleType=[byte] chrome_version=[str] threads=[int] logfile=[str] print=[bool] sleep_time=[rational]

# 参数介绍

### 总体规则

参数不必按顺序输入,将中括号(包括中括号)替换成值,所有参数都是可选的,不填就是默认参数,可重复,但后面的覆盖前面的

### poolsize

连接池大小,指定了requests可最多创建多少长连接,是**<u>uint,正整数</u>**类型,默认255

### roleType

发送的请求中的roleType,好分数疑似用来判断是学生还是家长,但只要是一个字节都可以,是**<u>byte,字节</u>**类型,默认"1"(学生)

### chrome_version

chrome版本,在请求头里有用,但一般没啥影响,不用管,是**<u>str,字符串</u>**类型,默认"96.0.4664.93"

### threads

发送请求的线程数,直接决定了你的攻击速度,一般半组就够了,多了反而会慢,是**<u>uint,正整数</u>**类型,默认1

### logfile

日志文件路径,类型是**<u>str,字符串</u>**,默认是输出到控制台,但可在print选项中设置不输出

### print

是否输出到控制台,即使logfile不是输出到控制台,只要print为True就会向控制台输出,类型是**<u>bool,只能输入"True"或"False"</u>**,默认是True

### sleep_time

每次遍历线程列表的间隔,单位秒,对单线程不起作用,是**<u>rational,有理数</u>**类型,具体可以是整数,浮点数或分数(分子/分母),默认是1

# 下载

### 所有系统通用

可以下载"attack_hfs_all.7z"

### 如果你连指令都不想输入,并且是windows64系统

可以下载"run64.bat"

然后和"attack_hfs_windows64.7z"解压出的"64"文件夹放到同一目录,运行即可

### 如果你连指令都不想输入,并且是windows86系统

可以下载"run86.bat"

然后和"attack_hfs_windows86.7z"解压出的"86"文件夹放到同一目录,运行即可

### 链接0

https://jiditaitan.lanzoup.com/b0113hv9i

密码:hg56th56gd6g

### 链接1

https://github.com/hg56th56gd6g/attack_hfs/releases/tag/3
