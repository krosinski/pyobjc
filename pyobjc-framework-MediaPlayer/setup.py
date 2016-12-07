'''
Wrappers for the "MediaPlayer" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-MediaPlayer',
    version="3.2.1b1",
    description = "Wrappers for the framework MediaPlayer on Mac OS X",
    long_description=__doc__,
    packages = [ "MediaPlayer" ],
    setup_requires = [
        'pyobjc-core>=3.2.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.2.1b1',
        'pyobjc-framework-AVFoundation>=3.2.1b1',
    ],
    min_os_level="10.12",
)