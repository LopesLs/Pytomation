from printer_automation import PrinterSettingsAutomation
import pyautogui


def run_printer_automation():
    """This function is the main function of the script.
    """

    printer_automation = PrinterSettingsAutomation(
        printer_name="Recipiente",
        label_width="5,70",
        label_height="4,30",
        right_margin="0,80",
        top_margin="0,60",
    )

    # Alert important information
    print(printer_automation.display_alert_message(title="Alerta", text="Enquanto o script estiver em execução por favor não toque no teclado ou mouse, certifique-se que o painel de controle esteja fechado!", button_value="OK"))

    # Inputs
    script_speed = printer_automation.get_user_input(title="Prompt 1/4", text="Por favor, informe a velocidade do script", default="0.8")
    write_interval = printer_automation.get_user_input(title="Prompt 2/4", text="Por favor, informe o intervalo de escrita", default="0.08")
    press_interval = printer_automation.get_user_input(title="Prompt 3/4", text="Por favor, informe o intervalo de pressionamento", default="0.5")
    printer_location = printer_automation.get_user_input(title="Prompt 4/4", text="Por favor, informe a localização da impressora", default="1")

    # Set values
    pyautogui.PAUSE = float(script_speed)
    printer_automation.write_interval = float(write_interval)
    printer_automation.press_interval = float(press_interval)
    printer_automation.printer_location = int(printer_location)

    # Execute functions
    print(printer_automation.open_devices_and_printers_window())
    print(printer_automation.find_printer(printer_name="Recipiente"))
    print(printer_automation.update_printer_preferences())
    print(printer_automation.update_media_settings())
    print(printer_automation.display_alert_message(title="Alerta", text="Script finalizado! Verifique se realmente está como Direct Thermal", button_value="OK"))

if __name__ == "__main__":
    run_printer_automation()
