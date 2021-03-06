import sys


if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import TestCase, min_os_level
    import Contacts

    class TestCNPhoneNumber(TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNLabelPhoneNumberiPhone, str)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberMobile, str)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberMain, str)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberHomeFax, str)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberWorkFax, str)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberOtherFax, str)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberPager, str)
