安装

```
git clone https://github.com/xia0ji233/srun_login
```

自己修改一下`login.py`  的 username 和 password 字段，换上自己的账号和密码即可。

这里解释一下用户名构成：用户名为自己的一卡通号加上@运营商，比如我的一卡通号码是00001818，然后用的是中国电信，那么我的账号就是00001818@chinanet

移动后面添加@cmcc

联通后面添加@unicom

校内网登录后面添加@xn(in 嘉兴学院，其它学校的校内网可以自己抓包看看，三大运营商的应该是不会变的)

登录

```
python login.py
```

如果想要开机自启动呢，可以做一个shell脚本，然后里面写上python {login.py的路径}

或者是自己写一个C程序，main函数里面直接写system("python {login.py的路径}")

注意{login.py的路径}最好是绝对地址，保证你这个文件在任意位置都能成功执行这个python脚本。

本python脚本用到了如下库，依赖冲突的问题并不大，所以缺哪个自己pip安装一下就好了。

```
requests
hashlib
```

具体分析过程详情请见我博客：https://xia0ji233.pro/2021/12/08/%E6%A0%A1%E5%9B%AD%E7%BD%91%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95/

分析过程参考的博客：https://blog.csdn.net/qq_41797946/article/details/89417722
