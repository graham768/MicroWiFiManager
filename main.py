from microwifimanager.manager import WifiManager

wlan = WifiManager().get_connection()

# if security is needed:
# wlan = WifiManager(ssid="MyAccessPoint", password="myPassword", authmode=3).get_connection()

if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")
