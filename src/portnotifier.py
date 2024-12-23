"""
================================================================================
Project: Serial Port Notifier
Description: 
    A background program that notifies the user when a device is connected to 
    a COM port, allows creating/saving configurations, and supports starting 
    serial connections via PuTTY. Designed for cross-platform compatibility.

File: portnotifier.py
Author: Juliana Gentile (jlg3012@rit.edu)
Date Created: 12/22/2024
Last Modified: 12/22/2024
Version: 1.0.0

Dependencies:
    - See requirements.txt

Notes:
    - Ensure PuTTY is installed and configured in the system PATH.

================================================================================
"""

import time
import serial.tools.list_ports

from notifications import notify_device_connected
from configmanager import load_config, save_config
from serialterminal import open_serial_terminal
from plyer import notification


def get_connected_devices():
    True
    #TODO implement


def notify_device_connected():
    True
    #TODO implement


def monitor_ports():
    True
    #TODO implement

if __name__ == "__main__":
    monitor_ports