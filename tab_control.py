import pyautogui
# import os

# os.environ['DISPLAY'] = ':0'
pyautogui.PAUSE = .1


# pyautogui.moveTo(300, 450, duration=2)



# #press multiple keys similar to what write() does
# #switch left
pyautogui.press(['cmd', 'shift', 'tab'])

print("Switch tab Left")

# #switch right
# pyautogui.press(['cmd', 'tab'])

# print("Switch tab Right")


# #holding down then release
# #switch left
# pyautogui.keyDown('ctrl') 	#hold down ctrl
# pyautogui.keyDown('shift')	#hold down shift
# pyautogui.press('tab')		#press tab
# pyautogui.keyUp('ctrl')		#release ctrl
# pyautogui.keyUp('shift')	#release shift

# print("Switch tab Left")

# #switch right
# pyautogui.keyDown('ctrl')	#hold down ctrl
# pyautogui.press('tab')		#press tab
# pyautogui.keyUp('ctrl')		#release ctrl

# print("Switch tab Right")