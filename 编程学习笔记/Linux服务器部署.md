# 增加新用户，配置密钥登录
//增加用户
adduser imooc_manager
//把imooc_manager添加到sudo组
gpasswd -a imooc_manager sudo
//把imooc_manager设置成root相同的权限
sudo visudo
//用imooc_manager抄写root规则

//生成密钥对
ssh-keygen -t rsa -b 4096 -C orca123456@163.com

//在服务端创建.ssh文件夹下创建authorized_keys文件
vi authorized_keys
//然后把公钥复制到该文件中
//修改文件权限
chmod 600 authorized_keys
//重启服务
sudo service ssh restart

# 搭建Nodejs环境
//更新系统
sudo apt-get update
//安装相关模块或包
sudo apt-get install vim openssl build-essential libssl-dev wget curl git
//安装nvm
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
//关闭并重新打开一个终端
//安装node
nvm install v6.9.5
//指定版本号
nvm use v6.9.5
//设置默认版本
nvm alias default v6.9.5
//制定通过国内淘宝镜像下载
npm --registry=https://registry.npm.taobao.org install -g npm
//增加文件监控数目
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
//安装cnpm
npm --registry=https://registry.npm.taobao.org install -g cnpm
（//找不到模块时通过npm同步到国内镜像）
cnpm sync koa
//安装相关工具
npm i pm2 webpack gulp grunt-cli -g
# 修改登录端口
//配置文件
sudo vi /etc/ssh/sshd_config
//重启服务
sudo service ssh restart
//登录新的端口
ssh -p 39999 imooc_manager@120.26.235.4
# 关闭root和密码登录
//打开配置文件
sudo vi /etc/ssh/sshd_config
//修改配置文件
//重启服务
sudo service ssh restart
# 配置iptables
//Ubuntu升级更新
sudo apt-get update && sudo apt-get upgrade
//清空当前规则
sudo iptables -F
//新建配置文件
sudo vi /etc/iptables.up.rules

'''
*filter

// allow all connections
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

// allow out traffic 
-A OUTPUT -j ACCEPT

// all http https
-A INPUT -p tcp --dport 443 -j ACCEPT
-A INPUT -p tcp --dport 80 -j ACCEPT

// all ssh port login
-A INPUT -p tcp -m state --state NEW --dport 39999 -j ACCEPT
// ping
-A INPUT -p icmp -m icmp --icmp-type 8 -j ACCEPT

// log denied calls
-A INPUT -m limit --limit 5/min -j LOG --log-prefix “iptables denied:” --log-level 7

// drop incoming sensitive connections
-A INPUT -p tcp --dport 80 -i eth0 -m state --state NEW -m recent --set
-A INPUT -p tcp --dport 80 -i eth0 -m state --state NEW -m recent --update --seconds 60 --hitcount 150 -j DROP

// reject all other inbound
-A INPUT -j REJECT
-A FORWARD -j REJECT

COMMIT
'''

//设置iptables路径
sudo iptables-restore < /etc/iptables.up.rules
//查看防火墙是否启动
sudo ufw status
//激活防火墙
sudo ufw enable
//设置防火墙开机启动
sudo vi /etc/network/if-up.d/iptables
#!/bin/sh
iptables-restore /etc/iptables.up.rules
//修改脚本权限
sudo chmod +x /etc/network/if-up.d/iptables
# 安装fail2ban
//安装
sudo apt-get install fail2ban
//配置
sudo vi /etc/fail2ban/jail.config
//查看状态
sudo service fail2ban status
//关停
sudo service fail2ban stop
//开启
sudo service fail2ban start