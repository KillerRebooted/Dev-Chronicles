import keyboard
import time

def block_keyboard(bool):
    if bool:
        for i in range(150):
            keyboard.block_key(i)
    else:
        for i in range(150):
            keyboard.unblock_key(i)

def test(callback):
    print(callback.name)

keyboard.hook(test)

block_keyboard(True)

print("Keyboard is now Blocked.")

time.sleep(5)

block_keyboard(False)

print("Keyboard is now Unblocked.")

time.sleep(5)