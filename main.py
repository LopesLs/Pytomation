import pyautogui
from time import sleep

# Wait for 5 seconds
def wait():
  for instance in range(3):
    sleep(1)
    print(instance + 1)

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

# The result bellow will be positive alwways
ajustScreenWith = screenWidth - 1366 # Ajusting x-axis if the screez size is different.
ajustScreenHeight = screenHeight - 768 # Ajusting y-axis if the screez size is different.

# Making always positive values
ajustScreenWith = ajustScreenWith if ajustScreenWith > 0 else ajustScreenWith * -1
ajustScreenHeight = ajustScreenHeight if ajustScreenHeight > 0 else ajustScreenHeight * -1

# Start of automation
pyautogui.PAUSE = 1.5 # Pause between actions
pyautogui.press('win')
pyautogui.write('firefox', interval=0.15) # Interval between key press
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
pyautogui.write('You are good in make automations', interval=0.15)