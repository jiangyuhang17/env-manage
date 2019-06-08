## <center>**Hadoop安装教程**</center>
author : jyh

### **实验环境**
三台Ubuntu16.04虚拟机（VirtualBox）

### **环境配置**

**Java环境**  
在Oracle官网下载JDK
```bash
sudo tar -xzvf jdk-8u212-linux-x64.tar.gz -C /usr/local/java
```
配置Java环境变量
```bash
export JAVA_HOME=/usr/local/java/jdk1.8.0_212
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin
```

**SSH免密码登陆**
```bash
sudo apt-get install ssh
#  生成公钥私钥
ssh-keygen -t rsa
# ssh localhost免密登陆
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

### **软件安装**
从Apache官网下载hadoop
```bash
tar -xzvf hadoop-3.2.0.tar.gz -C ~/
```

配置Hadoop环境变量
```bash
export HADOOP_PATH=/home/hadoop-master/hadoop-3.2.0
export PATH=$PATH:$HADOOP_PATH/bin:$HADOOP_PATH/sbin
```

### **软件配置**
### （一） 伪分布式Hadoop
#### 修改配置文件
指定JDK的安装位置 `etc/hadoop/hadoop-env.sh`
```bash
export JAVA_HOME=/usr/local/java/jdk1.8.0_212
```

配置HDFS的地址和端口号 `etc/hadoop/core-site.xml`
```xml
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

HDFS备份方式由3改为1 `etc/hadoop/hdfs-site.xml`
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

配置MapReduce中JobTracker的地址和端口 `etc/hadoop/mapred-site.xml`
```xml
<configuration>
    <property>
        <name>mapred.job.tracker</name>
        <value>localhost:9001</value>
    </property>
</configuration>
```

#### 启动Hadoop
```bash
# 格式化文件系统
$HADOOP/bin/hadoop namenode -format
# 启动所有进程
$HADOOP/sbin/start-all.sh
```
输入网址 `http://localhost:8088` 进入hadoop管理页面 
输入网址 `http://localhost:9870` 进入namenode页面  
输入网址 `http://localhost:9864` 进入datanode页面