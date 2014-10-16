说明
#####1.文件目录解释
+ installcopy.py ---类似windows的copy命令, 安装固定的格式将文件追加的exe的末尾
+ copyreverseparse.py --- 逆向测试生成的exe是否可用

#####2.如何将installcopy.py打包成独立的exe
+ 安装[python27](https://www.python.org/ftp/python/2.7/python-2.7.msi)
+ 安装pyinstaller(https://github.com/pyinstaller/pyinstaller) 或者 pip install pyinstaller 
+ pyinstaller -F -i images/copy.ico --distpath=distwin installcopy.py