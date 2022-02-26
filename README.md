# WiFi Manager

Lang   : Micropython 
Tested : 1.8 and 1.9.3

WiFi manager for ESP8266 - ESP12 - ESP32 written in micropython 

Based on [tayfunulu's WifiManager](https://github.com/tayfunulu/WiFiManager), but incorporates [jczic's MicroDNSSrv](https://github.com/jczic/MicroDNSSrv) to create a captive portal by default so users don't have to know the access point's IP Address.

# Main Features

- Web based connection manager with captive portal
- Save wifi password in `wifi.dat` (csv format)
- Easy to apply 

# Usage

Upload `wifimgr.py` and `main.py` to board and write code at the end of `main.py`

# Logic

1. Check `wifi.dat` file and try saved networks/passwords
2. Host Access Point and redirect all traffic to website (captive portal)
3. User can then provide the network password which is saved to `wifi.dat`
4. Run user code