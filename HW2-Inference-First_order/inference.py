from copy import deepcopy
import re
import sys

KB=[]
KB_IMP=[]
KB_FACT=[]
Failure='failure'
f=''

def OP(query):
	res=query.split('(')
	return res[0]

def ARGS(query):
	res=query.split('(')[1].split(')')[0]
	resVal=res.split(',')
	return resVal

def COMPOUND(query):
	if(type(query)==str):
		if('(' in query):
			return True
		else:
			return False
	else:
		return False

def UNIFY_VAR(var,x,theta_unify_var):
	theta=deepcopy(theta_unify_var)
	if(var in theta.keys()):
		return UNIFY(theta[var],x,theta)
	elif(x in theta.keys()):
		return UNIFY(var,theta[x],theta)
	else:
		theta[var]=x
		return theta

def VARIABLE(query):
	if(type(query) is str and query[0].islower()):
		return True
	else:
		return False

def UNIFY(x,y,theta_unify):
	theta=deepcopy(theta_unify)
	if(theta==Failure):
		return Failure
	elif(x==y):
		return theta
	elif(VARIABLE(x)):
		return UNIFY_VAR(x,y,theta)
	elif(VARIABLE(y)):
		return UNIFY_VAR(y,x,theta)
	elif(COMPOUND(x) and COMPOUND(y)):
		return UNIFY(ARGS(x),ARGS(y),UNIFY(OP(x),OP(y),theta))
	elif(type(x)==list and type(y)==list):
		return UNIFY(x[1:],y[1:],UNIFY(x[0],y[0],theta))
	else:
		return Failure

def FETCH_RULES_FOR_GOAL(KB,goal):
	rule_kb=[]
	for i in range(len(KB)):
		leftFlag=0
		rightFlag=0
		if('=>' in KB[i]):
			clause=KB[i].split('=>')
			clause_rhs=clause[1]
			if(clause_rhs == goal):
				rule_kb.append(KB[i])
				continue
			rhs_check=clause_rhs.split('(')
			goal_check=goal.split('(')
			if(rhs_check[0]==goal_check[0]):
				if(',' in clause_rhs):
					check_rhs_var=rhs_check[1].split(')')
					goal_check_var=goal_check[1].split(')')
					commaLeft=check_rhs_var[0].split(',')[0]
					goalLeft=goal_check_var[0].split(',')[0]
					commaRight=check_rhs_var[0].split(',')[1]
					goalRight=goal_check_var[0].split(',')[1]
					if(type(commaLeft) is str and commaLeft.islower()):
						leftFlag=1
					if(type(commaRight) is str and commaRight.islower()):
						rightFlag=1
					if(type(goalLeft) is str and goalLeft.islower()):
						leftFlag=1
					if(type(goalRight) is str and goalRight.islower()):
						rightFlag=1
					if(leftFlag==0):
						if(commaLeft==goalLeft):
							leftFlag=1
					if(rightFlag==0):
						if(commaRight==goalRight):
							rightFlag=1
					if(leftFlag==1 and rightFlag==1):
						rule_kb.append(KB[i])
						continue
				else:
					commaLeft=rhs_check[1].split(')')[0]
					goalLeft=goal_check[1].split(')')[0]
					if(type(commaLeft) is str and commaLeft.islower()):
						leftFlag=1
					if(type(goalLeft) is str and goalLeft.islower()):
						leftFlag=1
					if(leftFlag==0):
						if(commaLeft==goalLeft):
							leftFlag=1
					if(leftFlag==1):
						rule_kb.append(KB[i])
						continue
		else:
			if(KB[i]==goal):
				rule_kb.append(KB[i])
				continue
			if(KB[i].split('(')[0]==goal.split('(')[0]):
				if(',' in KB[i]):
					leftVar=KB[i].split('(')[1].split(',')[0]
					rightVar=KB[i].split('(')[1].split(',')[1].split(')')[0]
					goalLeftVar=goal.split('(')[1].split(',')[0]
					goalRightVar=goal.split('(')[1].split(',')[1].split(')')[0]
					if(type(leftVar) is str and leftVar.islower()):
						leftFlag=1
					if(type(rightVar) is str and rightVar.islower()):
						rightFlag=1
					if(type(goalLeftVar) is str and goalLeftVar.islower()):
						leftFlag=1
					if(type(goalRightVar) is str and goalRightVar.islower()):
						rightFlag=1
					if(leftFlag==0):
						if(leftVar==goalLeftVar):
							leftFlag=1
					if(rightFlag==0):
						if(rightVar==goalRightVar):
							rightFlag=1
					if(leftFlag==1 and rightFlag==1):
						rule_kb.append(KB[i])
						continue
				else:
					factVar=KB[i].split('(')[1].split(')')[0]
					goalVar=goal.split('(')[1].split(')')[0]
					if(',' not in goal):
						if(type(factVar) is str and factVar.islower()):
							leftFlag=1
						if(type(goalVar) is str and goalVar.islower()):
							leftFlag=1
						if(leftFlag==0):
							if(factVar==goalVar):
								leftFlag=1
						if(leftFlag==1):
							rule_kb.append(KB[i])
							continue
	return rule_kb

