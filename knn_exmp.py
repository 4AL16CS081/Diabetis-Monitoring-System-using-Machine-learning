import operator
import math
import pandas as pd
import csv

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):

		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classvotes={}
	for i in range(len(neighbors)):
		Response=neighbors[i][-1]
		if Response in classvotes:
			classvotes[Response]+=1
		else:
			classvotes[Response]=1
	sortedvotes=sorted(classvotes.items(),key=operator.itemgetter(1),reverse=True)
	return sortedvotes[0][0]

def getAccuracy(testSet,predictions):
	correct=0
	for i in range(len(testSet)):
		if testSet[i][-1]==predictions[i]:
			correct+=1
	return (correct/float(len(testSet)))*100.0


with open('trainingset.csv','r') as csvfile:
	Lines = csv.reader(csvfile)
	l=list(Lines)

trainSet = []

for row in range(len(l)):
	for col in range(8):
		l[row][col]=float(l[row][col])
		trainSet.append(l[row])
print("Train set:",trainSet)


with open('testdata.csv','r') as csvfile:
	Lines=csv.reader(csvfile)
	f=list(Lines)

testSet =[]
k=1
for row in range(len(f)):
	for col in range(8):
		f[row][col] = float(f[row][col])
		testSet.append(f[row])
print("Test Set",testSet)
rannng = range(1,11)
neighbors=[]
predictions=[]
for i in range(len(testSet)):
	neighbors= getNeighbors(trainSet, testSet[i], k)
	response=getResponse(neighbors)
	print("Nearest neighbor:",neighbors)
	print("Response",response)
	predictions.append(response)
	print('>predicted='+repr(response)+',actual='+repr(testSet[row][-1]))

accuracy=getAccuracy(testSet,predictions)
print('Accuracy'+repr(accuracy)+'%')


import matplotlib.pyplot as plt

x=[1,2]
y=[accuracy,0]
plt.title('Accuracy')
plt.bar(x,y)
plt.show()

