from PyObjCTools.TestSupport import *

import FileProvider

class TestNSFileProviderEnumerationHelper (FileProvider.NSObject):
    def finishEnumeratingChangesUpToSyncAnchor_moreComing_(self, a, b): pass
    def currentSyncAnchorWithCompletionHandler_(self, a): pass
    def didPresentEnumeratorInWindow_frontmost_(self, a, b): pass


class TestNSFileProviderEnumeration (TestCase):
    @min_os_level('10.15')
    def test_constants(self):
        self.assertIsInstance(FileProvider.NSFileProviderInitialPageSortedByDate, FileProvider.NSData)
        self.assertIsInstance(FileProvider.NSFileProviderInitialPageSortedByName, FileProvider.NSData)

    @min_sdk_level('10.15')
    def test_protocols(self):
        objc.protocolNamed('NSFileProviderEnumerationObserver')
        objc.protocolNamed('NSFileProviderChangeObserver')
        objc.protocolNamed('NSFileProviderEnumerator')

    def test_methods(self):
        self.assertArgIsBOOL(TestNSFileProviderEnumerationHelper.finishEnumeratingChangesUpToSyncAnchor_moreComing_, 1)
        self.assertArgIsBlock(TestNSFileProviderEnumerationHelper.currentSyncAnchorWithCompletionHandler_, 0, b'v')

        self.assertArgHasType(TestNSFileProviderEnumerationHelper.didPresentEnumeratorInWindow_frontmost_, 0, objc._C_UINT)
        self.assertArgHasType(TestNSFileProviderEnumerationHelper.didPresentEnumeratorInWindow_frontmost_, 1, objc._C_NSBOOL)


    @min_os_level('10.15')
    def test_methods10_15(self):
        self.assertArgIsOut(FileProvider.NSFileProviderExtension.enumeratorForContainerItemIdentifier_error_, 1)
        self.assertArgIsOut(FileProvider.NSFileProviderExtension.enumeratorForSearchQuery_error_, 1)
