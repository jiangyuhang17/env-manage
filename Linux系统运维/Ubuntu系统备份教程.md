## <center>**Ubuntu系统备份教程**</center>
author : jyh
### **系统备份**

将所有备份数据都放在`/media`内

备份 `/` 目录
```shell
sudo tar -cvpzf /media/ubuntu-root-backup@`date +%Y-%m+%d`.tar.gz --exclude=/boot --exclude=/cdrom --exclude=/devdata1 --exclude=/devdata2 --exclude=/home --exclude=/lost+found --exclude=/media --exclude=/mnt --exclude=/proc --exclude=/run --exclude=/tmp --exclude=/sys --exclude=/dev /
```

备份 `/home` 目录
```shell
sudo tar -cvpzf /media/ubuntu-home-backup@`date +%Y-%m+%d`.tar.gz /home
```

备份 `/devdata1` 目录
```shell
sudo tar -cvpzf /media/ubuntu-devdata1-backup@`date +%Y-%m+%d`.tar.gz --exclude=/devdata1/lost+found /devdata1
```

### **系统还原**

还原 `/` 目录
```shell
sudo tar -xvpzf /media/ubuntu-root-backup@2018-09+26.tar.gz -C /
```

还原 `/home` 目录
```shell
sudo tar -xvpzf /media/ubuntu-home-backup@2018-09+26.tar.gz -C /
```

还原 `/devdata1` 目录
```shell
sudo tar -xvpzf /media/ubuntu-devdata1-backup@2018-09+26.tar.gz -C /
```

### **参考资料**
1. https://blog.csdn.net/qq_35523593/article/details/78545530