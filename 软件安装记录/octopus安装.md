## <center>**清华octopus安装教程**</center>
author : jyh
### **软件介绍**
octopus是清华大学 Storage Research Group 设计并实现的基于RDMA的分布式非易失性内存文件系统 \
代码在github上开源 : `https://github.com/thustorage/octopus.git`

### **环境配置**
```shell
sudo yum install fuse-devel cryptopp-devel boost-devel libibverbs libibverbs-devel gcc-c++ openssl-devel cmake mpic**
```
根据 `参考资料 1` 为mpicxx配置环境变量
```
export PATH=/usr/lib64/mpich/bin:$PATH
export INCLUDE=/usr/include/mpich-x86_64:$INCLUDE
export LD_LIBRARY_PATH=/usr/lib64/mpich/lib:$LD_LIBRARY_PATH
```
根据 `参考资料 2` 删除系统自带的JDK \
根据 `参考资料 3` 安装Oracle JDK，配置环境变量

### **安装过程**
在主机上安装 `fedora 27` 操作系统
```shell
git clone https://github.com/thustorage/octopus.git
cd octopus
mkdir build
```

### **参考资料**
1. https://blog.csdn.net/kingdomkitty/article/details/80258364
2. https://blog.csdn.net/max_chau/article/details/79313660
3. https://www.cnblogs.com/xuzhiwei/p/4993035.html