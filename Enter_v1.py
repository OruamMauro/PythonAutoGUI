import pyautogui
import time

pyautogui.PAUSE = 10

time.sleep(10)

while True:
	pyautogui.typewrite('ABC')
	pyautogui.press('backspace')
	pyautogui.press('backspace')
	pyautogui.press('backspace')

exit()
