import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import WiFi

    class TestWFConnectionStatus (TestCase):
        @min_os_level('10.15')
        def test_classes(self):
            WiFi.WFConnectionStatus
