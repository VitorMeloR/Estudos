import pyautogui as pg
import time

pg.hotkey('win','tab')
time.sleep(1)
pg.press('tab')
time.sleep(2)
pg.press('right')
time.sleep(1)
pg.press('enter')
while True:
    time.sleep(4)
    print(pg.position())