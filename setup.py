from setuptools import setup

with open("README.md", "r",  encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='micro-wifi-manager',
    version='0.0.2',
    description="A MicroPython WiFi manager for ESPx devices with fallback web configuration portal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/graham768/MicroWiFiManager',
    license="MIT",
    packages=['microwifimanager']
)