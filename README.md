# SyncSuite

SyncSuite is a Python-based utility designed to enhance the longevity and performance of Windows-operated devices. It accomplishes this by applying critical updates and implementing power management tweaks.

## Features

- **Critical Updates**: Automates the process of applying Windows updates to ensure your system is up-to-date with the latest security patches and improvements.
- **Power Management Tweaks**: Adjusts power settings to optimize energy usage and extend device lifespan.
- **Startup Optimization**: Disables unnecessary startup programs to boost system performance.

## Requirements

- Python 3.x
- Windows operating system
- Administrative privileges to make system changes

## Installation

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/SyncSuite.git
    ```

2. Navigate to the directory.
    ```bash
    cd SyncSuite
    ```

3. Run the program.
    ```bash
    python SyncSuite.py
    ```

## Usage

- Ensure you have administrative privileges when running the script to allow it to make system changes.
- Review the log file `SyncSuite.log` to verify actions taken and troubleshoot any issues.

## Notes

- The script uses PowerShell commands to manage updates and power settings; ensure PowerShell is installed and accessible on your system.
- Modify the list of unnecessary programs in the `disable_unnecessary_startup` function to suit your specific needs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.