import pyautogui


class PrinterSettingsAutomation:
    """This class contains the functions to automate the printer."""

    def __init__(
        self,
        printer_name: str,
        label_width: str,
        label_height: str,
        right_margin: str,
        top_margin: str,
        write_interval: float = 0.08,
        press_interval: float = 0.5,
        printer_location: int = 1,
    ):
        self.printer_name = printer_name
        self.width = label_width
        self.height = label_height
        self.right = right_margin
        self.top = top_margin
        self.write_interval = write_interval
        self.press_interval = press_interval
        self.printer_location = printer_location

    def display_alert_message(self, title: str, text: str, button_value: str) -> str:
        """This function show the alerts.

        Args:
            title (str): title of alert
            text (str): text of alert
            button_value (str): value of button

        Returns:
            str: log message
        """

        pyautogui.alert(title=title, text=text, button=button_value)

        return "Alerts showed"

    def get_user_input(self, title: str, text: str, default: str) -> str:
        """This function show the prompts.

        Args:
            title (str): title of prompt
            text (str): text of prompt
            default (str): default value of prompt

        Returns:
            str: input value
        """

        return pyautogui.prompt(title=title, text=text, default=default)

    def open_devices_and_printers_window(self) -> str:
        """This function open the dispositives and printers window.

        Returns:
            str: log message
        """

        pyautogui.hotkey("win", "e")
        pyautogui.press("tab", presses=3, interval=0.5)
        pyautogui.hotkey("ctrl", "space")
        pyautogui.write(
            "Painel de Controle\Hardware e Sons\Dispositivos e Impressoras",
            interval=self.write_interval,
        )
        pyautogui.press("enter")

        return "Dispositives and printers window opened"

    def find_printer(self, printer_name: str) -> str:
        """This function find the printer and acess the preferences.

        Args:
            printer_name (str): name of printer that will be changed

        Returns:
            str: log message
        """

        pyautogui.press("tab", presses=3, interval=self.press_interval)
        pyautogui.write(printer_name, interval=self.write_interval)
        pyautogui.press("tab", presses=2, interval=self.press_interval)
        pyautogui.press("space")
        pyautogui.press("alt")
        pyautogui.hotkey("alt", "a")
        pyautogui.press("down", presses=2, interval=self.press_interval)
        pyautogui.press("enter")

        if self.printer_location != 1:
            pyautogui.press("down", presses=(self.printer_location - 1))
            pyautogui.press("enter")

        return f"found printer: {printer_name}"

    def update_printer_preferences(self) -> str:
        """This function change the preferences of the printer.

        Returns:
            str: log message
        """

        pyautogui.press("tab")
        pyautogui.press("5")
        pyautogui.press("tab", presses=6, interval=self.press_interval)
        pyautogui.write(self.width, interval=self.write_interval)
        pyautogui.press("tab")
        pyautogui.write(self.height, interval=self.write_interval)
        pyautogui.press("tab", presses=2, interval=self.press_interval)
        pyautogui.write(self.right, interval=self.write_interval)
        pyautogui.press("tab")
        pyautogui.write(self.top, interval=self.write_interval)

        return "Preferences changed"

    def update_media_settings(self) -> str:
        """This function change thermal transfer to direct thermal.

        Returns:
            str: log message
        """

        pyautogui.press("tab", presses=6, interval=self.press_interval)
        pyautogui.press("right")
        pyautogui.press("tab")
        pyautogui.press("right")
        pyautogui.hotkey("alt", "l")

        return "Media settings changed"
