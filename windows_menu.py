from pywinauto import mouse
from datetime import datetime
import time
import win32api


print(win32api.GetCursorPos())

new_x = 30
new_y = 1065

print("- - - - - - - - - -\n- - - - - - - - - -")

while True:
	mouse.click(button='left', coords=(new_x,new_y))
	print("Presiona CTRL+C para terminar el programa {0}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")),end='\r')
	time.sleep(10)
exit()