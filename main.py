import time
from cvDiff import cvdiffv1
from capture import captureFull
from inputControl import mouseClick

#del
import pyautogui as pag


icon_template = './imageTemplates/icon_template.png'
launch_template = './imageTemplates/launch_template.png'
selserver_template = './imageTemplates/selserver_template_t.png'
connect_template = './imageTemplates/connect_template.png'

#TODO
#유사도를 이용한 이미지 찾기 https://infodbbase.tistory.com/146
# 이미지 diff http://egloos.zum.com/mcchae/v/11271797
# 탬플릿 매칭 https://www.geeksforgeeks.org/template-matching-using-opencv-in-python/
#pip install opencv-contrib-python
#초기화 
# 화면 사이즈 저장, 
# 윈도우, 맥 환경 확인
# 배틀넷은 실행중이어야 한다. 
#1. 화면 하단 캡쳐
path = captureFull()
point = cvdiffv1(path, icon_template,'cv2.TM_SQDIFF')
mouseClick(point)

#실행을 위한 일시적 기다림.
time.sleep(1)

#4. 화면전체 캡쳐
path = captureFull()
point = cvdiffv1(path, launch_template,'cv2.TM_SQDIFF')
mouseClick(point)

time.sleep(20)
#7. (512,216) (로그홀라) 커서 이동(테스트용 531,231) 
path = captureFull()
point = cvdiffv1(path, selserver_template,'cv2.TM_SQDIFF')
mouseClick(point)

#==========1단계 종료==========

# 판단로직 시작. 스케쥴이용 필요. 
# 서버 로그인 상태인지 아닌지 판단필요.
# 캐릭터 선택 필요.

# 대기 이후 
#11. 접속하기버튼(687,650) 모니터링이 된다면
time.sleep(4)
path = captureFull()
point = cvdiffv1(path, connect_template,'cv2.TM_SQDIFF')
mouseClick(point)

exit()

time.sleep(3)
pag.moveTo(687, 650)

pag.click()
#12. 클릭
#13. 1시간 후 접속종료 화면 확인하기(스캐쥴링)
#인게임 화면은 findimage모듈을 사용한다. 
# 화면이 튕기게 되면 findimage모듈에서 실패가 떨어지면
# 접속 종료 화면 확인  
#14. 확인누르고
#15. 아이디 패스워드입력
#16. 확인
#17. 7번으로 이동.


