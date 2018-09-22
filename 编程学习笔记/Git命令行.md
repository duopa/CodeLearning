# 把本地文佳佳放入远程库
//初始化
git init

//增加所有文件到版本库
git add .

//提交本地修改
git commit -m 'initial commit'

//创建密钥对
ssh-keygen -t rsa -C “youremail@example.com”

//把公钥放到github网站上，新建一个仓库

//将本地仓库和远程仓库进行关联
git remote add origin git@github.com:orca123456/LearnNotes.git

//把本地文件上传到git上(第一次上传需要-u)
git push -u origin master

# Git忽略规则和.gitignore不生效的解决方法
https://www.cnblogs.com/zhangxiaoliu/p/6008038.html 

git rm -r –-cached .
git add .
git commit -m ‘update .gitignore’


# 提交更新的步骤
Git add .
git commit -m ‘Add title’
git push origin master
