## 数据库初始化

+ 根据已有数据库表初始化
  + 首先是确保可以连接上MySQL，安装了相关的mysql包，比如直接使用`pip install pymysql`
  + 在工程的`__init__.py`文件里添加如下配置
  ``` python
  import pymysql
  pymysql.install_as_MySQLdb()
  ```
  + 编辑`settings.py`将`app`加入工程
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grammar_correction', #加入的app名称
    ]
  ```
  + 进入项目路径，输入一下命令
  ```
  python .\manage.py inspectdb > .\grammar_correction\models.py
  ```

+ 根据`models.py`进行初始化
  + 在`models.py`文件中进行编辑，建立合适的数据库表
  + 编辑`settings.py`将`app`加入工程
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grammar_correction', #加入的app名称
    ]
  ```
  + 打开控制台，进入项目路径，输入一下命令
  ```
  Django 1.7.1及以上 用以下命令
  # 1. 创建更改的文件
  python manage.py makemigrations
  # 2. 将生成的py文件应用到数据库
  python manage.py migrate
  旧版本的Django 1.6及以下用
  python manage.py syncdb
  ```
  + 在进行上一步的时候控制台不报错就可以