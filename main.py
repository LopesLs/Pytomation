import pyautogui
from automation import start_automation
screenWidth, screenHeight = pyautogui.size()

# The result bellow will be positive alwways
ajustScreenWith = screenWidth - 1366 # Ajusting x-axis if the screez size is different.
ajustScreenHeight = screenHeight - 768 # Ajusting y-axis if the screez size is different.

# Start of automation
start_automation(ajustScreenWith, ajustScreenHeight)