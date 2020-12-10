## <center>**RDMA环境配置**</center>
author : jyh
### **安装Mellanox驱动**
下载对应操作系统的InfiniBand驱动程序 \
`http://cn.mellanox.com/page/software_overview_ib`

```shell
tar -zxvf MLNX_OFED_LINUX
cd MLNX_OFED_LINUX
sudo yum install python2-libxml2 tcsh tk
sudo ./mlnxofedinstall
```

**PS**:BIOS的Secure Boot可能导致驱动安装失败！！！

### **开启IB服务**
```shell
sudo /etc/init.d/openibd restart
sudo /etc/init.d/opensmd restart
ibstat
sudo chkconfig openibd on
sudo chkconfig opensmd on
reboot
```

### **设置IP地址**
#### Fedora
重启后，可以在`/etc/sysconfig/network-scripts/`中看见ifcfg-ib0文件 \
修改文件部分参数
```
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.0.23
NETMASK=255.255.255.0
NETWORK=192.168.0.0
```
重启网络服务
```shell
sudo service network restart
```

### **参考资料**
1. https://blog.csdn.net/u010587433/article/details/42076437/
