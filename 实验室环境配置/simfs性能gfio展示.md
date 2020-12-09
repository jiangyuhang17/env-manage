## <center>**simfs性能gfio展示**</center>
author : jyh
## **文件在NAS中的位置**
/lab/software/simfs/simfs性能gfio展示

## **编译Linux内核**
在Ubuntu16上，编译内核 `linux-4.4.30-simfs-simulator`

```bash
# 定位不到软件包——sudo apt update
# 软件包依赖问题——sudo apt -f install
sudo apt install libncurses5-dev
sudo apt install libssl-dev
cd linux-4.4.30
sudo make menuconfig
```

在menuconfig图形界面 \
输入 `/` 进行查找配置参数，输入 `cmdline` 回车 \
再接着输入 `1` 选择第一个选项，进入后回车 \
填入 `memmap=500M!1G memmap=500M!2G memmap=4G!4G` (memmap=a!b —— 从b开始预留a大小的内存) \
最后保存退出menuconfig。

```bash
sudo make -j80
sudo make modules_install
sudo make install
```

对于Ubuntu16,可能出现开机没有选择内核的界面的情况（开机不停按shift键亦可）

```bash
vi /etc/default/grub
```
将 `GRUB_HIDDEN_TIMEOUT=0` 一行注释（#）
```bash
sudo update-grub
```

## **挂载文件系统**
在相应文件系统模块目录下执行 `setup_XXXX.sh` 脚本，用 `df -hT` 确认

## **安装fio**
为了兼容性，安装fio-2.1.10

```bash
cd fio-2.1.10
./configure --enable-gfio
make -j80
make install
```

fio 及 gfio 可执行文件在 `/usr/local/bin` 里面

```bash
# 开启fio作为server
./fio -S
# 开启gfio图形界面
./gfio
# 若gfio无法连接fio server，查看当前进程，杀死残留的./gfio进程
ps aux
kill -9 jobnumber
```

## **编写fio测试文件**
test.fio
```fio
[global]
rw=randread
size=1g
numjobs=1
iodepth=32
buffered=0
direct=1
directory=/mnt/simfs

[simfs]
bs=4K

[simfs]
bs=4K
```
