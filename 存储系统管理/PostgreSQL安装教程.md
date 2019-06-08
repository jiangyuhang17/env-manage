## <center>**PostgreSQL安装教程**</center>
author : jyh
### **下载PostgreSQL安装包**

进入PostgreSQL官网，下载source版的tar.gz安装包
```shell
tar -zxvf postgresql-10.5.tar.gz
cd postgresql-10.5/
```

### **配置安装环境**

```shell
sudo apt install readline*
sudo apt install libreadline-dev
sudo apt install zlib*
sudo apt install openssl*
sudo apt install libssl-dev
sudo apt install libpython-dev python-numpy
```

####  **安装PostgreSQL**

```shell
./configure --prefix=/devdata1/postgresql-10.5/ --with-python --with-openssl --enable-debug
sudo make -j 100
sudo make install -j 100
```

####  **配置PostgreSQL相关内容**

设置符号链接
```shell
sudo ln -sf /devdata1/postgresql-10.5/ /devdata1/pgsql
cd /devdata1/pgsql
```

建立文件夹存放数据库数据
```
mkdir pgdata
cd pgdata
mkdir logfile
```

添加环境变量
```shell
vim ~/.bashrc
```

在最后添加下列数据 \
`export PATH=$PATH:/devdata1/pgsql/bin` \
`export LD_LIBRARY_PATH=/devdata1/pgsql/lib` \
`export PGDATA=/devdata1/pgsql/pgdata`
```shell
source ~/.bashrc
```

初始化数据库
```shell
initdb -D $PGDATA -E UTF8 --locale=C -U postgres
```

修改pgdata相关数据
```shell
vim pg_hba.conf
```
在86行下面新增一行信息 \
`host    all             all             0.0.0.0/0               trust`
```shell
vim postgresql.conf
```
修改内容（行号. 内容） \
41. `data_directory = '/devdata1/pgsql/pgdata'` \
43. `hba_file = '/devdata1/pgsql/pgdata/pg_hba.conf'` \
45. `ident_file = '/devdata1/pgsql/pgdata/pg_ident.conf'` \
59. `listen_addresses = '*' ` \
63. `port = 5432` \
344. `log_destination = 'stderr'` \
350. `logging_collector = on ` \
356. `log_directory = '/devdata1/pgsql/pgdata/logfile'` \
358. `log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'` \
360. `log_file_mode = 0600`

### **启动数据库**
```shell
pg_ctl -D $PGDATA start
```
运行在5432端口

### **进入psql控制台**
```shell
psql -U postgres
```