def FOL_BC_ASK(KB,goal,theta_ask):
	theta=deepcopy(theta_ask)
	impList=[]
	currentRuleList=[]
	rule_ask=FETCH_RULES_FOR_GOAL(KB_IMP,goal)
	for rule in rule_ask:
		myStr='Query: '+str(rule)+'\n'
		f.write(myStr)
		print 'Query: ',rule
		rhs=rule.split('=>')[1]
		lhs=rule.split('=>')[0]
		lhsRule=lhs.split('&')
		tempDict=UNIFY(rhs,goal,{})
		if tempDict!=Failure:
			temp=0
			for i in range(len(lhsRule)):
				myStr='Query: '+str(lhsRule[i])+'\n'
				f.write(myStr)
				print 'Query: ',lhsRule[i]
				listVar=FOL_BC_ASK(KB,lhsRule[i],theta)
				if listVar!=[]:
					listVar.sort()
					myStr=str(lhsRule[i])+': True: '+str(sorted(list(set(listVar))))+'\n'
					f.write(myStr)
					print lhsRule[i]+': True: '+str(sorted(list(set(listVar))))
				else:
					myStr=str(lhsRule[i])+': False'+'\n'
					f.write(myStr)
					print lhsRule[i]+': False'
				if temp==0:
					impList = listVar
					temp=1
				else:
					impList= list((set(impList) & set(listVar)))
	ruleFact=FETCH_RULES_FOR_GOAL(KB_FACT,goal)
	if ruleFact!=[]:
		for rule in ruleFact:
			variableDictionary=UNIFY(rule,goal,theta)
			if variableDictionary.__contains__('x') :
				impList.append(variableDictionary['x'])
	return impList

def FOL_BC_FACT(KB,goal,theta_fact):
	theta=deepcopy(theta_fact)
	if goal in KB_FACT:
		return True
	else:
		outputValue=False
		for i in KB_IMP:
			rhs=i.split('=>')[1]
			lhs=i.split('=>')[0]
			unifyVar=UNIFY(rhs,goal,theta)
			if unifyVar!=Failure:
				myStr='Query: '+str(i)+'\n'
				f.write(myStr)
				print 'Query:',i
				lhsSplit=lhs.split('&')
				tempValue=True
				for item in lhsSplit:
					pattern="(?<=[\(, ])[a-z][0-9]*(?=[\), ])"
					var=re.findall(pattern,item)
					uniqueVar=list(set(var))
					for i in range(len(uniqueVar)):
						newVar,temp = re.subn("(?<=[\(, ])[a-z][0-9]*(?=[\), ])",unifyVar['x'],item)
					myStr='Query: '+str(item)+'\n'
					f.write(myStr)
					print 'Query:',item
					factValue=FOL_BC_FACT(KB,newVar,theta)
					myStr=str(item)+': '+str(factValue)+'\n'
					f.write(myStr)
					print item+': '+str(factValue)
					tempValue=tempValue and factValue
				outputValue=outputValue or tempValue
		return outputValue

if __name__ == '__main__':
	inputFile=open(sys.argv[1],"r")
	#inputFile=open("input_23.txt","r")
	if inputFile.mode=='r':
		inputFileLines=inputFile.readlines()
		inputFileLines = [line.strip() for line in inputFileLines]
		goal=inputFileLines[0]
		numberLines=int(inputFileLines[1])
		global KB_IMP
		global KB_FACT
		global KB
		for numberRows in range(2,numberLines+2):
			KB.append(inputFileLines[numberRows])
			if '=>' in inputFileLines[numberRows]:
				KB_IMP.append(inputFileLines[numberRows])
			else:
				KB_FACT.append(inputFileLines[numberRows])
		print goal
		print '\n'
		for i in range(numberLines):
			print KB[i]
		print '\n'
		f=open("output.txt","a")
		myStr='Query: '+str(goal)+'\n'
		f.write(myStr)
		print 'Query: ',goal
		pattern="(?<=[\(, ])[a-z][0-9]*(?=[\), ])"
		var=re.findall(pattern,goal)
		uniqueVar=list(set(var))
		if(uniqueVar!=[]):
			returnValue=FOL_BC_ASK(KB,goal,{})
			if returnValue!=[]:
				returnValue.sort()
				myStr=str(goal)+': True: '+str(returnValue)+'\n'
				f.write(myStr)
				print goal+': True: '+str(returnValue)
			else:
				myStr=str(goal)+': False'+'\n'
				f.write(myStr)
				print goal+': False'
		else:
			returnValue=FOL_BC_FACT(KB,goal,{})
			myStr=str(goal)+': '+str(returnValue)+'\n'
			f.write(myStr)
			print goal+': '+str(returnValue)
		f.close()