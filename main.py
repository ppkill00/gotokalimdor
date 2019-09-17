import pyautogui as pag
import time


#TODO
#유사도를 이용한 이미지 찾기 https://infodbbase.tistory.com/146
# 이미지 diff http://egloos.zum.com/mcchae/v/11271797
# 탬플릿 매칭 https://www.geeksforgeeks.org/template-matching-using-opencv-in-python/
#pip install opencv-contrib-python
#초기화 
# 배틀넷은 실행중이어야 한다. 
#1. 화면 하단 캡쳐
#2. 배틀넷 아이콘 위치 확인(1048,737)
pag.moveTo(1048, 737)
pag.click()

time.sleep(3)
#4. 화면전체 캡쳐
#5. 게임시작 위치 확인 (274,560)
pag.moveTo(374, 658)
time.sleep(1)
pag.click()

time.sleep(30)
#7. (512,216) (로그홀라) 커서 이동(테스트용 531,231) 
pag.moveTo(531, 231)
pag.click()

time.sleep(3)
#9. 확인버튼(785,564) 이동 
pag.moveTo(785, 564)

pag.click()
# 대기가 발생한다. 
# 대기 이후 
#11. 접속하기버튼(687,650) 모니터링이 된다면
time.sleep(3)
pag.moveTo(687, 650)

pag.click()
#12. 클릭
#13. 1시간 후 접속종료 화면 확인하기(스캐쥴링)
#14. 확인누르고
#15. 아이디 패스워드입력
#16. 확인
#17. 7번으로 이동.


