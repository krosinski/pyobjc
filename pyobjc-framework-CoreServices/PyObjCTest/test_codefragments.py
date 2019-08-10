from PyObjCTools.TestSupport import *

import CoreServices


class TestAliases(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("kCFragResourceType")
        self.assert_not_wrapped("kCFragResourceID")
        self.assert_not_wrapped("kCFragLibraryFileType")
        self.assert_not_wrapped("kCFragAllFileTypes")
        self.assert_not_wrapped("kPowerPCCFragArch")
        self.assert_not_wrapped("kMotorola68KCFragArch")
        self.assert_not_wrapped("kAnyCFragArch")
        self.assert_not_wrapped("kCompiledCFragArch")
        self.assert_not_wrapped("kCompiledCFragArch")
        self.assert_not_wrapped("kNullCFragVersion")
        self.assert_not_wrapped("kImportLibraryCFrag")
        self.assert_not_wrapped("kApplicationCFrag")
        self.assert_not_wrapped("kDropInAdditionCFrag")
        self.assert_not_wrapped("kStubLibraryCFrag")
        self.assert_not_wrapped("kWeakStubLibraryCFrag")
        self.assert_not_wrapped("kIsCompleteCFrag")
        self.assert_not_wrapped("kFirstCFragUpdate")
        self.assert_not_wrapped("kCFragGoesToEOF")
        self.assert_not_wrapped("kMemoryCFragLocator")
        self.assert_not_wrapped("kDataForkCFragLocator")
        self.assert_not_wrapped("kResourceCFragLocator")
        self.assert_not_wrapped("kNamedFragmentCFragLocator")
        self.assert_not_wrapped("kCFBundleCFragLocator")
        self.assert_not_wrapped("kCFBundlePreCFragLocator")
        self.assert_not_wrapped("CFragUsage1Union")
        self.assert_not_wrapped("CFragUsage2Union")
        self.assert_not_wrapped("kCFragLibUsageMapPrivatelyMask")
        self.assert_not_wrapped("CFragWhere1Union")
        self.assert_not_wrapped("CFragWhere2Union")
        self.assert_not_wrapped("kDefaultCFragNameLen")
        self.assert_not_wrapped("CFragResourceMember")
        self.assert_not_wrapped("CFragResourceExtensionHeader")
        self.assert_not_wrapped("CFragResourceSearchExtension")
        self.assert_not_wrapped("kCFragResourceSearchExtensionKind")
        self.assert_not_wrapped("CFragResource")
        self.assert_not_wrapped("kCurrCFragResourceVersion")
        self.assert_not_wrapped("AlignToFour")
        self.assert_not_wrapped("CFMOffsetOf")
        self.assert_not_wrapped("kBaseCFragResourceMemberSize")
        self.assert_not_wrapped("kBaseCFragResourceSize")
        self.assert_not_wrapped("NextCFragResourceMemberPtr")
        self.assert_not_wrapped("FirstCFragResourceExtensionPtr")
        self.assert_not_wrapped("NextCFragResourceExtensionPtr")
        self.assert_not_wrapped("FirstCFragResourceSearchQualifier")
        self.assert_not_wrapped("NextCFragResourceSearchQualifier")
        self.assert_not_wrapped("kReferenceCFrag")
        self.assert_not_wrapped("kFindCFrag")
        self.assert_not_wrapped("kPrivateCFragCopy")
        self.assert_not_wrapped("kUnresolvedCFragSymbolAddress")
        self.assert_not_wrapped("kCodeCFragSymbol")
        self.assert_not_wrapped("kDataCFragSymbol")
        self.assert_not_wrapped("kTVectorCFragSymbol")
        self.assert_not_wrapped("kTOCCFragSymbol")
        self.assert_not_wrapped("kGlueCFragSymbol")
        self.assert_not_wrapped("CFragHasFileLocation")
        self.assert_not_wrapped("GetSharedLibrary")
        self.assert_not_wrapped("GetDiskFragment")
        self.assert_not_wrapped("GetMemFragment")
        self.assert_not_wrapped("CloseConnection")
        self.assert_not_wrapped("FindSymbol")
        self.assert_not_wrapped("CountSymbols")
        self.assert_not_wrapped("GetIndSymbol")
        self.assert_not_wrapped("CFragSystem7MemoryLocator")
        self.assert_not_wrapped("CFragSystem7DiskFlatLocator")
        self.assert_not_wrapped("CFragSystem7SegmentedLocator")
        self.assert_not_wrapped("CFragCFBundleLocator")
        self.assert_not_wrapped("CFragSystem7Locator")
        self.assert_not_wrapped("CFragSystem7InitBlock")
        self.assert_not_wrapped("CFragInitBlock")
        self.assert_not_wrapped("ConvertBundlePreLocator")
        self.assert_not_wrapped("kPowerPCArch")
        self.assert_not_wrapped("kMotorola68KArch")
        self.assert_not_wrapped("kAnyArchType")
        self.assert_not_wrapped("kNoLibName")
        self.assert_not_wrapped("kNoConnectionID")
        self.assert_not_wrapped("kLoadLib")
        self.assert_not_wrapped("kFindLib")
        self.assert_not_wrapped("kNewCFragCopy")
        self.assert_not_wrapped("kLoadNewCopy")
        self.assert_not_wrapped("kUseInPlace")
        self.assert_not_wrapped("kCodeSym")
        self.assert_not_wrapped("kDataSym")
        self.assert_not_wrapped("kTVectSym")
        self.assert_not_wrapped("kTOCSym")
        self.assert_not_wrapped("kGlueSym")
        self.assert_not_wrapped("kInMem")
        self.assert_not_wrapped("kOnDiskFlat")
        self.assert_not_wrapped("kOnDiskSegmented")
        self.assert_not_wrapped("kIsLib")
        self.assert_not_wrapped("kIsApp")
        self.assert_not_wrapped("kIsDropIn")
        self.assert_not_wrapped("kFullLib")
        self.assert_not_wrapped("kUpdateLib")
        self.assert_not_wrapped("kWholeFork")
        self.assert_not_wrapped("kCFMRsrcType")
        self.assert_not_wrapped("kCFMRsrcID")
        self.assert_not_wrapped("kSHLBFileType")
        self.assert_not_wrapped("kUnresolvedSymbolAddress")
        self.assert_not_wrapped("kPowerPC")
        self.assert_not_wrapped("kMotorola68K")


if __name__ == "__main__":
    main()
