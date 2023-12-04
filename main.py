import pyautogui
from automation import start_automation

# Get the current screen size
current_screen_width, current_screen_height = pyautogui.size()

# Define the screen size used during development
DEVELOPMENT_SCREEN_SIZE = (1366, 768)

# Calculate the adjustment needed for different screen sizes
adjust_screen_width = current_screen_width - DEVELOPMENT_SCREEN_SIZE[0]
adjust_screen_height = current_screen_height - DEVELOPMENT_SCREEN_SIZE[1]

# Start the automation, passing in the necessary adjustments
start_automation(adjust_screen_width, adjust_screen_height)