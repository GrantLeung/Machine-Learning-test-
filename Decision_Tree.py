# -*- coding: UTF-8 -*-
from math import log

"""
函数说明:创建测试数据集

Parameters:
    无
Returns:
    dataSet - 数据集
    labels - 分类属性
"""
def createDataSet():
    dataset =[
        [0, 0, 0, 0, 'no'],
        [0, 0, 0, 1, 'no'],
        [0, 1, 0, 1, 'yes'],
        [0, 1, 1, 0, 'yes'],
        [0, 0, 0, 0, 'no'],
        [1, 0, 0, 0, 'no'],
        [1, 0, 0, 1, 'no'],
        [1, 1, 1, 1, 'yes'],
        [1, 0, 1, 2, 'yes'],
        [1, 0, 1, 2, 'yes'],
        [2, 0, 1, 2, 'yes'],
        [2, 0, 1, 1, 'yes'],
        [2, 1, 0, 1, 'yes'],
        [2, 1, 0, 2, 'yes'],
        [2, 0, 0, 0, 'no']
    ]
    labels = ['不放贷','放贷']
    return dataset, labels

"""
函数说明:计算给定数据集的经验熵(香农熵)
 
Parameters:
    dataSet - 数据集
Returns:
    shannonEnt - 经验熵(香农熵)
"""
def calShannonEnt(dataSet):
    #返回数据集的行数
    numEntireties = len(dataSet)    
    #保存每个标签(Label)出现次数的字典                
    labelCounts = {}
    #对每组特征向量进行统计
    for featVec in dataSet:
        #提取标签(Label)信息
        currentLabel = featVec[-1]
        #如果标签(Label)没有放入统计次数的字典,添加进去
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        #Label计数
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        #选择该标签(Label)的概率
        prob = float(labelCounts[key])/numEntireties
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

"""
函数说明:按照给定特征划分数据集
 
Parameters:
    dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
Returns:
    无
"""
def splitDataSet(dataSet, axis, value):
    #创建返回的数据集列表
    retDataSet = []
    #遍历数据集
    for featVec in dataSet:
        if featVec[axis] == value:
            #去掉axis特征
            reducedFeatVec = featVec[:axis]
            #将符合条件的添加到返回的数据集
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

"""
函数说明:选择最优特征
 
Parameters:
    dataSet - 数据集
Returns:
    bestFeature - 信息增益最大的(最优)特征的索引值
"""
def chooseBestFeatureToSplit(dataSet):
    #特征数量
    numFeatures = len(dataSet[0]) - 1
    #计算数据集的香农熵
    baseEntropy = calShannonEnt(dataSet)
    #信息增益
    bestInfoGain = 0.0
    #最优特征的索引值
    bestFeature = -1
    #遍历所有特征
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        #创建set集合{},元素不可重复
        uniqueVals = set(featList)
        #经验条件熵
        newEntropy = 0.0
        #计算信息增益
        for value in uniqueVals:
            #subDataSet划分后的子集
            subDataSet = splitDataSet(dataSet, i, value)
            #计算子集的概率
            prob = len(subDataSet) / float(len(dataSet))
            #根据公式计算经验条件熵
            newEntropy += prob * calShannonEnt(subDataSet)
        #信息增益
        infoGain = baseEntropy - newEntropy
        #打印每个特征的信息增益
        print("第%d个特征的增益%.3f" % (i, infoGain))
        #计算信息增益
        if (infoGain > bestInfoGain):
            #更新信息增益，找到最大的信息增益
            bestInfoGain = infoGain
            #记录信息增益最大的特征的索引值
            bestFeature = i
    #返回信息增益最大的特征的索引值
    return bestFeature
        

if __name__ == '__main__':
    dataSet, features = createDataSet()
    print("最优特征索引值:" + str(chooseBestFeatureToSplit(dataSet)))