# MicroPython WiFi Manager

A MicroPython WiFi manager for ESPx devices with fallback web configuration portal

Based on tayfunulu's [WifiManager](https://github.com/tayfunulu/WiFiManager), but incorporates jczic's [MicroDNSSrv](https://github.com/jczic/MicroDNSSrv) to create a captive portal by default so users don't have to find the access point's IP Address. The goal is to act similarly to tzapu's  popular C++ [WifiManager](https://github.com/tzapu/WiFiManager) while taking advantage of the simplicity of python for development.

# Installation

## Installation with upip

> ⚠ Note: if you are using this package with OTA updates, be sure to avoid overwriting `lib/` where upip installs packages.

From micropython command line run
```
import upip
upip.install("micro-wifi-manager")
```

## Manual Installation

Copy the `microwifimanager/` directory to your device and refer to `main.py` for usage
# Main Features

- Easily setup device's WiFi connection from phone or computer
- Web based connection manager with captive portal
- Save wifi password in `wifi.dat` (csv format)

# Usage

See `main.py` for an example

```python
from microwifimanager.manager import WifiManager

wlan = WifiManager().get_connection()
```

The `WifiManager` lets you setup your wifi access point's name and password as well as the authentication modes
```
# authmodes: 0=open, 1=WEP, 2=WPA-PSK, 3=WPA2-PSK, 4=WPA/WPA2-PSK
WifiManager(ssid='WifiManager', password='', authmode=0)
```

# Logic

1. Check `wifi.dat` file and try saved networks/passwords
2. Host WiFi access point and web server, and redirect all traffic to web server (captive portal)
3. User can then provide the network password which is saved to `wifi.dat`
4. Run user code

![flowchart](/docs/flowchart.png)