# 下载地址
Msysgit https://git-scm.com/download.win



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

# Git忽略文件配置
    #           表示此为注释,将被Git忽略
*.a             表示忽略所有 .a 结尾的文件
!lib.a          表示但lib.a除外
/TODO           表示仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO
build/          表示忽略 build/目录下的所有文件，过滤整个build文件夹；
doc/*.txt       表示会忽略doc/notes.txt但不包括 doc/server/arch.txt
 
bin/:           表示忽略当前路径下的bin文件夹，该文件夹下的所有内容都会被忽略，不忽略 bin 文件
/bin:           表示忽略根目录下的bin文件
/*.c:           表示忽略cat.c，不忽略 build/cat.c
debug/*.obj:    表示忽略debug/io.obj，不忽略 debug/common/io.obj和tools/debug/io.obj
**/foo:         表示忽略/foo,a/foo,a/b/foo等
a/**/b:         表示忽略a/b, a/x/b,a/x/y/b等
!/bin/run.sh    表示不忽略bin目录下的run.sh文件
*.log:          表示忽略所有 .log 文件
config.php:     表示忽略当前路径的 config.php 文件
 
/mtk/           表示过滤整个文件夹
*.zip           表示过滤所有.zip文件
/mtk/do.c       表示过滤某个具体文件

# Git忽略规则和.gitignore不生效的解决方法
https://www.cnblogs.com/zhangxiaoliu/p/6008038.html 

git rm -r –-cached .
git add .
git commit -m ‘update .gitignore’


# 提交更新的步骤
Git add .
git commit -m ‘Add title’
git push origin master

# 其他命令
//查询git配置
git config --list

#配置用户信息
git config --global user.name "tyler"
git config --global user.email "tyler@163.com"

# git工作流
//清理当前工作目录
clear
//查看目录
ll
//查看当前状态
git status
//添加到暂存区
git add .
//添加到本地仓库
git commit -m "commit notes"
//从暂存区回归到工作区
git reset HEAD bash_demo.txt
//回退工作区的文件的更改内容
git checkout -- bash_demo.txt
//查询日志
git log
//复制上一次的commit号，进行回滚，包括最终仓库和暂存区文件
git reset --hard dfadf8708a7d0f89a6s0df8adf97a60df8a6d09
//清除工作区文件
git rm bash_demo.txt
//清楚暂存区和仓库去
git commit -m "delete bash demo"

# 远程仓库
//创建密钥对
ssh-keygen -t rsa -C “youremail@example.com”
//查看本地仓库和github是否连通
ssh -T git@github.com
//新建README文档（>>表示追加）
echo “# tyler_muke” >> README.md
git init
//添加到暂存仓库
git add README.md
git commit -m "first commit"
//把本地仓库和远程仓库关联起来（需要先在github上新建仓库）
git remote add origin git@github.com:tylerdemo/tyler_muke.git
//-u是把本地master与远程master关联起来
git push -u origin master
git pull origin master --allow-unrelated-histories

# 标签管理
//列出当前所有标签
git tag
//基于当前分支当前commitID创建标签
git tag v1.0.1
//添加信息
git tag -a name -m "comment"
//删除标签
git tag -d name
//推送到仓库
git push origin v1.0.1

# 分支管理
//创建分支
git branch branch_name
//查看分支
git branch
//切换分支
git checkout branch_name
//先切换到master分支，再合并到master分支
git checkout master
git merge branch_name
//删除分支
git branch -d branchName









