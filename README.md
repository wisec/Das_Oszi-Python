# Creating a Virtual env

```
python3 -m 'venv' venv
. venv/bin/activate
pip install -r requirements.txt
```


# DSO5XXXX-Python
 Access to the Hantek DSO5XXXXP oscilloscope from Python 3.x

See this sites for details:
* https://elinux.org/Das_Oszi_Protocol
* https://randomprojects.org/wiki/Voltcraft_DSO-3062C

My Hantek DSO5102P reports VID:PID as 049f:505a so I added the file ``99-dso5102P.rules`` to ``/lib/udev/rules.d/`` (or to ``/etc/udev/rules.d/``)

    SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="049f", ATTR{idProduct}=="505a", MODE="0666"

and reload udev rules with

    $ sudo udevadm control --reload-rules
    $ sudo udevadm trigger

