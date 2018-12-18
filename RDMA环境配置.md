## <center>**RDMA环境配置**</center>
author : jyh
### **安装Mellanox驱动**
下载对应操作系统的InfiniBand驱动程序 \
`http://cn.mellanox.com/page/software_overview_ib`

```shell
tar -zxvf MLNX_OFED_LINUX
cd MLNX_OFED_LINUX
sudo ./mlnxofedinstall
```

### **开启IB服务**
```shell
sudo /etc/init.d/openibd restart
sudo service start opensmd
ibstat
```

