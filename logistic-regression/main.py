from numpy import *

import logRegres

from horse import horse

dataArr, labelMat = logRegres.loadDataSet()

# weights = logRegres.gradAscent(dataArr, labelMat)
#
# weights = logRegres.stocGradAscent0(array(dataArr), labelMat)

# weights = logRegres.stocGradAscent1(array(dataArr), labelMat)

# logRegres.plotBestFit(weights)

horse.multiTest()