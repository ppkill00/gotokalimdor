import time, schedule, signal, os, subprocess
from cvDiff import cvdiffv1
from capture import captureFull, captureRectangle
from inputControl import mouseClick, mouseRclick
from imgDiff import imgDiffv1
from slackbot import sendTexttoSlack, sendImgtoSlack

#del
import pyautogui as pag


icon_template = './imageTemplates/icon_template.png'
launch_template = './imageTemplates/launch_template.png'
selserver_template = './imageTemplates/selserver_template.png'
# selserver_template = './imageTemplates/selserver_template_t.png'
connect_template = './imageTemplates/connect_template.png'
ingame_template = './imageTemplates/ingame_template.png'
wow_template = './imageTemplates/wow_template.png'
path = './images/1909222008_r.png'


def sigint_handler(signum, frame):
    print ('Stop pressing the CTRL+C!')
    print(str(signum))
    exit()
    pass

#TODO
#유사도를 이용한 이미지 찾기 https://infodbbase.tistory.com/146
# 이미지 diff http://egloos.zum.com/mcchae/v/11271797
# 탬플릿 매칭 https://www.geeksforgeeks.org/template-matching-using-opencv-in-python/
#pip install opencv-contrib-python
# 초기화 
# 화면 사이즈 저장, 
# 윈도우, 맥 환경 확인
# 배틀넷은 실행중이어야 한다.

# 클라이언트 실행 기능 


def connectWow():
    path = captureFull("최초접속")
    point = cvdiffv1(path, icon_template,'cv2.TM_SQDIFF')
    mouseClick(point)
    #실행을 위한 대기
    time.sleep(1)
    #4. 화면전체 캡쳐
    path = captureFull("게임실행")
    point = cvdiffv1(path, launch_template,'cv2.TM_SQDIFF')
    mouseClick(point)
    time.sleep(15)
    # 와우 클라이언트 접속 기능.
    #7. (512,216) (로그홀라) 커서 이동(테스트용 531,231) 
    path = captureFull("서버 선택 및 접속")
    point = cvdiffv1(path, selserver_template,'cv2.TM_SQDIFF')
    mouseClick(point)
    sendTexttoSlack('와우 초기화 및 접속 단계 완료')
    amIwait()
    

#==========1단계 종료==========

# 판단로직 시작. 스케쥴이용 필요. 
# 대기 화면 not ingame
# 서버 로그인 상태인지 아닌지 판단필요.
# 캐릭터 선택 필요.
# 대기 이후 
#11. 접속하기버튼(687,650) 모니터링이 된다면

def amIwait():
    print("am I wait")
    time.sleep(5)
    captureFull("대기 화면 또는 케릭터 선택화면")
    point =(500,588,770,767)
    while True:
        path = captureRectangle(point,None)
        if imgDiffv1(path,connect_template): ##원 사이즈랑 차이가 나면 이슈
            #connect phase
            fpath = captureFull("게임 시작, 접속하기")
            point = cvdiffv1(fpath, connect_template,'cv2.TM_SQDIFF')
            mouseClick(point)
            time.sleep(10)
            sendTexttoSlack('대기상태 종료')
            break
        else:
            time.sleep(5)
            print('not ingame')
    print("exit amIwait")

def checkIngame():
    print("check In game")
    captureFull("게임 시작, 접속하기")
    # point = (0,636,1365,767)
    point = (104,608,290,767)
    path = captureRectangle(point,None)
    if imgDiffv1(path,ingame_template):
        print("ingame")        

    else:
        # need wait...
        print('not ingame')
        
        exitWow()
        time.sleep(5)
        connectWow()
        
def exitWow():
    fpath = captureFull("종료되는 상황 확인")
    point = cvdiffv1(fpath, wow_template,'cv2.TM_SQDIFF')
    mouseRclick(point)
    pag.press('up')
    pag.press('enter')




# path = captureFull()
# point = cvdiffv1(path, connect_template,'cv2.TM_SQDIFF')
# mouseClick(point)


#접속 성공 -> 캐릭터 이동, 매크로 사용, 따라가기 및 말하기, 인벤토리 확인 등의 업무 수행


#12. 클릭
#13. 1시간 후 접속종료 화면 확인하기(스캐쥴링)
# 인게임 화면은 findimage모듈을 사용한다. 
# 화면이 튕기게 되면 findimage모듈에서 실패가 떨어지면
# 접속 종료 화면 확인
# 
#   
#14. 확인누르고ok_template
#15. 아이디 패스워드입력 ppkill00@gmail.com 
#16. 확인
#17. 7번으로 이동.


# schedule.every(10).minutes.do(checkIngame)
schedule.every(10).seconds.do(checkIngame)


signal.signal(signal.SIGINT, sigint_handler)  #ctrl-c 예외 처리.


if __name__ == '__main__':
    connectWow() #최초 로그인 부터 시작.
    while True:
        schedule.run_pending()

