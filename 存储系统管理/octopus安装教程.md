## <center>**清华octopus安装教程**</center>
author : jyh
### **软件介绍**
octopus是清华大学 Storage Research Group 设计并实现的基于RDMA的分布式非易失性内存文件系统 \
代码在github上开源 : `https://github.com/thustorage/octopus.git`

## Ubuntu 16
### **环境配置**
```shell
sudo apt install libfuse-dev libcrypto++-dev libboost-dev libibverbs-dev libssl-dev g++ cmake mpich
```
根据 参考资料 3 安装Oracle JDK，配置环境变量
```
export JAVA_HOME=/usr/java/jdk1.8.0_191-amd64
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin
```
### **安装过程**
```shell
git clone https://github.com/thustorage/octopus.git
cd octopus
```
由于清华的CMakeLists.txt只针对fedora系统，所以需要换成自己写的CMakeLists.txt \
修改conf.xml的id和ip，并在/etc/hosts中添加ip和主机号（注意不是用户名,且要添加非localhost的第一位）
```shell
sudo /etc/init.d/networking restart
```
```shell
mkdir build
cmake ..
make -j8
```

### **运行方式**
server端
```shell
sudo ./dmfs
```

client端
```shell
sudo ./mpibw op_time block_time(K)
```

## fedora 27
### **环境配置**
```shell
sudo yum install fuse-devel cryptopp-devel boost-devel libibverbs-devel gcc-c++ openssl-devel cmake mpic**
```
根据 `参考资料 1` 为mpicxx配置环境变量
```
export PATH=/usr/lib64/mpich/bin:$PATH
export INCLUDE=/usr/include/mpich-x86_64:$INCLUDE
export LD_LIBRARY_PATH=/usr/lib64/mpich/lib:$LD_LIBRARY_PATH
```
根据 `参考资料 2` 删除系统自带的JDK \
根据 `参考资料 3` 安装Oracle JDK，配置环境变量
```
export JAVA_HOME=/usr/java/jdk1.8.0_191-amd64
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin
```

### **安装过程**
```shell
git clone https://github.com/thustorage/octopus.git
cd octopus
mkdir build
cmake ..
make -j8
```

### **参考资料**
1. https://blog.csdn.net/kingdomkitty/article/details/80258364
2. https://blog.csdn.net/max_chau/article/details/79313660
3. https://www.cnblogs.com/xuzhiwei/p/4993035.html