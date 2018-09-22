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
