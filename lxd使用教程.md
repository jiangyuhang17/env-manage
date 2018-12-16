## <center>**LXD使用教程**</center>
author : jyh
### **概述**

LXC (Linux Container)，内核虚拟化技术，提供轻量级的虚拟化，以便隔离进程和资源

LXC中可以装许多小的容器，每个容器都具备完整的运行环境，如特定cpu，memory节点，可分配的cpu时间，IO时间，受限的内存大小(内存和swap)，提供对底层设备的访问，拥有独立的namespace(网络、pid、ipc、mmt和uts)

LXD是提供了REST API的LXC容器管理器，解决了LXC的一些缺陷 \
LXD拆分为daemon (命令为lxd) 和客户端 (命令为lxc)

### **<center>Ubuntu16.04使用LXD教程</center>**

### **安装LXD及初始配置**

```shell
# 安装lxd
sudo apt-get install lxd
# 将用户添加到lxd组，最后一个参数为用户名
sudo usermod --append --groups lxd jyh
# 安装存储后端ZFS，可以用LVM不过相对麻烦
sudo apt-get install zfsutils-linux
# LXD初始配置
sudo lxd init
```
初始配置时，前面回车默认，遇到设置IPv6的选择No

![avatar](./pic/lxd-init-1.png)

重新配置`sudo lxd init`时，要删除库中原有的容器和镜像 \
参考资料：https://blog.simos.info/how-to-initialize-lxd-again/


### **创建新容器**

```shell
# 创建容器
lxc launch ubuntu:16.04 jyh
# 查看已有容器
lxc list
```

![avatar](./pic/lxd-container-1.png)

### **进入容器**

```shell
# 以root身份进入容器
lxc exec jyh /bin/bash
```
可以看出容器里面是个微型操作系统

![avatar](./pic/lxd-exec-1.png)

### **宿主机分享文件给容器**

```shell
# 这行命令很重要，避免ipmaps带来的权限问题
lxc config set jyh security.privileged true
# 将宿主机上的/tmp的文件分享到容器的/tmp/share目录下
lxc config device add jyh tmpshare disk path=/tmp/share source=/tmp
```
经测试，宿主机和容器均能对共享文件进行读写，共享文件始终保持一致性，且不会占用容器的空间

![avatar](./pic/lxd-share-1.png)

取消文件共享
```shell
lxc config device remove jyh tmpshare
```

![avatar](./pic/lxd-share-2.png)

### **测试共享文件中OrientDB的使用**

先将OrientDB文件解压到~/Downloads下，在执行共享文件操作
```shell
lxc config set jyh security.privileged true
lxc config device add jyh orientdb disk path=/root/orientdb source=~/Downloads/orientdb-3.0.7
```

![avatar](./pic/lxd-share-3.png)

配置JAVA环境，其实也可以用分享文件的方式建立JAVA环境
```shell
sudo apt install openjdk-8-jdk
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
```

进入容器，开启OrientDB服务
```shell
lxc exec jyh /bin/bash
cd orientdb/bin
./server.sh
```

开启服务后，可以在宿主机上用容器的IPv4地址加上端口号打开浏览器，如`10.107.155.22:2480`打开OrientDB界面

### **创建快照**

```shell
# 创建快照
# lxc snapshot <container> <snapshot name>
lxc snapshot jyh jyhsnap1
# 列出所有快照
# lxc info <container>
lxc info jyh
# 恢复快照
# lxc restore <container> <snapshot name>
lxc restore jyh jyhsnap1
# 从快照中创建一个新的容器
# lxc copy <source container>/<snapshot name> <destination container>
lxc copy jyhsnap1 jyh2
```

### 参考资料
1. https://linux.cn/article-7618-1.html?spm=a2c4e.11153940.blogcont88134.9.4bcd1586nm0cvb
2. https://askubuntu.com/questions/691039/adding-a-shared-host-directory-to-an-lxc-lxd-container