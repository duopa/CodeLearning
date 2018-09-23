# 安装
//需要安装openssl
sudo yum install -y openssl -devel
//安装pip3 install scrapy

报错:error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": 
http://landinghub.visualstudio.com/visual-cpp-build-tools

解决方案:

打开网址 `http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted` 下载twisted对应版本的whl文件
（如我的Twisted-18.7.0-cp37-cp37m-win32.whl），cp后面是python版本，amd64代表64位
怎么查看版本python的版本呢？直接python,可以看到版本号37表示3.7版本36表示3.6版本,win32表示32位,
amd64表示64位,同理其他版本一样 
下载好对应的twisted然后我把它移动到 e:/python/
执行：pip install e:/python/Twisted-18.7.0-cp37-cp37m-win32.whl

文档参考1:https://www.jb51.net/article/125081.htm 
文档参考2:https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

再次执行: pip install scrapy 

没毛病的话,scrapy -version可以看到版本号
参考文献：https://blog.csdn.net/qq_27517377/article/details/82151264

# 创建项目
//新建项目
scrapy startproject douban
// 创建爬虫，cd到spider目录下
scrapy genspider douban_spider moive.douban.com

# 运行爬虫
scrapy crawl douban_spider
报错：
File "c:\program files\python37\lib\site-packages\twisted\conch\manhole.py", line 154
    def write(self, data, async=False):
解决方案：
python37中async是系统关键字，把manhole.py文件中所有的async改为async1

报错：
No module named 'win32api'
解决方案：
pip install pypiwin32


