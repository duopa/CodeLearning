# 购买AWS服务器
# 下载shadowsocks客户端
# 服务器操作
//安装依赖
//CentOS
yum install python-setuptools && easy_install pip
pip install shadowsocks
//Debian / Ubuntu:
apt-get install python-pip
pip install shadowsocks
//编辑文件(没有就新建)
vi /etc/shadowsocks.json
'''
{
    "server":"18.223.122.188"
    "server_port":8388,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"Cz123456",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open":false
}
'''
//运行
ssserver -c /etc/shadowsocks.json -d start
# 在客户端中添加信息