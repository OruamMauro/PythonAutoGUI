import pyautogui

pyautogui.PAUSE = 2.5

pyautogui.press('winleft')
pyautogui.typewrite('skype\n')
pyautogui.typewrite('Mauro Delgadillo')
pyautogui.press('enter')
pyautogui.typewrite('Test: Mensaje automático\n')
