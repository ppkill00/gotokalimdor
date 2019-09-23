from PIL import ImageGrab
import time
from slackbot import sendImgtoSlack

def captureFull(title):
    now = time.strftime('%y%m%d%H')
    img=ImageGrab.grab()
    saveas="./images/"+"{}{}".format(now,'.png')
    img.save(saveas)
    if title != None:
        sendImgtoSlack(saveas,title)
    return saveas

def captureRectangle(point,title):
    now = time.strftime('%y%m%d%H%M')
    img=ImageGrab.grab(bbox=point)
    saveas="./images/"+"{}{}".format(now,'_r.png')
    img.save(saveas)
    if title != None:
        sendImgtoSlack(saveas,title)
    return saveas