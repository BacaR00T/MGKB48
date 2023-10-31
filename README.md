# MGKB48
~Wireless ergo keeb <br>
~Left and right part connects to the main powerboard with nice!_nano (or any another pro micro pinout MCU). This main board also includes IP5306 charging circuit to be able to use Li-Po 18650 batteries.

![mgkb48](https://github.com/BacaR00T/MGKB48/assets/81833517/43564939-5fd0-44ae-843e-08f6653fc776)


# MCU file configuration
To be able to use the nice!nano (or any other MCU with nRF52840) and KMK, it's needed to flash the MCU with [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) and then compile the [kmk library](https://kmkfw.io/docs/Getting_Started) and the [adafruit_ble](https://github.com/adafruit/Adafruit_CircuitPython_BLE/tree/main/adafruit_ble) (for BLE connectivity) library since usable flash is only ~256kb. How to you can find [here](https://kmkfw.io/docs/Officially_Supported_Microcontrollers). But don't worry the compiled files are in code/CIRCUITPY so just upload them to the MCU.



# PCB
![Screenshot from 2023-10-07 15-43-36](https://github.com/BacaR00T/MGKB48/assets/81833517/d8f7f681-150d-416c-a624-c4bb8dc74a29)
![Screenshot from 2023-10-07 15-44-19](https://github.com/BacaR00T/MGKB48/assets/81833517/eddfc508-3062-4606-a9ec-e8fb9a15d32b)
