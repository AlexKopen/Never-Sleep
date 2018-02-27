import pyautogui
import threading

moveMouseUp = True

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def moveMouse():
    global moveMouseUp
    pyautogui.moveRel(None, 10) if moveMouseUp else pyautogui.moveRel(None, -10)
    moveMouseUp = not moveMouseUp
    print ('Moved mouse')

set_interval(moveMouse, 3)
