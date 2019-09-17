import pyautogui as pag
import time

while True:
    x, y = pag.position()
    print('x좌표 : %s, y좌표 : %s' % (x , y)) #1365, 767

# pag.moveTo(200, 200)
# pag.click()
