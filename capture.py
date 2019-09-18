from PIL import ImageGrab
import time

def captureFull():
    now = time.strftime('%y%m%d%H%M%S')
    img=ImageGrab.grab()
    saveas="./images/"+"{}{}".format(now,'.png')
    img.save(saveas)
    print(saveas)
    return saveas