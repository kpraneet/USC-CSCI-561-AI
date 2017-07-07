import sys
from copy import deepcopy
import itertools

queries=[]
individualQuery={}
listQuery=[]
bayesNetwork={}

def parseQuery(query,flag):
	global individualQuery
	tempDict={}
	tempList=[]
	for i in range(len(query)):
		tempDict={}
		name=query[i]
		value=''
		if '=' in query[i]:
			name=query[i].split('=')[0].strip(' ')
			value=query[i].split('=')[1].strip(' ')
		tempDict['name']=name
		tempDict['value']=value
		tempList.append(tempDict)
	if flag:
		individualQuery['variables']=tempList
	else:
		individualQuery['parents']=tempList

def makeBayesNetwork(queryList):
	global bayesNetwork
	parentList=[]
	truthTable={}
	if '|' in queryList[0]:
		querySplit=queryList[0].split('|')
		nameNode=querySplit[0].strip(' ')
		if ' ' in querySplit[1]:
			parentsSplit=querySplit[1].split(' ')
			for individualParent in parentsSplit:
				if individualParent!='':
					parentList.append(individualParent)
		else:
			parentList.append(querySplit[1].strip(' '))
	else:
		nameNode=queryList[0]
	for i in range(1,len(queryList)):
		dictValue=queryList[i].split(' ')[0]
		dictKey=' '.join(queryList[i].split(' ')[1: ])
		if dictKey == '':
			dictKey='+'
		dictValue=float(dictValue)
		truthTable[dictKey]=dictValue
	#print nameNode
	#print parentList
	#print truthTable
	bayesNetwork[nameNode]={'parents':parentList,'truthTable':truthTable}

def calculateProbability(x,y):
	global bayesNetwork
	listTemp=[]
	varTemp=''
	for i in bayesNetwork[x[0]]['parents']:
		for j in y:
			if j[0]==i:
				listTemp.append(j)
	for k in listTemp:
		varTemp=varTemp+k[1]+' '
	if varTemp=='':
		varTemp='+'
	varTemp=varTemp.strip(' ')
	if x[1]=='+':
		return bayesNetwork[x[0]]['truthTable'][varTemp]
	else:
		return 1.0 - bayesNetwork[x[0]]['truthTable'][varTemp]

def enumerate_all(var,e):
	varE=[]
	if len(var)==0:
		return 1.0
	y=var[0]
	for i in e:
		varE.append(i[0])
	if y in varE:
		varY=[]
		for j in e:
			if y==j[0]:
				varY.append(j)
				break
		return calculateProbability(varY[0],e)*enumerate_all(var[1:],e)
	else:
		return calculateProbability((y,'+'),e)*enumerate_all(var[1:],e+[(y,'+')]) + calculateProbability((y,'-'),e)*enumerate_all(var[1:],e+[(y,'-')])

def normalize(normalizeQ,normalizeX):
	normalizeVar=''
	total=0
	for i in normalizeX:
		normalizeVar=normalizeVar+i[1]+' '
	normalizeVar=normalizeVar.strip(' ')
	for j in normalizeQ.keys():
		total=total+normalizeQ[j]
	return normalizeQ[normalizeVar]/total

def enumeration_ask(x,e,bn):
	q={}
	variableX=[]
	varComb=[]
	individualVariable=[]
	cartesianList=list(itertools.product(('+','-'),repeat=len(x)))
	for i in x:
		variableX.append(i[0])
	for i in range(len(cartesianList)):
		individualVariable=[]
		for j in range(len(cartesianList[i])):
			if cartesianList[i][j]=='+':
				individualVariable.append((variableX[j],'+'))
			else:
				individualVariable.append((variableX[j],'-'))
		varComb.append(individualVariable)
	#print varComb
	for j in range(len(varComb)):
		q[' '.join(cartesianList[j])]=enumerate_all(bn,e+varComb[j])
	return normalize(q,x)

if __name__ == '__main__':
	inputFile=open(sys.argv[1],"r")
	#inputFile=open("sample01.txt","r")
	if inputFile.mode=='r':
		inputFileLines=inputFile.readlines()
		inputFileLines = [line.strip() for line in inputFileLines]
		totalQueries=int(inputFileLines[0])
		networkList=[]
		for inputIndex in range(1,totalQueries+1):
			queries.append(inputFileLines[inputIndex])
		for inputIndex in range(totalQueries+1,len(inputFileLines)):
			networkList.append(inputFileLines[inputIndex])
		#print totalQueries
		#for i in range(len(queries)):
		#	print queries[i]
		#for i in range(len(networkList)):
		#	print networkList[i]
		for i in range(len(queries)):
			individualQuery={}
			singleQuery=queries[i].split('(')[1].split(')')[0]
			if '|' in singleQuery:
				parentList=singleQuery.split('|')[1].strip(' ')
				parents=parentList.split(',')
				parseQuery(parents,False)
				if ',' in singleQuery.split('|')[0]:
					queryVariables=singleQuery.split('|')[0].split(',')
					parseQuery(queryVariables,True)
				else:
					queryVariables=singleQuery.split('|')[0].split(',')
					parseQuery(queryVariables,True)
			else:
				queryVariables=singleQuery.split(',')
				parseQuery(queryVariables,True)
				individualQuery['parents']=[]
			listQuery.append(individualQuery)
		#print listQuery
		tempVar=0
		while tempVar < len(networkList):
			tempList=[]
			if networkList[tempVar]=='***':
				tempVar=tempVar+1
			else:
				while tempVar < len(networkList) and networkList[tempVar]!='***':
					tempList.append(networkList[tempVar])
					tempVar=tempVar+1
				tempVar=tempVar+1
			makeBayesNetwork(tempList)
		#print bayesNetwork
		tempSortList=[]
		bn=[]
		copyBN=deepcopy(bayesNetwork)
		for i in copyBN.keys():
			if len(copyBN[i]['parents'])==0:
				tempSortList.append(i)
		while len(tempSortList)!=0:
			networkNode=tempSortList.pop(0)
			bn.append(networkNode)
			for j in copyBN.keys():
				if networkNode in copyBN[j]['parents']:
					copyBN[j]['parents'].remove(networkNode)
					if len(copyBN[j]['parents'])==0:
						tempSortList.append(j)		
		#print bn
		fileTruncate=open("output.txt","w")
		fileTruncate.truncate()
		fileTruncate.close()
		for i in listQuery:
			x=[]
			e=[]
			variableList=i['variables']
			for j in variableList:
				x.append((j['name'],j['value']))
			listParents=i['parents']
			for k in listParents:
				e.append((k['name'],k['value']))
			output=enumeration_ask(x,e,bn)
			writeOutput=format(output,'.2f')
			#print writeOutput
			f=open("output.txt","a")
			f.write(writeOutput)
			f.write("\n")
			f.close()