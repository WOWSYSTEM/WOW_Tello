import wowtello.wowtello
import time
import threading

wowtello.wowtello._WOW_TELLO_DEBUG_ENABLE = True

t = wowtello.wowtello.Tello('192.168.10.1')

print("접속 대기...")
while(not t.is_connected()):
	time.sleep(0.1)
print("접속 완료")

print("이륙 시작")
t.takeoff()
print("이륙 완료")
time.sleep(3)

def led1_process():
	global t
	for i in range(10):
		t.ext_led(255, 0, 0)
		time.sleep(0.5)
		t.ext_led(255, 255, 0)
		time.sleep(0.5)
		t.ext_led(0, 0, 255)
		time.sleep(0.5)

led_thread = threading.Thread(target=led1_process)
led_thread.setDaemon(True)
led_thread.start()

print("상승")
t.up(50)
time.sleep(2)
print("하강")
t.down(50)
time.sleep(2)
print("전진")
t.forward(50)
time.sleep(2)
print("후진")
t.back(50)
time.sleep(2)
print("착륙")
t.land()
