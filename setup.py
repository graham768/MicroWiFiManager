from setuptools import setup
import sdist_upip

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='micro-wifi-manager',
    version='0.0.1',
    description="A MicroPython WiFi manager for ESPx devices with fallback web configuration portal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/graham768/MicroWiFiManager',
    license="MIT",
    cmdclass={'sdist': sdist_upip.sdist},
    packages=['microwifimanager']
)