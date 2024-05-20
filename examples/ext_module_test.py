import wowtello.wowtello
import time

wowtello.wowtello._WOW_TELLO_DEBUG_ENABLE = True

t = wowtello.wowtello.Tello('192.168.10.1')

print("접속 대기...")
while(not t.is_connected()):
	time.sleep(0.1)
print("접속 완료")

print("LED 기본 테스트")
	# 외부 LED 제어 함수
	# @param r : 0-255
	# @param g : 0-255
	# @param b : 0-255
for i in range(5):
	t.ext_led(255, 0, 0)
	time.sleep(0.5)
	t.ext_led(0, 255, 0)
	time.sleep(0.5)
	t.ext_led(0, 0, 255)
	time.sleep(0.5)

print("완료")

print("LED 페이드 테스트")
	# 외부 LED Fade 제어 함수
	# 설정한 색으로 LED가 천천히 밝기가 변한다.(Fading)
	# @param f : 밝기 변화 주파수 0.1 ~ 2.5Hz의 범위로 입력 가능하다.
	# @param r : 0-255
	# @param g : 0-255
	# @param b : 0-255
t.ext_led_fade(2.5, 100, 255, 255)
time.sleep(5)
print("완료")

print("LED 색 변환 테스트")
	# 외부 LED Blink 제어 함수
	# 설정한 두 색으로 LED가 깜빡인다
	# @param f : 깜박일 주파수 0.1 ~ 10Hz의 범위로 입력 가능하다.
	# @param r1 : 0-255
	# @param g1 : 0-255
	# @param b1 : 0-255
	# @param r2 : 0-255
	# @param g2 : 0-255
	# @param b2 : 0-255
t.ext_led_blink(2.0, 255, 0, 0, 0, 0, 1000) # 1000은 자동으로 255로 변경됨
time.sleep(5)
print("완료")
t.ext_led(0, 0, 0)

print("도트매트릭스 픽셀 제어 테스트")
pixels = [
	0,0,0,1,1,1,1,0,
	0,0,0,1,1,1,1,1,
	0,0,1,3,3,0,3,0,
	0,0,1,3,3,3,3,3,
	0,0,0,1,3,3,3,0,
	0,1,1,3,2,2,2,0,
	3,0,2,2,2,2,2,3,
	0,0,3,0,0,0,3,0
]
t.ext_mled(pixels)

	# Dot-matrix Display를 제어하는 함수
	# 픽셀이 입력되며, 1차원 리스트가 들어간다.
	# 8x8 Display이므로, 64길이 이하의 리스트가 입력된다.
	# 
	# @param pixels : 길이 64 이하의 1차원 리스트
	# 데이터 순서대로 왼쪽->오른쪽, 위->아래 순서로 정렬된다.
	# 리스트에는 0~3까지의 숫자가 입력된다.
	# 0 : 꺼짐
	# 1 : Red
	# 2 : Blue
	# 3 : Purple
time.sleep(5)
print('완료')

print('test 빨간색, 왼쪽으로 흐르기 테스트')
	# Dot-matrix Display를 제어하는 함수
	# 문자열을 출력한다.
	# @param direction 문자열이 흐르는 방향
	# 0 : 왼쪽
	# 1 : 오른쪽
	# 2 : 위쪽
	# 3 : 아래쪽
	# @param color 문자열 색상
	# 0 : Red
	# 1 : Blue
	# 2 : Purple
	# @param f 문자열 흐르는 속도(frame rate / 0.1~2.5Hz)
	# @param string 출력할 문자열 길이. 70자 제한이다.
t.ext_mled_display_string(0, 0, 1.0, 'test')
time.sleep(5)

print('AbCd 파란색, 오른쪽으로 흐르기 테스트')
t.ext_mled_display_string(1, 1, 1.0, 'AbCd')
time.sleep(5)

print('wowsysten 보라색, 위로 흐르기 테스트')
t.ext_mled_display_string(2, 2, 1.0, 'wowsystem')
time.sleep(5)

print('i love you nobu! 빨간색, 아래로 흐르기 테스트, 속도 더 빠르게')

t.ext_mled_display_string(3, 0, 2.5, 'i love you nobu!')
time.sleep(10)

print('완료')

for i in range(4):
	print(f'그림 {i}쪽으로 흐르기')
	t.ext_mled_image(i, 0.5*i, pixels)
	time.sleep(3)
print('완료')

print('아스키 출력 테스트')
t.ext_mled_static_ascii(0, 'W')
time.sleep(2.5)
print('완료')

print('프리셋 출력 테스트')
t.ext_mled_static_ascii(0, 'heart')
time.sleep(2.5)
print('완료')

print('TOF센서 읽기', t.ext_get_tof())
print('버전 정보 읽기', t.ext_get_version())

print('All test complete')