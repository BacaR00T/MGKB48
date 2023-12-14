# MGKB48
~Wireless ergo keeb <br>
~Left and right part connects to the main powerboard with nice!nano (or any another pro micro pinout MCU). This main board also includes IP5306 charging circuit to be able to use Li-Po 18650 batteries.

![mgkb48](https://github.com/BacaR00T/MGKB48/assets/81833517/83df6a31-fb3e-429e-8804-57d09a7955eb)


# MCU file configuration
To be able to use the nice!nano (or any other MCU with nRF52840) and KMK, it's needed to flash the MCU with [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) and then compile the [kmk library](https://kmkfw.io/docs/Getting_Started) and the [adafruit_ble](https://github.com/adafruit/Adafruit_CircuitPython_BLE/tree/main/adafruit_ble) (for BLE connectivity) library since usable flash is only ~256kb. How to you can find [here](https://kmkfw.io/docs/Officially_Supported_Microcontrollers). But don't worry the compiled files are in Code/CIRCUITPY directory so just upload them to the MCU.


