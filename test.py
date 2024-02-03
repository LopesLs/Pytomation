import pyautogui

pyautogui.PAUSE = 0.8
pyautogui.hotkey("win", "e")
pyautogui.press("tab", presses=3, interval=0.5)
pyautogui.hotkey("ctrl", "space")
pyautogui.write("Painel de Controle\Hardware e Sons\Dispositivos e Impressoras", interval=0.05)
pyautogui.press("enter")