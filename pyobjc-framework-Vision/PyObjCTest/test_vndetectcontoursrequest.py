from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectContoursRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectContourRequestRevision1, 1)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(Vision.VNDetectContoursRequest.detectDarkOnLight)
        self.assertResultIsBOOL(Vision.VNDetectContoursRequest.setDetectDarkOnLight_)
