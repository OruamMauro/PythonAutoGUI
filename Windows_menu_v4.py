import pyautogui
import time

pyautogui.press('winleft')
x1 = 0
y1 = 0
print("Presiona Ctrl+C para cerrar!!!\n")
while True:
	time.sleep(10)
	x2, y2 = pyautogui.position()
	if x1 == x2 and y1 == y2:
		pyautogui.press('winleft')
		t = time.localtime()
		print("Ya te fuiste y me dejaste..", end='\r')
	else:
		print("Estás quesque trabajando...", end='\r')
	x1, y1 = pyautogui.position()

exit()
