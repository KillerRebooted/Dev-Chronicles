from winotify import Notification, audio
import os, pystray, sys
from PIL import Image

cur_dir = os.path.dirname(os.path.realpath(__file__))

#Notification
toast = Notification(app_id="Test", title="Important Info", msg="Click This!!", duration="short", icon=f"{cur_dir}\\Cupid Bot.jpeg")

toast.set_audio(audio.Default, loop=False)

toast.add_actions(label="Yes, This", launch="https://youtube.com")

toast.show()

#System Tray Icon
image = Image.open(f"{cur_dir}\\Cupid Bot.jpeg")

def quit_bot(icon, item):
    if str(item) == "Exit":
        os._exit(0)
    if str(item) == "Restart":
        os.execl(sys.executable, sys.executable, f'"{__file__}"')

icon = pystray.Icon("Test Icon", image, "Test Icon", menu=pystray.Menu(pystray.MenuItem("Restart", quit_bot), pystray.MenuItem("Exit", quit_bot)))

icon.run()