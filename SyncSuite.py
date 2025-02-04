import os
import ctypes
import subprocess
import winreg
import logging

# Setup logging
logging.basicConfig(filename='SyncSuite.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('SyncSuite started.')

def apply_updates():
    """
    Apply critical updates using Windows Update.
    """
    try:
        logging.info('Applying Windows updates.')
        subprocess.check_call(['powershell.exe', '-Command', 'Install-WindowsUpdate -AcceptAll -AutoReboot'])
        logging.info('Windows updates applied successfully.')
    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to apply updates: {e}')

def set_power_management():
    """
    Set power management tweaks for better longevity.
    """
    try:
        logging.info('Applying power management settings.')

        # Set power plan to "Balanced"
        subprocess.check_call(['powercfg', '/setactive', '381b4222-f694-41f0-9685-ff5bb260df2e'])
        logging.info('Power plan set to Balanced.')

        # Set sleep and display settings
        subprocess.check_call(['powercfg', '/change', 'standby-timeout-ac', '30'])
        subprocess.check_call(['powercfg', '/change', 'standby-timeout-dc', '15'])
        subprocess.check_call(['powercfg', '/change', 'monitor-timeout-ac', '10'])
        subprocess.check_call(['powercfg', '/change', 'monitor-timeout-dc', '5'])
        logging.info('Sleep and display settings adjusted.')

        # Enable hibernation
        subprocess.check_call(['powercfg', '/hibernate', 'on'])
        logging.info('Hibernation enabled.')

    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to apply power management settings: {e}')

def disable_unnecessary_startup():
    """
    Disable unnecessary startup programs to enhance performance.
    """
    try:
        logging.info('Disabling unnecessary startup programs.')

        # Example registry path for startup programs
        startup_reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, startup_reg_path, 0, winreg.KEY_WRITE) as key:
            # List of unnecessary programs to disable
            unnecessary_programs = ['SomeProgram', 'AnotherProgram']

            for program in unnecessary_programs:
                try:
                    winreg.DeleteValue(key, program)
                    logging.info(f'Disabled startup program: {program}')
                except FileNotFoundError:
                    logging.warning(f'Startup program not found: {program}')

    except Exception as e:
        logging.error(f'Failed to disable unnecessary startup programs: {e}')

def main():
    """
    Main function to run SyncSuite tasks.
    """
    apply_updates()
    set_power_management()
    disable_unnecessary_startup()
    logging.info('SyncSuite completed.')

if __name__ == "__main__":
    main()