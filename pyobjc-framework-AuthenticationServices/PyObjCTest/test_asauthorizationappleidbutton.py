from PyObjCTools.TestSupport import *

import AuthenticationServices

class TestASAuthorizationAppleIDButton (TestCase):
    def test_constants(self):
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonTypeSignIn, 0)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonTypeContinue, 1)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonTypeDefault = AuthenticationServices.ASAuthorizationAppleIDButtonTypeSignIn)

        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonStyleWhite, 0)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonStyleWhiteOutline, 1)
        self.assertEqual(AuthenticationServices.ASAuthorizationAppleIDButtonStyleBlack, 2)