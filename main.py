"""
================================================================================
Project: Serial Port Notifier
Description: 
    A background program that notifies the user when a device is connected to 
    a COM port, allows creating/saving configurations, and supports starting 
    serial connections via PuTTY. Designed for cross-platform compatibility.

File: main.py
Description:
    Entry point to the program

Author: Juliana Gentile (jlg3012@rit.edu)
Date Created: 12/24/2024
Last Modified: 12/24/2024
Version: 1.0.0

Dependencies:
    - See requirements.txt

Notes:
    - Ensure PuTTY is installed and configured in the system PATH.

================================================================================
"""
from gui.app import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.run()
