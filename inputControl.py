import pyautogui as pag


def mouseClick( xy ):
    pag.moveTo(xy)
    pag.click()
