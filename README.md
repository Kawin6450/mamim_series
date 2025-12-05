# manim_series
Python下载
---
> https://mirrors.huaweicloud.com/python/3.13.7/python-3.13.7-amd64.exe

这里我们不讲安装过程，自己去这里看
---
> https://blog.csdn.net/sensen_kiss/article/details/141940274

由于pip默认下载源很慢，这里我们改用清华源

cmd
---
> pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

然后开始安装
---
> pip install manim

需要配合ffmpeg使用
---
> https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z

为了方便在命令行中直接调用 FFmpeg，需要将其添加到系统的环境变量中。
---
在桌面左下角开始菜单搜索"菜单"，找到"编辑编辑环境变量"，然后点击打开。
点击“环境变量”按钮。
找到“系统变量”中的 Path 条目并点击“编辑”。
在“编辑环境变量”窗口中，点击“新建”，输入 FFmpeg 的 bin 文件夹路径。
依次点击“确定”以保存设置（三个“确定”缺一不可）。
注意：确保路径准确，以便系统能正确找到 FFmpeg 文件。
测试安装是否成功
按 Win + R 键，输入 cmd 打开命令行窗口。
在命令行中输入以下命令查看 FFmpeg 版本：
> ffmpeg -version
如果正确显示 FFmpeg 版本号和相关信息，说明安装成功。
