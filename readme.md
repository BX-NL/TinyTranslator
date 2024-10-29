# A Tiny Translator #

## 简介 | Introduction

A Tiny Translator是一个小巧的翻译工具
（~~或许并不小巧，可恶的Python让它的占用大了好几倍~~），

总之，它可以使用快捷键翻译选中的文本。

可以自动检测源语言，并翻译为您的目标语言，将结果显示在 Windows 通知中，并且可以随时粘贴。

A Tiny Translator is a tiny translation tool 
(~~Maybe not small, the abominable Python lead it to occupy several times larger~~),

In short, it can use shortcut key translation text.

It can automatically detect the source language and translate it as your target language. The results will be display in Windows notifications and you can paste it at any time.

## 功能 | Features ##

自动检测源语言。

Automatic detection source language.

将选中的文本翻译为另一种语言。

Translate the selected text into another language.

可自定义的快捷键（默认为 Ctrl + Alt + Q）。

Custom shortcut keys (default Ctrl + Alt + Q).

作为托盘图标在后台运行。

As a tray icon, run in the background.

简单直观的通知提示。

Simple and intuitive notification prompt.

自动复制到剪贴板，方便随时使用。

Automatically copy it to the clipboard, which is convenient to use at any time.

## 使用 | Installation ##

**1.直接使用 | Use directly：**

>[下载 | Download](https://github.com/BX-NL/A-Tiny-Translator/releases)

>并点击 A Little Translator.exe 启动程序

>And then, run 'A Little Translator.exe'.

**2.本地部署 | Local deployment:**

>下载源码 | Download the source code

    git clone https://github.com/BX-NL/A-Tiny-Translator.git
    cd A-Tiny-Translator

>安装依赖 | Install the dependences

    pip install -r requirements.txt

>然后 | Then

    python main.py

程序将在后台运行，复制文本并按下快捷键进行翻译。

The program will run in the background. Now you can copy the text and press the shortcut key for translation.

## Customization / 自定义 ##
You can change the hotkey by modifying the Hot_key variable in the script:

您可以通过修改脚本中的 Hot_key 变量来自定义快捷键：

## Setting ##

如果你需要修改这些设置，请使用本地部署。（或许有一天我会把这块改出来）

If you need to modify these settings, please use local deployment. (Maybe one day I will change this piece)

快捷键|Hot Key

>hot_key = 'Ctrl+Alt+Q'

您的语言|Your Language

>language = 'zh-cn'

选择翻译服务|Choose a translation service.

>selector = 'google'

通知弹出的时长|The timeout of the Notification (in seconds)

>timeout = 5

是否启用托盘图标|Whether to enable a tray icon

>use_tray_icon = True

## License / 许可证 ##

此项目基于 MIT 许可证 - 详情请参阅 LICENSE 文件。

This project is licensed under the MIT License - see the LICENSE file for details.
