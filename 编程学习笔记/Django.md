# 安装
pip install Django==2.1.1

//查看版本
python -m django --version

# 创建项目
django-admin startproject myblog

# 运行项目
python manage.py runserver
//更改端口号，默认是8000
python manage.py runserver 9999

# 创建APP
python manage.py startapp blog


//生成SQL语句
python manage.py makemigrations
python manage.py migrate
//查看SQL语句
python manage.py sqlmigrate appname fileid

