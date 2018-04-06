# CAN_msg_emulator

## Communicating via SocketCAN

To communicate between a motor controller node and a PC (laptop etc.) the SocketCAN Interface is needed.
For development, the [USBtin- USB to CAN interface board][USBtin] was used.

SocketCAN for Linux was installed using the following commands.

Firstly, the kernel modules are installed;

    $ sudo modprobe can
    $ sudo modprobe can-raw
    $ sudo modprobe slcan

Next, the CAN utils can be obtained and compiled;

    $ git clone https://github.com/linux-can/can-utils.git
    $ cd can-utils
    $ make 
    $ make install [?]

In order to use the interface correctly, firstly the device address needs to be determined.
This can be found using the following command once the device has been plugged in (where tty/ACM0 is the target device)

    $ tail /var/log/kern.log
    kernel: [ ] usb 1-4.2.3: new full-speed USB device number 8 using ehci-pci
    kernel: [ ] usb 1-4.2.3: New USB device found, idVendor=04d8, idProduct=000a
    kernel: [ ] usb 1-4.2.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    kernel: [ ] usb 1-4.2.3: Product: USBtin
    kernel: [ ] cdc_acm 1-4.2.3:1.0: This device cannot do calls on its own. It is not a modem.
    kernel: [ ] cdc_acm 1-4.2.3:1.0: ttyACM0: USB ACM device
    kernel: [ ] usbcore: registered new interface driver cdc_acm
    kernel: [ ] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters

With the device address determined, the SocketCAN interface can be attached and started.
Note that the "-s<x>" flag should default to "-s8" for the typical baudrate of 1MBaud.


    $ sudo ./slcan_attach -f -s<x> -o /dev/ttyACM0
    attached tty /dev/ttyACM0 to netdevice slcan0
    $ sudo ./slcand ttyACM0 slcan0
    $ sudo ifconfig slcan0 up

### Using Command Line to communicate via CAN

It is possible to send CAN Frames directly from the Command Line and is useful to check that the system is initialised as expected. 
To transmit a CAN Frame, the following command is used, where in this example, the interface has already been constructed as "slcan0", 
the identifier has been set to "0x0AB" and the data is fixed at 8 data bytes. NOTE "#" identifies the seperation between identifier and 
data, and the "." operator between data bytes is optional

    $ cansend slcan0 0ab#01.02.03.04.05.06.07.08


[USBtin]: [http://www.fischl.de/usbtin/]# CAN_msg_emulator
