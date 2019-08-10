from PyObjCTools.TestSupport import *

import CoreServices


class TestFinder(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("kClippingCreator")
        self.assert_not_wrapped("kClippingPictureType")
        self.assert_not_wrapped("kClippingTextType")
        self.assert_not_wrapped("kClippingSoundType")
        self.assert_not_wrapped("kClippingUnknownType")
        self.assert_not_wrapped("kInternetLocationCreator")
        self.assert_not_wrapped("kInternetLocationHTTP")
        self.assert_not_wrapped("kInternetLocationFTP")
        self.assert_not_wrapped("kInternetLocationFile")
        self.assert_not_wrapped("kInternetLocationMail")
        self.assert_not_wrapped("kInternetLocationNNTP")
        self.assert_not_wrapped("kInternetLocationAFP")
        self.assert_not_wrapped("kInternetLocationAppleTalk")
        self.assert_not_wrapped("kInternetLocationNSL")
        self.assert_not_wrapped("kInternetLocationGeneric")
        self.assert_not_wrapped("kCustomIconResource")
        self.assert_not_wrapped("kCustomBadgeResourceType")
        self.assert_not_wrapped("kCustomBadgeResourceID")
        self.assert_not_wrapped("kCustomBadgeResourceVersion")
        self.assert_not_wrapped("CustomBadgeResource")
        self.assert_not_wrapped("kRoutingResourceType")
        self.assert_not_wrapped("kRoutingResourceID")
        self.assert_not_wrapped("RoutingResourceEntry")
        self.assert_not_wrapped("kContainerFolderAliasType")
        self.assert_not_wrapped("kContainerTrashAliasType")
        self.assert_not_wrapped("kContainerHardDiskAliasType")
        self.assert_not_wrapped("kContainerFloppyAliasType")
        self.assert_not_wrapped("kContainerServerAliasType")
        self.assert_not_wrapped("kApplicationAliasType")
        self.assert_not_wrapped("kContainerAliasType")
        self.assert_not_wrapped("kDesktopPrinterAliasType")
        self.assert_not_wrapped("kContainerCDROMAliasType")
        self.assert_not_wrapped("kApplicationCPAliasType")
        self.assert_not_wrapped("kApplicationDAAliasType")
        self.assert_not_wrapped("kPackageAliasType")
        self.assert_not_wrapped("kAppPackageAliasType")
        self.assert_not_wrapped("kSystemFolderAliasType")
        self.assert_not_wrapped("kAppleMenuFolderAliasType")
        self.assert_not_wrapped("kStartupFolderAliasType")
        self.assert_not_wrapped("kPrintMonitorDocsFolderAliasType")
        self.assert_not_wrapped("kPreferencesFolderAliasType")
        self.assert_not_wrapped("kControlPanelFolderAliasType")
        self.assert_not_wrapped("kExtensionFolderAliasType")
        self.assert_not_wrapped("kExportedFolderAliasType")
        self.assert_not_wrapped("kDropFolderAliasType")
        self.assert_not_wrapped("kSharedFolderAliasType")
        self.assert_not_wrapped("kMountedFolderAliasType")
        self.assert_not_wrapped("kIsOnDesk")
        self.assert_not_wrapped("kColor")
        self.assert_not_wrapped("kIsShared")
        self.assert_not_wrapped("kHasNoINITs")
        self.assert_not_wrapped("kHasBeenInited")
        self.assert_not_wrapped("kHasCustomIcon")
        self.assert_not_wrapped("kIsStationery")
        self.assert_not_wrapped("kNameLocked")
        self.assert_not_wrapped("kHasBundle")
        self.assert_not_wrapped("kIsInvisible")
        self.assert_not_wrapped("kIsAlias")
        self.assert_not_wrapped("fOnDesk")
        self.assert_not_wrapped("fHasBundle")
        self.assert_not_wrapped("fInvisible")
        self.assert_not_wrapped("fTrash")
        self.assert_not_wrapped("fDesktop")
        self.assert_not_wrapped("fDisk")
        self.assert_not_wrapped("kIsStationary")
        self.assert_not_wrapped("kExtendedFlagsAreInvalid")
        self.assert_not_wrapped("kExtendedFlagHasCustomBadge")
        self.assert_not_wrapped("kExtendedFlagObjectIsBusy")
        self.assert_not_wrapped("kExtendedFlagHasRoutingInfo")
        self.assert_not_wrapped("kFirstMagicBusyFiletype")
        self.assert_not_wrapped("kLastMagicBusyFiletype")
        self.assert_not_wrapped("kMagicBusyCreationDate")
        self.assert_not_wrapped("FileInfo")
        self.assert_not_wrapped("FolderInfo")
        self.assert_not_wrapped("ExtendedFileInfo")
        self.assert_not_wrapped("ExtendedFolderInfo")
        self.assert_not_wrapped("FInfo")
        self.assert_not_wrapped("FXInfo")
        self.assert_not_wrapped("DInfo")
        self.assert_not_wrapped("DXInfo")


if __name__ == "__main__":
    main()
