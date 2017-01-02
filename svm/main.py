from numpy import matrix, mat

import svmMLiA

# dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
#
# b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)
#
# ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
#
# datMat = mat(dataArr)
# print(datMat[0] * mat(ws) + b)
# print(labelArr[0])

# svmMLiA.testRbf(10.1)

svmMLiA.testDigits(('rbf', 20))