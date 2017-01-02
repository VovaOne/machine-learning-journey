import adaboost
from numpy import *

# datMat, classLabels = adaboost.loadSimpData()

# D = mat(ones((5, 1)) / 5)
#
# adaboost.buildStump(datMat, classLabels, D)
#
# classifierArray = adaboost.adaBoostTrainDS(datMat, classLabels, 9)


datArr, labelArr = adaboost.loadSimpData()
classifierArr = adaboost.adaBoostTrainDS(datArr, labelArr, 30)
