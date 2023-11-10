import pyautogui

def start_automation(adjustmentX : int, adjustmentY : int) -> None:
  """
  This function will start the automation.

  Parameters:
  None

  Returns:
  None

  """
  pyautogui.PAUSE = 1.5 # Pause between actions
  pyautogui.press('win')
  pyautogui.write('firefox', interval=0.15) # Interval between key press
  pyautogui.press('enter')
  pyautogui.hotkey('ctrl', 't')
  pyautogui.write('google.com', interval=0.15)
  pyautogui.press('enter')
  pyautogui.moveTo(1292 + adjustmentX, 740 + adjustmentY)
  pyautogui.click()