import regression
from numpy import *
import matplotlib.pyplot as plt

xArr, yArr = regression.loadDataSet('ex0.txt')

# ws = regression.standRegres(xArr, yArr)

# xMat = mat(xArr)
# yMat = mat(yArr)
# yHat = xMat * ws

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])

# xCopy = xMat.copy()
# xCopy.sort(0)
# yHat = xCopy * ws
# ax.plot(xCopy[:, 1], yHat)
# plt.show()



# yHat = regression.lwlrTest(xArr, xArr, yArr, 0.003)
# xMat = mat(xArr)
#
# srtInd = xMat[:, 1].argsort(0)
# xSort = xMat[srtInd][:, 0, :]
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(xSort[:, 1], yHat[srtInd])
# ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
# plt.show()


# abX, abY = regression.loadDataSet('abalone.txt')

# yHat01 = regression.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
# yHat1 = regression.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 1)
# yHat10 = regression.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 10)
#
# print(regression.rssError(abY[0:99], yHat01.T))
# print(regression.rssError(abY[0:99], yHat1.T))
# print(regression.rssError(abY[0:99], yHat10.T))


# abX, abY = regression.loadDataSet('abalone.txt')
#
# yHat01 = regression.lwlrTest(abX[100:199], abX[0:99], abY[0:99], 0.1)
# print(regression.rssError(abY[100:199], yHat01.T))
#
# yHat1 = regression.lwlrTest(abX[100:199], abX[0:99], abY[0:99], 1)
# print(regression.rssError(abY[100:199], yHat1.T))
#
# yHat10 = regression.lwlrTest(abX[100:199], abX[0:99], abY[0:99], 10)
# print(regression.rssError(abY[100:199], yHat10.T))


abX, abY = regression.loadDataSet('abalone.txt')
ridgeWeights = regression.ridgeTest(abX, abY)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ridgeWeights)
plt.show()
