import pyautogui
import threading

moveMouseUp = True
count = 1


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def moveMouse():
    global moveMouseUp
    global count
    pixelsToMove = 1 if moveMouseUp else -1
    pyautogui.moveRel(0, pixelsToMove)
    moveMouseUp = not moveMouseUp
    print('Moved mouse ' + str(count) + ' times')
    count += 1


set_interval(moveMouse, 60)
