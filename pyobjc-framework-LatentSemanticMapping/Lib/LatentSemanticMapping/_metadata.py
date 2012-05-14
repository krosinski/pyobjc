# This file is generated by objective.metadata
#
# Last update: Thu Mar  8 09:35:37 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$$'''
enums = '''$kLSMClusterAgglomerative@4$kLSMClusterCategories@0$kLSMClusterKMeans@0$kLSMClusterTokens@2$kLSMClusterWords@1$kLSMMapBadCluster@-6644$kLSMMapBadPath@-6643$kLSMMapDiscardCounts@1$kLSMMapHashText@256$kLSMMapLoadMutable@2$kLSMMapNoSuchCategory@-6641$kLSMMapOutOfState@-6640$kLSMMapOverflow@-6645$kLSMMapPairs@1$kLSMMapTriplets@2$kLSMMapWriteError@-6642$kLSMResultBestWords@1$kLSMTextApplySpamHeuristics@4$kLSMTextPreserveAcronyms@2$kLSMTextPreserveCase@1$'''
misc.update({'kLSMAlgorithmDense': 'LSMAlgorithmDense', 'kLSMPrecisionFloat': 'LSMPrecisionFloat', 'kLSMSweepCutoffKey': 'LSMSweepCutoff', 'kLSMAlgorithmSparse': 'LSMAlgorithmSparse', 'kLSMDimensionKey': 'LSMDimension', 'kLSMAlgorithmKey': 'LSMAlgorithm', 'kLSMPrecisionKey': 'LSMPrecision', 'kLSMPrecisionDouble': 'LSMPrecisionDouble', 'kLSMSweepAgeKey': 'LSMSweepAge', 'kLSMIterationsKey': 'LSMIterations'})
functions={'LSMMapGetCategoryCount': (b'l^{__LSMMap=}',), 'LSMMapAddTextWithWeight': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}If', b'i^{__LSMMap=}^{__LSMText=}If'),), 'LSMTextAddToken': (sel32or64(b'l^{__LSMText=}^{__CFData=}', b'i^{__LSMText=}^{__CFData=}'),), 'LSMMapSetStopWords': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}', b'i^{__LSMMap=}^{__LSMText=}'),), 'LSMTextGetTypeID': (b'L',), 'LSMMapStartTraining': (sel32or64(b'l^{__LSMMap=}', b'i^{__LSMMap=}'),), 'LSMMapCompile': (sel32or64(b'l^{__LSMMap=}', b'i^{__LSMMap=}'),), 'LSMMapWriteToStream': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}L', b'i^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}L'),), 'LSMResultCopyWordCluster': (b'^{__CFArray=}^{__LSMResult=}l', '', {'retval': {'already_cfretained': True}}), 'LSMResultGetCount': (b'l^{__LSMResult=}',), 'LSMResultGetCategory': (b'I^{__LSMResult=}l',), 'LSMMapGetTypeID': (b'L',), 'LSMResultGetTypeID': (b'L',), 'LSMResultCreate': (b'^{__LSMResult=}^{__CFAllocator=}^{__LSMMap=}^{__LSMText=}lL', '', {'retval': {'already_cfretained': True}}), 'LSMResultCopyWord': (b'^{__CFString=}^{__LSMResult=}l', '', {'retval': {'already_cfretained': True}}), 'LSMMapCreateClusters': (b'^{__CFArray=}^{__CFAllocator=}^{__LSMMap=}^{__CFArray=}lL', '', {'retval': {'already_cfretained': True}}), 'LSMMapApplyClusters': (sel32or64(b'l^{__LSMMap=}^{__CFArray=}', b'i^{__LSMMap=}^{__CFArray=}'),), 'LSMTextAddWords': (sel32or64(b'l^{__LSMText=}^{__CFString=}^{__CFLocale=}L', b'i^{__LSMText=}^{__CFString=}^{__CFLocale=}L'),), 'LSMResultCopyTokenCluster': (b'^{__CFArray=}^{__LSMResult=}l', '', {'retval': {'already_cfretained': True}}), 'LSMMapAddText': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}I', b'i^{__LSMMap=}^{__LSMText=}I'),), 'LSMTextCreate': (b'^{__LSMText=}^{__CFAllocator=}^{__LSMMap=}', '', {'retval': {'already_cfretained': True}}), 'LSMMapWriteToURL': (sel32or64(b'l^{__LSMMap=}^{__CFURL=}L', b'i^{__LSMMap=}^{__CFURL=}L'),), 'LSMResultGetScore': (b'f^{__LSMResult=}l',), 'LSMMapCreateFromURL': (b'^{__LSMMap=}^{__CFAllocator=}^{__CFURL=}L', '', {'retval': {'already_cfretained': True}}), 'LSMResultCopyToken': (b'^{__CFData=}^{__LSMResult=}l', '', {'retval': {'already_cfretained': True}}), 'LSMMapGetProperties': (b'^{__CFDictionary=}^{__LSMMap=}',), 'LSMMapAddCategory': (b'I^{__LSMMap=}',), 'LSMTextAddWord': (sel32or64(b'l^{__LSMText=}^{__CFString=}', b'i^{__LSMText=}^{__CFString=}'),), 'LSMMapCreate': (b'^{__LSMMap=}^{__CFAllocator=}L', '', {'retval': {'already_cfretained': True}}), 'LSMMapSetProperties': (b'v^{__LSMMap=}^{__CFDictionary=}',)}
cftypes=[('LSMMapRef', b'^{__LSMMap=}', 'LSMMapGetTypeID', None), ('LSMResultRef', b'^{__LSMResult=}', 'LSMResultGetTypeID', None), ('LSMTextRef', b'^{__LSMText=}', 'LSMTextGetTypeID', None)]
expressions = {}

# END OF FILE