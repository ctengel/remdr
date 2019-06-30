#!/usr/bin/env python3

import sys
import evdev
import pprint

dev1 = evdev.device.InputDevice(sys.argv[1])
pprint.pprint(dev1.capabilities(True, True))
