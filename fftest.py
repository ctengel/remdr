#!/usr/bin/env python3

import sys
import evdev
import pprint

print('All devices:')
for name in evdev.list_devices():
    print(name)
print()

print('This device')
dev1 = evdev.device.InputDevice(sys.argv[1])
pprint.pprint(dev1.capabilities(True, True))
