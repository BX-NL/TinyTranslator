import time  # 计时器
import logging  # 日志模块
import keyboard  # 监听键盘输入
import threading  # 创建线程
import pyperclip  # 剪贴板
import pyautogui  # 控制系统

from PIL import Image, ImageDraw  # 画图标用的
from pystray import Icon, MenuItem, Menu  # 画图标用的
from googletrans import Translator  # 谷歌翻译API
from windows_toasts import Toast, WindowsToaster  # Windows Toast 通知

# 软件设置|Setting
# 快捷键|Hot Key
hot_key = 'Ctrl+Alt+Q'
# 您的语言|Your Language
language = 'zh-cn'
# 选择翻译服务|Choose a translation service.
selector = 'google'
# 通知弹出的时长|The timeout of the Notification (in seconds)
timeout = 5
# 是否启用托盘图标|Whether to enable a tray icon
use_tray_icon = True

# 创建Windows Toast通知对象
toaster = WindowsToaster("A Tiny Translator")

# 记录程序运行日志，仅供开发人员使用|Record program running logs, it only for developers.
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 翻译器模块|Translator module
class select_translator():
    def _google(text, dest_lang):
        # 使用谷歌翻译为目标语言|Use Google Translation as a destination language.
        translated = Translator().translate(text=text, dest=dest_lang)
        # 获取翻译后的结果|Get the result after translation
        translated_text = translated.text

        return translated_text

# 翻译模块|Translation module
def translate():
    def auto_copy():
        # 自动复制，可能不起作用，建议手动复制|Automatic copy, it may be not work, it is recommended to copy manually.
        # !存在问题，Python位于前台时，Ctrl+C会中止程序，在尝试其它方法
        # pyautogui.hotkey('Ctrl', 'C')
        # 延时0.5秒|Delay 0.5 seconds.
        time.sleep(0.5)
    # auto_copy()

    # 从剪贴板获取文本|Get text from the clipboard.
    text = pyperclip.paste()
    # 判断是否文本|Determine whether text.
    if type(text)==str:
        logger.info(f'Get the text content: {text}')
        try:
            # 创建对象|Create an object.
            translator = Translator()
            # 分析文本的源语言|Analyze the source language of the text
            detected = translator.detect(text)
            # 获取源语言|Get the source language of the text.
            src_lang = detected.lang

            # 判断语言以确认翻译目标|Determine language to confirm the destination language.
            if src_lang == 'en':
                dest_lang = language
            elif src_lang.startswith('zh'):
                dest_lang = 'en'
            else:
                dest_lang = language
            logging.info(f'Source language: {src_lang}, Destination language: {dest_lang}')

            # todo 未来可能增加其它翻译
            if selector=='google':
                translated_text = select_translator._google(text=text, dest_lang=dest_lang)
            logging.info(f'Get the translated text: {translated_text}')
            # 将结果复制到剪贴板|Copy the result to the clipboard.
            pyperclip.copy(translated_text)
            logging.info('The result has been copied to the clipboard.')

            return text, translated_text

        # 出现错误时发送通知|Send notification when there is an error.
        except Exception:
            logging.error(f'ERROR! Translator has some problem. {Exception}')
    else:
        logging.error('ERROR! Copy content is not text.')

def notify(text, translated_text):
    # 创建Windows Toast通知|Create a Windows Toast notification.
    new_toast = Toast()
    # 设置通知文本|Set notification text.
    new_toast.text_fields = [text, translated_text]
    # 回调函数，点击通知时执行命令，还没想好做什么
    # new_toast.on_activated = lambda _: print("Toast clicked!")
    # 发送系统通知|Send system notification.
    toaster.show_toast(new_toast)
    logging.info('The toast was be send.')

def translate_and_notify():
    text, translated_text = translate()
    notify(text=text, translated_text=translated_text)
    logging.info(f'Waiting the hot key: {hot_key}')


# 监听键盘快捷键|Monitor keyboard shortcut
def monitor_keys():
    logging.info(f'Waiting the hot key: {hot_key}')

    while True:
        # 添加快捷键|Add hot key
        keyboard.add_hotkey(hotkey=hot_key, callback=translate_and_notify)
        # 等待按键被按下|Wait for the hotkey to be pressed.
        keyboard.wait()


# 托盘图标|Tray icon
def tray_icon():
    # 退出功能|Exit function
    def quit_action(icon, item):
        icon.stop()

    # 绘制图标|Draw the icon
    icon_image = Image.new(mode='RGB', size=(64, 64), color=(255, 255, 255))
    draw = ImageDraw.Draw(im=icon_image)
    draw.rectangle(xy=(16, 16, 48, 48), fill=(102,204,255))

    # 制作菜单|Create the menu
    menu = Menu(MenuItem(text='退出 | quit', action=quit_action))
    icon = Icon(name="translator", icon=icon_image, menu=menu)

    # 创建托盘图标|Start the tray icon
    icon.run()

# mian
def main():
    logging.info('The programme has started.')
    # 开始监听键盘快捷键|Start listening to keyboard shortcuts.
    t = threading.Thread(target=monitor_keys, daemon=True)
    logging.info('Keyboard listener was online.')
    t.start()
    
    if use_tray_icon:
        # 启动系统托盘图标|Create a tray icon.
        tray_icon()
        
    else:
        logging.warning('The tray icon has been closed')
        # 不使用托盘图标，使用sleep()挂起线程|Without the tray icon, use Sleep() to hang the thread.
        while True:
            time.sleep(10)


if __name__ == "__main__":
    main()
