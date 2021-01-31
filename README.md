# clean-up-low-pixels-images

清理「宽度/高度」小于 N 像素的图片

## 手动筛选

利用 windows 自带功能：

    文件夹内右键 ---> 查看 ---> 详细信息 ---> 列标签处右键 ---> 选中分辨率

## 利用 python

删除文件后不会放到回收站，网上有利用「pywin32」这个库来实现该效果

## portable version

- 下载 python 的 Windows embeddable package 版本
- [下载对应版本的 Pillow 库](https://pypi.org/project/Pillow/#files) （注意 python 版本以及系统架构）
- 将 whl 用 zip 格式解压缩，并放到 python 根目录

## installed version

- install python
- pip install virtualenv
- virtualenv env --no-site-packages
- source env/bin/activate （deactivate 退出虚拟环境）
- pip install Pillow
