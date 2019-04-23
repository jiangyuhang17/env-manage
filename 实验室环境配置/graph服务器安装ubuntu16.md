## <center>**graph服务器安装Ubuntu16系统**</center>

### **步骤一**

拔出服务器显卡，换成实验室GTX的显卡

### **步骤二**

用u盘启动盘安装`Ubuntu 16.04.4`

####  **步骤三**

进入系统，在执行下列命令,修改`blacklist.conf`文件
```shell
sudo apt install vim
sudo vim /etc/modprobe.d/blacklist.conf
```
在`blacklist.conf`最后两行添加，为了禁用nouveau第三方驱动： \
`blacklist nouveau` \
`options nouveau modeset=0`

保存修改之后，执行下列命令来刷新内核：
```shell
sudo update-initramfs -u
```

### **步骤四**

关闭电脑，取出GTX显卡，换成服务器原来的显卡，重新开机即可 

