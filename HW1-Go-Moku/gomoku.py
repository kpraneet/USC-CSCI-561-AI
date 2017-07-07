import sys
from copy import deepcopy

def findneighbours(inputMatrix,numberLines):
	neighbourMatrix = []
	for inputIndex in range(numberLines):
		inputRow= [inputCharacter for inputCharacter in inputMatrix[inputIndex]]
		neighbourMatrix.append(inputRow)
	for i in range(numberLines):
		for j in range(numberLines):
			if (inputMatrix[i][j]=='.'):
				if(i==0 and j==0):
					if ((inputMatrix[i][j+1]!='.' and inputMatrix[i][j+1]!='*') or (inputMatrix[i+1][j]!='.' and inputMatrix[i+1][j]!='*') or (inputMatrix[i+1][j+1]!='.' and inputMatrix[i+1][j+1]!='*')):
						neighbourMatrix[i][j]='*'
				elif(i==numberLines-1 and j==numberLines-1):
					if((inputMatrix[i][j-1]!='.' and inputMatrix[i][j-1]!='*') or (inputMatrix[i-1][j]!='.' and inputMatrix[i-1][j]!='*') or (inputMatrix[i-1][j-1]!='.' and inputMatrix[i-1][j-1]!='*')):
						neighbourMatrix[i][j]='*'
				elif(i==0 and j==numberLines-1):
					if((inputMatrix[i][j-1]!='.' and inputMatrix[i][j-1]!='*') or (inputMatrix[i+1][j]!='.' and inputMatrix[i+1][j]!='*') or (inputMatrix[i+1][j-1]!='.' and inputMatrix[i+1][j-1]!='*')):
						neighbourMatrix[i][j]='*'
				elif(i==numberLines-1 and j==0):
					if((inputMatrix[i-1][j]!='.' and inputMatrix[i-1][j]!='*') or (inputMatrix[i-1][j+1]!='.' and inputMatrix[i-1][j+1]!='*') or (inputMatrix[i][j+1]!='.' and inputMatrix[i][j+1]!='*')):
						neighbourMatrix[i][j]='*'
				elif(i==0 and j>0):
					if((inputMatrix[i][j+1]!='.' and inputMatrix[i][j+1]!='*') or (inputMatrix[i][j-1]!='.' and inputMatrix[i][j-1]!='*') or (inputMatrix[i+1][j]!='.' and inputMatrix[i+1][j]!='*') or (inputMatrix[i+1][j+1]!='.' and inputMatrix[i+1][j+1]!='*') or (inputMatrix[i+1][j-1]!='.' and inputMatrix[i+1][j-1]!='*')):
						neighbourMatrix[i][j]='*'
				elif(i==numberLines-1 and j>0):
					if((inputMatrix[i][j+1]!='.' and inputMatrix[i][j+1]!='*') or (inputMatrix[i][j-1]!='.' and inputMatrix[i][j-1]!='*') or (inputMatrix[i-1][j]!='.' and inputMatrix[i-1][j]!='*') or (inputMatrix[i-1][j-1]!='.' and inputMatrix[i-1][j-1]!='*') or (inputMatrix[i-1][j+1]!='.' and inputMatrix[i-1][j+1]!='*')):
						neighbourMatrix[i][j]='*'
				elif(i>0 and j==0):
					if((inputMatrix[i-1][j]!='.' and inputMatrix[i-1][j]!='*') or (inputMatrix[i+1][j]!='.' and inputMatrix[i+1][j]!='*') or (inputMatrix[i][j+1]!='.' and inputMatrix[i][j+1]!='*') or (inputMatrix[i-1][j+1]!='.' and inputMatrix[i-1][j+1]!='*') or (inputMatrix[i+1][j+1]!='.' and inputMatrix[i+1][j+1]!='*')):
						neighbourMatrix[i][j]='*'	
				elif(i>0 and j==numberLines-1):
					if((inputMatrix[i-1][j]!='.' and inputMatrix[i-1][j]!='*') or (inputMatrix[i+1][j]!='.' and inputMatrix[i+1][j]!='*') or (inputMatrix[i][j-1]!='.' and inputMatrix[i][j-1]!='*') or (inputMatrix[i-1][j-1]!='.' and inputMatrix[i-1][j-1]!='*') or (inputMatrix[i+1][j-1]!='.' and inputMatrix[i+1][j-1]!='*')):
						neighbourMatrix[i][j]='*'
				else:
					if ((inputMatrix[i][j+1]!='.' and inputMatrix[i][j+1]!='*') or (inputMatrix[i][j-1]!='.' and inputMatrix[i][j-1]!='*') or (inputMatrix[i-1][j+1]!='.' and inputMatrix[i-1][j+1]!='*') or (inputMatrix[i-1][j-1]!='.' and inputMatrix[i-1][j-1]!='*') or (inputMatrix[i-1][j]!='.' and inputMatrix[i-1][j]!='*') or (inputMatrix[i+1][j+1]!='.' and inputMatrix[i+1][j+1]!='*') or (inputMatrix[i+1][j-1]!='.' and inputMatrix[i+1][j-1]!='*') or (inputMatrix[i+1][j]!='.' and inputMatrix[i+1][j]!='*')):
						neighbourMatrix[i][j]='*'
	return neighbourMatrix

def evalneighbours(inputMatrix,numberLines):
	evalNeighbourValue=[]
	sortValueNeighbour=[]
	for i in range(numberLines):
		for j in range(numberLines):
			if(inputMatrix[i][j]=='*'):
				dictEvalValue={}
				dictEvalValue['x']=i
				dictEvalValue['y']=j
				evalNeighbourValue.append(dictEvalValue)

	sortValueNeighbour=sorted(evalNeighbourValue,key=lambda x:(x['y'],-x['x']))
	return sortValueNeighbour

def eval(evalMatrix,player,numberLines,x,y):
	flagCheck=False
	maxPlayerCount=0
	
	blx=wlx=brx=wrx=x
	bux=wux=bdx=wdx=x
	bly=wly=bry=wry=y
	buy=wuy=bdy=wdy=y
	bdtlx=wdtlx=bdtrx=wdtrx=x
	bdtly=wdtly=bdtry=wdtry=y
	bdblx=wdblx=bdbrx=wdbrx=x
	bdbly=wdbly=bdbry=wdbry=y

	countBlackLeft=0
	countWhiteLeft=0
	countBlackRight=0
	countWhiteRight=0
	countBlackTop=0
	countWhiteTop=0
	countBlackBottom=0
	countWhiteBottom=0
	countBlackTopLeft=0
	countWhiteTopLeft=0
	countBlackTopRight=0
	countWhiteTopRight=0
	countBlackBottomLeft=0
	countWhiteBottomLeft=0
	countBlackBottomRight=0
	countWhiteBottomRight=0

	bly=bly-1
	if(bly>=0):
		while(bly>=0 and evalMatrix[blx][bly]=='b'):
			countBlackLeft=countBlackLeft+1
			bly=bly-1
	wly=wly-1
	if(wly>=0):
		while(wly>=0 and evalMatrix[wlx][wly]=='w'):
			countWhiteLeft=countWhiteLeft+1
			wly=wly-1
	bry=bry+1
	if(bry<=numberLines-1):
		while(bry<=numberLines-1 and evalMatrix[brx][bry]=='b'):
			countBlackRight=countBlackRight+1
			bry=bry+1
	wry=wry+1
	if(wry<=numberLines-1):
		while(wry<=numberLines-1 and evalMatrix[wrx][wry]=='w'):
			countWhiteRight=countWhiteRight+1
			wry=wry+1
	bux=bux-1
	if(bux>=0):
		while(bux>=0 and evalMatrix[bux][buy]=='b'):
			countBlackTop=countBlackTop+1
			bux=bux-1
	wux=wux-1
	if(wux>=0):
		while(wux>=0 and evalMatrix[wux][wuy]=='w'):
			countWhiteTop=countWhiteTop+1
			wux=wux-1
	bdx=bdx+1
	if(bdx<=numberLines-1):
		while(bdx<=numberLines-1 and evalMatrix[bdx][bdy]=='b'):
			countBlackBottom=countBlackBottom+1
			bdx=bdx+1
	wdx=wdx+1
	if(wdx<=numberLines-1):
		while(wdx<=numberLines-1 and evalMatrix[wdx][wdy]=='w'):
			countWhiteBottom=countWhiteBottom+1
			wdx=wdx+1
	bdtlx=bdtlx-1
	bdtly=bdtly-1
	if(bdtlx>=0 and bdtly>=0):
		while(bdtlx>=0 and bdtly>=0 and evalMatrix[bdtlx][bdtly]=='b'):
			countBlackTopLeft=countBlackTopLeft+1
			bdtlx=bdtlx-1
			bdtly=bdtly-1
	wdtlx=wdtlx-1
	wdtly=wdtly-1
	if(wdtlx>=0 and wdtly>=0):
		while(wdtlx>=0 and wdtly>=0 and evalMatrix[wdtlx][wdtly]=='w'):
			countWhiteTopLeft=countWhiteTopLeft+1
			wdtlx=wdtlx-1
			wdtly=wdtly-1
	bdtrx=bdtrx-1
	bdtry=bdtry+1
	if(bdtrx>=0 and bdtry<=numberLines-1):
		while(bdtrx>=0 and bdtry<=numberLines-1 and evalMatrix[bdtrx][bdtry]=='b'):
			countBlackTopRight=countBlackTopRight+1
			bdtrx=bdtrx-1
			bdtry=bdtry+1
	wdtrx=wdtrx-1
	wdtry=wdtry+1
	if(wdtrx>=0 and wdtry<=numberLines-1):
		while(wdtrx>=0 and wdtry<=numberLines-1 and evalMatrix[wdtrx][wdtry]=='w'):
			countWhiteTopRight=countWhiteTopRight+1
			wdtrx=wdtrx-1
			wdtry=wdtry+1
	bdblx=bdblx+1
	bdbly=bdbly-1
	if(bdblx<=numberLines-1 and bdbly>=0):
		while(bdblx<=numberLines-1 and bdbly>=0 and evalMatrix[bdblx][bdbly]=='b'):
			countBlackBottomLeft=countBlackBottomLeft+1
			bdblx=bdblx+1
			bdbly=bdbly-1
	wdblx=wdblx+1
	wdbly=wdbly-1
	if(wdblx<=numberLines-1 and wdbly>=0):
		while(wdblx<=numberLines-1 and wdbly>=0 and evalMatrix[wdblx][wdbly]=='w'):
			countWhiteBottomLeft=countWhiteBottomLeft+1
			wdblx=wdblx+1
			wdbly=wdbly-1
	bdbrx=bdbrx+1
	bdbry=bdbry+1
	if(bdbrx<=numberLines-1 and bdbry<=numberLines-1):
		while(bdbrx<=numberLines-1 and bdbry<=numberLines-1 and evalMatrix[bdbrx][bdbry]=='b'):
			countBlackBottomRight=countBlackBottomRight+1
			bdbrx=bdbrx+1
			bdbry=bdbry+1
	wdbrx=wdbrx+1
	wdbry=wdbry+1
	if(wdbrx<=numberLines-1 and wdbry<=numberLines-1):
		while(wdbrx<=numberLines-1 and wdbry<=numberLines-1 and evalMatrix[wdbrx][wdbry]=='w'):
			countWhiteBottomRight=countWhiteBottomRight+1
			wdbrx=wdbrx+1
			wdbry=wdbry+1

	countBlackLeftBlock=0
	countWhiteLeftBlock=0
	countBlackRightBlock=0
	countWhiteRightBlock=0
	countBlackTopBlock=0
	countWhiteTopBlock=0
	countBlackBottomBlock=0
	countWhiteBottomBlock=0
	countBlackTopLeftBlock=0
	countWhiteTopLeftBlock=0
	countBlackTopRightBlock=0
	countWhiteTopRightBlock=0
	countBlackBottomLeftBlock=0
	countWhiteBottomLeftBlock=0
	countBlackBottomRightBlock=0
	countWhiteBottomRightBlock=0

	if(countBlackLeft==0 and (countWhiteLeft>0 or y==0)):
		countBlackLeftBlock=1
	if(countWhiteLeft==0 and (countBlackLeft>0 or y==0)):
		countWhiteLeftBlock=1
	if(countBlackRight==0 and (countWhiteRight>0 or y==numberLines-1)):
		countBlackRightBlock=1
	if(countWhiteRight==0 and (countBlackRight>0 or y==numberLines-1)):
		countWhiteRightBlock=1
	if(countBlackTop==0 and (countWhiteTop>0 or x==0)):
		countBlackTopBlock=1
	if(countWhiteTop==0 and (countBlackTop>0 or x==0)):
		countWhiteTopBlock=1
	if(countBlackBottom==0 and (countWhiteBottom>0 or x==numberLines-1)):
		countBlackBottomBlock=1
	if(countWhiteBottom==0 and (countBlackBottom>0 or x==numberLines-1)):
		countWhiteBottomBlock=1
	if(countBlackTopLeft==0 and (countWhiteTopLeft>0 or x==0 or y==0)):
		countBlackTopLeftBlock=1
	if(countWhiteTopLeft==0 and (countBlackTopLeft>0 or x==0  or y==0)):
		countWhiteTopLeftBlock=1
	if(countBlackTopRight==0 and (countWhiteTopRight>0 or x==0 or y==numberLines-1)):
		countBlackTopRightBlock=1
	if(countWhiteTopRight==0 and (countBlackTopRight>0 or x==0 or y==numberLines-1)):
		countWhiteTopRightBlock=1
	if(countBlackBottomLeft==0 and (countWhiteBottomLeft>0 or x==numberLines-1 or y==0)):
		countBlackBottomLeftBlock=1
	if(countWhiteBottomLeft==0 and (countBlackBottomLeft>0 or x==numberLines-1 or y==0)):
		countWhiteBottomLeftBlock=1
	if(countBlackBottomRight==0 and (countWhiteBottomRight>0 or x==numberLines-1 or y==numberLines-1)):
		countBlackBottomRightBlock=1
	if(countWhiteBottomRight==0 and (countBlackBottomRight>0 or x==numberLines-1 or y==numberLines-1)):
		countWhiteBottomRightBlock=1

	if(countBlackLeft!=0 and (y-countBlackLeft==0 or evalMatrix[x][y-countBlackLeft-1]=='w')):
		countBlackLeftBlock=1
	if(countWhiteLeft!=0 and (y-countWhiteLeft==0 or evalMatrix[x][y-countWhiteLeft-1]=='b')):
		countWhiteLeftBlock=1
	if(countBlackRight!=0 and (y+countBlackRight==numberLines-1 or evalMatrix[x][y+countBlackRight+1]=='w')):
		countBlackRightBlock=1
	if(countWhiteRight!=0 and (y+countWhiteRight==numberLines-1 or evalMatrix[x][y+countWhiteRight+1]=='b')):
		countWhiteRightBlock=1
	if(countBlackTop!=0 and (x-countBlackTop==0 or evalMatrix[x-countBlackTop-1][y]=='w')):
		countBlackTopBlock=1
	if(countWhiteTop!=0 and (x-countWhiteTop==0 or evalMatrix[x-countWhiteTop-1][y]=='b')):
		countWhiteTopBlock=1
	if(countBlackBottom!=0 and (x+countBlackBottom==numberLines-1 or evalMatrix[x+countBlackBottom+1][y]=='w')):
		countBlackBottomBlock=1
	if(countWhiteBottom!=0 and (x+countWhiteBottom==numberLines-1 or evalMatrix[x+countWhiteBottom+1][y]=='b')):
		countWhiteBottomBlock=1
	if(countBlackTopLeft!=0 and ((x-countBlackTopLeft==0 or y-countBlackTopLeft==0) or evalMatrix[x-countBlackTopLeft-1][y-countBlackTopLeft-1]=='w')):
		countBlackTopLeftBlock=1
	if(countWhiteTopLeft!=0 and ((x-countWhiteTopLeft==0 or y-countWhiteTopLeft==0) or evalMatrix[x-countWhiteTopLeft-1][y-countWhiteTopLeft-1]=='b')):
		countWhiteTopLeftBlock=1
	if(countBlackTopRight!=0 and ((x-countBlackTopRight==0 or y+countBlackTopRight==numberLines-1) or evalMatrix[x-countBlackTopRight-1][y+countBlackTopRight+1]=='w')):
		countBlackTopRightBlock=1
	if(countWhiteTopRight!=0 and ((x-countWhiteTopRight==0 or y+countWhiteTopRight==numberLines-1) or evalMatrix[x-countWhiteTopRight-1][y+countWhiteTopRight+1]=='b')):
		countWhiteTopRightBlock=1
	if(countBlackBottomLeft!=0 and ((x+countBlackBottomLeft==numberLines-1 or y-countBlackBottomLeft==0) or evalMatrix[x+countBlackBottomLeft+1][y-countBlackBottomLeft-1]=='w')):
		countBlackBottomLeftBlock=1
	if(countWhiteBottomLeft!=0 and ((x+countWhiteBottomLeft==numberLines-1 or y-countWhiteBottomLeft==0) or evalMatrix[x+countWhiteBottomLeft+1][y-countWhiteBottomLeft-1]=='b')):
		countWhiteBottomLeftBlock=1
	if(countBlackBottomRight!=0 and ((x+countBlackBottomRight==numberLines-1 or y+countBlackBottomRight==numberLines-1) or evalMatrix[x+countBlackBottomRight+1][y+countBlackBottomRight+1]=='w')):
		countBlackBottomRightBlock=1
	if(countWhiteBottomRight!=0 and ((x+countWhiteBottomRight==numberLines-1 or y+countWhiteBottomRight==numberLines-1) or evalMatrix[x+countWhiteBottomRight+1][y+countWhiteBottomRight+1]=='b')):
		countWhiteBottomRightBlock=1

	if(player==1):
		if(countBlackLeft+countBlackRight>=4 or countBlackTop+countBlackBottom>=4 or countBlackTopLeft+countBlackBottomRight>=4 or countBlackTopRight+countBlackBottomLeft>=4):
			flagCheck=True
			if(countBlackLeft+countBlackRight>=4):
				maxPlayerCount=maxPlayerCount+50000
			if(countBlackTop+countBlackBottom>=4):
				maxPlayerCount=maxPlayerCount+50000
			if(countBlackTopLeft+countBlackBottomRight>=4):
				maxPlayerCount=maxPlayerCount+50000
			if(countBlackTopRight+countBlackBottomLeft>=4):
				maxPlayerCount=maxPlayerCount+50000
			
		if((countWhiteLeft==4 and countWhiteLeftBlock==1) or (countWhiteRight==4 and countWhiteRightBlock==1) or (countWhiteTop==4 and countWhiteTopBlock==1) or (countWhiteBottom==4 and countWhiteBottomBlock==1) or (countWhiteTopLeft==4 and countWhiteTopLeftBlock==1) or (countWhiteTopRight==4 and countWhiteTopRightBlock==1) or (countWhiteBottomLeft==4 and countWhiteBottomLeftBlock==1) or (countWhiteBottomRight==4 and countWhiteBottomRightBlock==1)):
			if(countWhiteLeft==4 and countWhiteLeftBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteRight==4 and countWhiteRightBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteTop==4 and countWhiteTopBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteBottom==4 and countWhiteBottomBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteTopLeft==4 and countWhiteTopLeftBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteTopRight==4 and countWhiteTopRightBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteBottomLeft==4 and countWhiteBottomLeftBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countWhiteBottomRight==4 and countWhiteBottomRightBlock==1):
				maxPlayerCount=maxPlayerCount+10000

		if((countBlackLeft+countBlackRight==3 and countBlackLeftBlock==0 and countBlackRightBlock==0) or (countBlackTop+countBlackBottom==3 and countBlackTopBlock==0 and countBlackBottomBlock==0) or (countBlackTopLeft+countBlackBottomRight==3 and countBlackTopLeftBlock==0 and countBlackBottomRightBlock==0) or (countBlackTopRight+countBlackBottomLeft==3 and countBlackTopRightBlock==0 and countBlackBottomLeftBlock==0)):
			if(countBlackLeft+countBlackRight==3 and countBlackLeftBlock==0 and countBlackRightBlock==0):
				maxPlayerCount=maxPlayerCount+5000
			if(countBlackTop+countBlackBottom==3 and countBlackTopBlock==0 and countBlackBottomBlock==0):
				maxPlayerCount=maxPlayerCount+5000
			if(countBlackTopLeft+countBlackBottomRight==3 and countBlackTopLeftBlock==0 and countBlackBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+5000
			if(countBlackTopRight+countBlackBottomLeft==3 and countBlackTopRightBlock==0 and countBlackBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+5000

		if(((countBlackLeft+countBlackRight==3) and ((countBlackLeftBlock==1 and countBlackRightBlock==0) or (countBlackLeftBlock==0 and countBlackRightBlock==1))) or ((countBlackTop+countBlackBottom==3) and ((countBlackTopBlock==1 and countBlackBottomBlock==0) or (countBlackTopBlock==0 and countBlackBottomBlock==1))) or ((countBlackTopLeft+countBlackBottomRight==3) and ((countBlackTopLeftBlock==1 and countBlackBottomRightBlock==0) or (countBlackTopLeftBlock==0 and countBlackBottomRightBlock==1))) or ((countBlackTopRight+countBlackBottomLeft==3) and ((countBlackTopRightBlock==1 and countBlackBottomLeftBlock==0) or (countBlackTopRightBlock==0 and countBlackBottomLeftBlock==1)))):
			if((countBlackLeft+countBlackRight==3) and ((countBlackLeftBlock==1 and countBlackRightBlock==0) or (countBlackLeftBlock==0 and countBlackRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
			if((countBlackTop+countBlackBottom==3) and ((countBlackTopBlock==1 and countBlackBottomBlock==0) or (countBlackTopBlock==0 and countBlackBottomBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
			if((countBlackTopLeft+countBlackBottomRight==3) and ((countBlackTopLeftBlock==1 and countBlackBottomRightBlock==0) or (countBlackTopLeftBlock==0 and countBlackBottomRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
			if((countBlackTopRight+countBlackBottomLeft==3) and ((countBlackTopRightBlock==1 and countBlackBottomLeftBlock==0) or (countBlackTopRightBlock==0 and countBlackBottomLeftBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
		
		if((countWhiteLeft==3 and countWhiteLeftBlock==0) or (countWhiteRight==3 and countWhiteRightBlock==0) or (countWhiteTop==3 and countWhiteTopBlock==0) or (countWhiteBottom==3 and countWhiteBottomBlock==0) or (countWhiteTopLeft==3 and countWhiteTopLeftBlock==0) or (countWhiteTopRight==3 and countWhiteTopRightBlock==0) or (countWhiteBottomLeft==3 and countWhiteBottomLeftBlock==0) or (countWhiteBottomRight==3 and countWhiteBottomRightBlock==0)):
			if(countWhiteLeft==3 and countWhiteLeftBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteRight==3 and countWhiteRightBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteTop==3 and countWhiteTopBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteBottom==3 and countWhiteBottomBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteTopLeft==3 and countWhiteTopLeftBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteTopRight==3 and countWhiteTopRightBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteBottomLeft==3 and countWhiteBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countWhiteBottomRight==3 and countWhiteBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+500
			
		if((countWhiteLeft==3 and countWhiteLeftBlock==1) or (countWhiteRight==3 and countWhiteRightBlock==1) or (countWhiteTop==3 and countWhiteTopBlock==1) or (countWhiteBottom==3 and countWhiteBottomBlock==1) or (countWhiteTopLeft==3 and countWhiteTopLeftBlock==1) or (countWhiteTopRight==3 and countWhiteTopRightBlock==1) or (countWhiteBottomLeft==3 and countWhiteBottomLeftBlock==1) or (countWhiteBottomRight==3 and countWhiteBottomRightBlock==1)):
			if(countWhiteLeft==3 and countWhiteLeftBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteRight==3 and countWhiteRightBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteTop==3 and countWhiteTopBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteBottom==3 and countWhiteBottomBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteTopLeft==3 and countWhiteTopLeftBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteTopRight==3 and countWhiteTopRightBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteBottomLeft==3 and countWhiteBottomLeftBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countWhiteBottomRight==3 and countWhiteBottomRightBlock==1):
				maxPlayerCount=maxPlayerCount+100

		if((countBlackLeft+countBlackRight==2 and countBlackLeftBlock==0 and countBlackRightBlock==0) or (countBlackTop+countBlackBottom==2 and countBlackTopBlock==0 and countBlackBottomBlock==0) or (countBlackTopLeft+countBlackBottomRight==2 and countBlackTopLeftBlock==0 and countBlackBottomRightBlock==0) or (countBlackTopRight+countBlackBottomLeft==2 and countBlackTopRightBlock==0 and countBlackBottomLeftBlock==0)):
			if(countBlackLeft+countBlackRight==2 and countBlackLeftBlock==0 and countBlackRightBlock==0):
				maxPlayerCount=maxPlayerCount+50
			if(countBlackTop+countBlackBottom==2 and countBlackTopBlock==0 and countBlackBottomBlock==0):
				maxPlayerCount=maxPlayerCount+50
			if(countBlackTopLeft+countBlackBottomRight==2 and countBlackTopLeftBlock==0 and countBlackBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+50
			if(countBlackTopRight+countBlackBottomLeft==2 and countBlackTopRightBlock==0 and countBlackBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+50

		if(((countBlackLeft+countBlackRight==2) and ((countBlackLeftBlock==1 and countBlackRightBlock==0) or (countBlackLeftBlock==0 and countBlackRightBlock==1))) or ((countBlackTop+countBlackBottom==2) and ((countBlackTopBlock==1 and countBlackBottomBlock==0) or (countBlackTopBlock==0 and countBlackBottomBlock==1))) or ((countBlackTopLeft+countBlackBottomRight==2) and ((countBlackTopLeftBlock==1 and countBlackBottomRightBlock==0) or (countBlackTopLeftBlock==0 and countBlackBottomRightBlock==1))) or ((countBlackTopRight+countBlackBottomLeft==2) and ((countBlackTopRightBlock==1 and countBlackBottomLeftBlock==0) or (countBlackTopRightBlock==0 and countBlackBottomLeftBlock==1)))):
			if((countBlackLeft+countBlackRight==2) and ((countBlackLeftBlock==1 and countBlackRightBlock==0) or (countBlackLeftBlock==0 and countBlackRightBlock==1))):
				maxPlayerCount=maxPlayerCount+10
			if((countBlackTop+countBlackBottom==2) and ((countBlackTopBlock==1 and countBlackBottomBlock==0) or (countBlackTopBlock==0 and countBlackBottomBlock==1))):
				maxPlayerCount=maxPlayerCount+10
			if((countBlackTopLeft+countBlackBottomRight==2) and ((countBlackTopLeftBlock==1 and countBlackBottomRightBlock==0) or (countBlackTopLeftBlock==0 and countBlackBottomRightBlock==1))):
				maxPlayerCount=maxPlayerCount+10
			if((countBlackTopRight+countBlackBottomLeft==2) and ((countBlackTopRightBlock==1 and countBlackBottomLeftBlock==0) or (countBlackTopRightBlock==0 and countBlackBottomLeftBlock==1))):
				maxPlayerCount=maxPlayerCount+10

		if((countBlackLeft+countBlackRight==1 and countBlackLeftBlock==0 and countBlackRightBlock==0) or (countBlackTop+countBlackBottom==1 and countBlackTopBlock==0 and countBlackBottomBlock==0) or (countBlackTopLeft+countBlackBottomRight==1 and countBlackTopLeftBlock==0 and countBlackBottomRightBlock==0) or (countBlackTopRight+countBlackBottomLeft==1 and countBlackTopRightBlock==0 and countBlackBottomLeftBlock==0)):
			if(countBlackLeft+countBlackRight==1 and countBlackLeftBlock==0 and countBlackRightBlock==0):
				maxPlayerCount=maxPlayerCount+5
			if(countBlackTop+countBlackBottom==1 and countBlackTopBlock==0 and countBlackBottomBlock==0):
				maxPlayerCount=maxPlayerCount+5
			if(countBlackTopLeft+countBlackBottomRight==1 and countBlackTopLeftBlock==0 and countBlackBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+5
			if(countBlackTopRight+countBlackBottomLeft==1 and countBlackTopRightBlock==0 and countBlackBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+5

		if(((countBlackLeft+countBlackRight==1) and ((countBlackLeftBlock==1 and countBlackRightBlock==0) or (countBlackLeftBlock==0 and countBlackRightBlock==1))) or ((countBlackTop+countBlackBottom==1) and ((countBlackTopBlock==1 and countBlackBottomBlock==0) or (countBlackTopBlock==0 and countBlackBottomBlock==1))) or ((countBlackTopLeft+countBlackBottomRight==1) and ((countBlackTopLeftBlock==1 and countBlackBottomRightBlock==0) or (countBlackTopLeftBlock==0 and countBlackBottomRightBlock==1))) or ((countBlackTopRight+countBlackBottomLeft==1) and ((countBlackTopRightBlock==1 and countBlackBottomLeftBlock==0) or (countBlackTopRightBlock==0 and countBlackBottomLeftBlock==1)))):
			if((countBlackLeft+countBlackRight==1) and ((countBlackLeftBlock==1 and countBlackRightBlock==0) or (countBlackLeftBlock==0 and countBlackRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1
			if((countBlackTop+countBlackBottom==1) and ((countBlackTopBlock==1 and countBlackBottomBlock==0) or (countBlackTopBlock==0 and countBlackBottomBlock==1))):
				maxPlayerCount=maxPlayerCount+1
			if((countBlackTopLeft+countBlackBottomRight==1) and ((countBlackTopLeftBlock==1 and countBlackBottomRightBlock==0) or (countBlackTopLeftBlock==0 and countBlackBottomRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1
			if((countBlackTopRight+countBlackBottomLeft==1) and ((countBlackTopRightBlock==1 and countBlackBottomLeftBlock==0) or (countBlackTopRightBlock==0 and countBlackBottomLeftBlock==1))):
				maxPlayerCount=maxPlayerCount+1
	else:
		if(countWhiteLeft+countWhiteRight>=4 or countWhiteTop+countWhiteBottom>=4 or countWhiteTopLeft+countWhiteBottomRight>=4 or countWhiteTopRight+countWhiteBottomLeft>=4):
			flagCheck=True
			if(countWhiteLeft+countWhiteRight>=4):
				maxPlayerCount=maxPlayerCount+50000
			if(countWhiteTop+countWhiteBottom>=4):
				maxPlayerCount=maxPlayerCount+50000
			if(countWhiteTopLeft+countWhiteBottomRight>=4):
				maxPlayerCount=maxPlayerCount+50000
			if(countWhiteTopRight+countWhiteBottomLeft>=4):
				maxPlayerCount=maxPlayerCount+50000

		if((countBlackLeft==4 and countBlackLeftBlock==1) or (countBlackRight==4 and countBlackRightBlock==1) or (countBlackTop==4 and countBlackTopBlock==1) or (countBlackBottom==4 and countBlackBottomBlock==1) or (countBlackTopLeft==4 and countBlackTopLeftBlock==1) or (countBlackTopRight==4 and countBlackTopRightBlock==1) or (countBlackBottomLeft==4 and countBlackBottomLeftBlock==1) or (countBlackBottomRight==4 and countBlackBottomRightBlock==1)):
			if(countBlackLeft==4 and countBlackLeftBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackRight==4 and countBlackRightBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackTop==4 and countBlackTopBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackBottom==4 and countBlackBottomBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackTopLeft==4 and countBlackTopLeftBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackTopRight==4 and countBlackTopRightBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackBottomLeft==4 and countBlackBottomLeftBlock==1):
				maxPlayerCount=maxPlayerCount+10000
			if(countBlackBottomRight==4 and countBlackBottomRightBlock==1):
				maxPlayerCount=maxPlayerCount+10000

		if((countWhiteLeft+countWhiteRight==3 and countWhiteLeftBlock==0 and countWhiteRightBlock==0) or (countWhiteTop+countWhiteBottom==3 and countWhiteTopBlock==0 and countWhiteBottomBlock==0) or (countWhiteTopLeft+countWhiteBottomRight==3 and countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==0) or (countWhiteTopRight+countWhiteBottomLeft==3 and countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==0)):
			if(countWhiteLeft+countWhiteRight==3 and countWhiteLeftBlock==0 and countWhiteRightBlock==0):
				maxPlayerCount=maxPlayerCount+5000
			if(countWhiteTop+countWhiteBottom==3 and countWhiteTopBlock==0 and countWhiteBottomBlock==0):
				maxPlayerCount=maxPlayerCount+5000
			if(countWhiteTopLeft+countWhiteBottomRight==3 and countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+5000
			if(countWhiteTopRight+countWhiteBottomLeft==3 and countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+5000

		if(((countWhiteLeft+countWhiteRight==3) and ((countWhiteLeftBlock==1 and countWhiteRightBlock==0) or (countWhiteLeftBlock==0 and countWhiteRightBlock==1))) or ((countWhiteTop+countWhiteBottom==3) and ((countWhiteTopBlock==1 and countWhiteBottomBlock==0) or (countWhiteTopBlock==0 and countWhiteBottomBlock==1))) or ((countWhiteTopLeft+countWhiteBottomRight==3) and ((countWhiteTopLeftBlock==1 and countWhiteBottomRightBlock==0) or (countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==1))) or ((countWhiteTopRight+countWhiteBottomLeft==3) and ((countWhiteTopRightBlock==1 and countWhiteBottomLeftBlock==0) or (countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==1)))):
			if((countWhiteLeft+countWhiteRight==3) and ((countWhiteLeftBlock==1 and countWhiteRightBlock==0) or (countWhiteLeftBlock==0 and countWhiteRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
			if((countWhiteTop+countWhiteBottom==3) and ((countWhiteTopBlock==1 and countWhiteBottomBlock==0) or (countWhiteTopBlock==0 and countWhiteBottomBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
			if((countWhiteTopLeft+countWhiteBottomRight==3) and ((countWhiteTopLeftBlock==1 and countWhiteBottomRightBlock==0) or (countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1000
			if((countWhiteTopRight+countWhiteBottomLeft==3) and ((countWhiteTopRightBlock==1 and countWhiteBottomLeftBlock==0) or (countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==1))):
				maxPlayerCount=maxPlayerCount+1000

		if((countBlackLeft==3 and countBlackLeftBlock==0) or (countBlackRight==3 and countBlackRightBlock==0) or (countBlackTop==3 and countBlackTopBlock==0) or (countBlackBottom==3 and countBlackBottomBlock==0) or (countBlackTopLeft==3 and countBlackTopLeftBlock==0) or (countBlackTopRight==3 and countBlackTopRightBlock==0) or (countBlackBottomLeft==3 and countBlackBottomLeftBlock==0) or (countBlackBottomRight==3 and countBlackBottomRightBlock==0)):
			if(countBlackLeft==3 and countBlackLeftBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackRight==3 and countBlackRightBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackTop==3 and countBlackTopBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackBottom==3 and countBlackBottomBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackTopLeft==3 and countBlackTopLeftBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackTopRight==3 and countBlackTopRightBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackBottomLeft==3 and countBlackBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+500
			if(countBlackBottomRight==3 and countBlackBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+500

		if((countBlackLeft==3 and countBlackLeftBlock==1) or (countBlackRight==3 and countBlackRightBlock==1) or (countBlackTop==3 and countBlackTopBlock==1) or (countBlackBottom==3 and countBlackBottomBlock==1) or (countBlackTopLeft==3 and countBlackTopLeftBlock==1) or (countBlackTopRight==3 and countBlackTopRightBlock==1) or (countBlackBottomLeft==3 and countBlackBottomLeftBlock==1) or (countBlackBottomRight==3 and countBlackBottomRightBlock==1)):
			if(countBlackLeft==3 and countBlackLeftBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackRight==3 and countBlackRightBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackTop==3 and countBlackTopBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackBottom==3 and countBlackBottomBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackTopLeft==3 and countBlackTopLeftBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackTopRight==3 and countBlackTopRightBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackBottomLeft==3 and countBlackBottomLeftBlock==1):
				maxPlayerCount=maxPlayerCount+100
			if(countBlackBottomRight==3 and countBlackBottomRightBlock==1):
				maxPlayerCount=maxPlayerCount+100

		if((countWhiteLeft+countWhiteRight==2 and countWhiteLeftBlock==0 and countWhiteRightBlock==0) or (countWhiteTop+countWhiteBottom==2 and countWhiteTopBlock==0 and countWhiteBottomBlock==0) or (countWhiteTopLeft+countWhiteBottomRight==2 and countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==0) or (countWhiteTopRight+countWhiteBottomLeft==2 and countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==0)):
			if(countWhiteLeft+countWhiteRight==2 and countWhiteLeftBlock==0 and countWhiteRightBlock==0):
				maxPlayerCount=maxPlayerCount+50
			if(countWhiteTop+countWhiteBottom==2 and countWhiteTopBlock==0 and countWhiteBottomBlock==0):
				maxPlayerCount=maxPlayerCount+50
			if(countWhiteTopLeft+countWhiteBottomRight==2 and countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+50
			if(countWhiteTopRight+countWhiteBottomLeft==2 and countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+50

		if(((countWhiteLeft+countWhiteRight==2) and ((countWhiteLeftBlock==1 and countWhiteRightBlock==0) or (countWhiteLeftBlock==0 and countWhiteRightBlock==1))) or ((countWhiteTop+countWhiteBottom==2) and ((countWhiteTopBlock==1 and countWhiteBottomBlock==0) or (countWhiteTopBlock==0 and countWhiteBottomBlock==1))) or ((countWhiteTopLeft+countWhiteBottomRight==2) and ((countWhiteTopLeftBlock==1 and countWhiteBottomRightBlock==0) or (countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==1))) or ((countWhiteTopRight+countWhiteBottomLeft==2) and ((countWhiteTopRightBlock==1 and countWhiteBottomLeftBlock==0) or (countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==1)))):
			if((countWhiteLeft+countWhiteRight==2) and ((countWhiteLeftBlock==1 and countWhiteRightBlock==0) or (countWhiteLeftBlock==0 and countWhiteRightBlock==1))):
				maxPlayerCount=maxPlayerCount+10
			if((countWhiteTop+countWhiteBottom==2) and ((countWhiteTopBlock==1 and countWhiteBottomBlock==0) or (countWhiteTopBlock==0 and countWhiteBottomBlock==1))):
				maxPlayerCount=maxPlayerCount+10
			if((countWhiteTopLeft+countWhiteBottomRight==2) and ((countWhiteTopLeftBlock==1 and countWhiteBottomRightBlock==0) or (countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==1))):
				maxPlayerCount=maxPlayerCount+10
			if((countWhiteTopRight+countWhiteBottomLeft==2) and ((countWhiteTopRightBlock==1 and countWhiteBottomLeftBlock==0) or (countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==1))):
				maxPlayerCount=maxPlayerCount+10

		if((countWhiteLeft+countWhiteRight==1 and countWhiteLeftBlock==0 and countWhiteRightBlock==0) or (countWhiteTop+countWhiteBottom==1 and countWhiteTopBlock==0 and countWhiteBottomBlock==0) or (countWhiteTopLeft+countWhiteBottomRight==1 and countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==0) or (countWhiteTopRight+countWhiteBottomLeft==1 and countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==0)):
			if(countWhiteLeft+countWhiteRight==1 and countWhiteLeftBlock==0 and countWhiteRightBlock==0):
				maxPlayerCount=maxPlayerCount+5
			if(countWhiteTop+countWhiteBottom==1 and countWhiteTopBlock==0 and countWhiteBottomBlock==0):
				maxPlayerCount=maxPlayerCount+5
			if(countWhiteTopLeft+countWhiteBottomRight==1 and countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==0):
				maxPlayerCount=maxPlayerCount+5
			if(countWhiteTopRight+countWhiteBottomLeft==1 and countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==0):
				maxPlayerCount=maxPlayerCount+5

		if(((countWhiteLeft+countWhiteRight==1) and ((countWhiteLeftBlock==1 and countWhiteRightBlock==0) or (countWhiteLeftBlock==0 and countWhiteRightBlock==1))) or ((countWhiteTop+countWhiteBottom==1) and ((countWhiteTopBlock==1 and countWhiteBottomBlock==0) or (countWhiteTopBlock==0 and countWhiteBottomBlock==1))) or ((countWhiteTopLeft+countWhiteBottomRight==1) and ((countWhiteTopLeftBlock==1 and countWhiteBottomRightBlock==0) or (countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==1))) or ((countWhiteTopRight+countWhiteBottomLeft==1) and ((countWhiteTopRightBlock==1 and countWhiteBottomLeftBlock==0) or (countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==1)))):
			if((countWhiteLeft+countWhiteRight==1) and ((countWhiteLeftBlock==1 and countWhiteRightBlock==0) or (countWhiteLeftBlock==0 and countWhiteRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1
			if((countWhiteTop+countWhiteBottom==1) and ((countWhiteTopBlock==1 and countWhiteBottomBlock==0) or (countWhiteTopBlock==0 and countWhiteBottomBlock==1))):
				maxPlayerCount=maxPlayerCount+1
			if((countWhiteTopLeft+countWhiteBottomRight==1) and ((countWhiteTopLeftBlock==1 and countWhiteBottomRightBlock==0) or (countWhiteTopLeftBlock==0 and countWhiteBottomRightBlock==1))):
				maxPlayerCount=maxPlayerCount+1
			if((countWhiteTopRight+countWhiteBottomLeft==1) and ((countWhiteTopRightBlock==1 and countWhiteBottomLeftBlock==0) or (countWhiteTopRightBlock==0 and countWhiteBottomLeftBlock==1))):
				maxPlayerCount=maxPlayerCount+1

	dictionaryReturnValues={}
	dictionaryReturnValues['x']=x
	dictionaryReturnValues['y']=y
	dictionaryReturnValues['value']=maxPlayerCount
	if(flagCheck==True):
		dictionaryReturnValues['isWin']=True
	else:
		dictionaryReturnValues['isWin']=False
	return dictionaryReturnValues
	
def greedy(inputMatrix,greedyMatrix,player,numberLines):
	evalValueGreedy=[]
	sortValueGreedy=[]
	greedyCount=0
	for i in range(numberLines):
		for j in range(numberLines):
			if (greedyMatrix[i][j]=='*'):
				greedyCount=greedyCount+1
				evalValueGreedy.append(eval(greedyMatrix,player,numberLines,i,j))
	sortValueGreedy=sorted(evalValueGreedy,key=lambda x:(-x['value'],x['y'],-x['x']))
	finalGreedyValues=sortValueGreedy[0]
	if(player==1):
		inputMatrix[finalGreedyValues['x']][finalGreedyValues['y']]='b'
	else:
		inputMatrix[finalGreedyValues['x']][finalGreedyValues['y']]='w'

	f=open("next_state.txt","w")
	for innerList in inputMatrix:
		for element in innerList:
			f.write(element)
		f.write('\n')
	f.close()

class myTree:
	def __init__(self,boardMartix,depth,x,y,player,numberLines):
		self.boardMartix=boardMartix
		self.evalValue=0
		self.parent=[]
		self.children=[]
		self.depth=depth
		self.x=x
		self.y=y
		self.player=player
		self.numberLines=numberLines
		self.branchSum=0
		self.alpha=0
		self.beta=0
	def printTree(self):
		for matrixLength in range(self.numberLines):
			print self.boardMartix[matrixLength]
		print self.evalValue
		print self.parent
		print self.children
		print self.depth
		print self.x
		print self.y
		print self.player
		print self.numberLines
		print self.branchSum
		print self.alpha
		print self.beta
	def addNode(self,nodeTree):
		self.children.append(nodeTree)

def printCharacters(x,y,depth,value,numberLines):
	f=open("traverse_log.txt","a")
	if(depth==0):
		if(value==-99999999):
			f.write('root,0,-Infinity')
			f.write("\n")
		elif(value==99999999):
			f.write('root,0,Infinity')
			f.write("\n")
		else:
			f.write('root,0,%d' %value)
			f.write("\n")
	else:
		if(value==99999999):
			f.write('%c%d,%d,Infinity' %(chr(y+65),numberLines-x,depth))
			f.write("\n")
		elif(value==-99999999):
			f.write('%c%d,%d,-Infinity' %(chr(y+65),numberLines-x,depth))
			f.write("\n")
		else:
			f.write('%c%d,%d,%d' %(chr(y+65),numberLines-x,depth,value))
			f.write("\n")
	f.close()

def printAlphaBeta(x,y,depth,value,numberLines,alpha,beta):
	f=open("traverse_log.txt","a")
	if(value==99999999):
		printValue='Infinity'
	elif(value==-99999999):
		printValue='-Infinity'
	else:
		printValue=value
	if(alpha==99999999):
		alphaValue='Infinity'
	elif(alpha==-99999999):
		alphaValue='-Infinity'
	else:
		alphaValue=alpha
	if(beta==99999999):
		betaValue='Infinity'
	elif(beta==-99999999):
		betaValue='-Infinity'
	else:
		betaValue=beta
	if(depth==0):
		f.write('root,0,')
		if(isinstance(printValue, basestring)):
			f.write('%s' %printValue)
		else:
			f.write('%d' %printValue)
		f.write(',')
		if(isinstance(alphaValue, basestring)):
			f.write('%s' %alphaValue)
		else:
			f.write('%d' %alphaValue)
		f.write(',')
		if(isinstance(betaValue, basestring)):
			f.write('%s' %betaValue)
		else:
			f.write('%d' %betaValue)
		f.write("\n")
	else:
		f.write(chr(y+65))
		f.write('%d' %(numberLines-x))
		f.write(',')
		f.write('%d' %depth)
		f.write(',')
		if(isinstance(printValue, basestring)):
			f.write('%s' %printValue)
		else:
			f.write('%d' %printValue)
		f.write(',')
		if(isinstance(alphaValue, basestring)):
			f.write('%s' %alphaValue)
		else:
			f.write('%d' %alphaValue)
		f.write(',')
		if(isinstance(betaValue, basestring)):
			f.write('%s' %betaValue)
		else:
			f.write('%d' %betaValue)
		f.write("\n")
	f.close()

def traverse(node,inputMatrix,depthValue,depth,maximizingPlayer,player,opponent,numberLines):
	if(depthValue==depth):
		return
	winFlag=False
	neighbourMatrix=findneighbours(node.boardMartix,numberLines)
	neighbourSortValue=[]
	copyMatrix=[]
	neighbourSortValue=evalneighbours(neighbourMatrix,numberLines)
	copyMatrix=deepcopy(node.boardMartix)
	for i in range(len(neighbourSortValue)):
		tempValue=neighbourSortValue[i]
		x=tempValue['x']
		y=tempValue['y']
		if(player==1):
			copyMatrix[x][y]='b'
		else:
			copyMatrix[x][y]='w'
		rootChildren=myTree(copyMatrix,depthValue+1,x,y,player,numberLines)
		rootChildren.parent=node
		node.addNode(rootChildren)
		minimaxValue=eval(rootChildren.boardMartix,rootChildren.player,rootChildren.numberLines,rootChildren.x,rootChildren.y)
		if(minimaxValue['isWin']==True):
			winFlag=True
		if(not maximizingPlayer):
			minimaxValue['value']=-1*minimaxValue['value']
		if(rootChildren.depth==depth):
			rootChildren.evalValue=minimaxValue['value']+rootChildren.parent.branchSum
		else:
			rootChildren.branchSum=minimaxValue['value']+rootChildren.parent.branchSum
			bestValue=99999999
			if(maximizingPlayer):
				rootChildren.evalValue=bestValue
			else:
				rootChildren.evalValue=-1*bestValue
			if(winFlag):
				rootChildren.evalValue=rootChildren.branchSum	
		printCharacters(x,y,rootChildren.depth,rootChildren.evalValue,numberLines)
		if(not winFlag):
			traverse(rootChildren,rootChildren.boardMartix,rootChildren.depth,depth,not maximizingPlayer,opponent,player,numberLines)
		copyMatrix[x][y]='.'
		if(maximizingPlayer):
			if(rootChildren.evalValue>node.evalValue):
				node.evalValue=rootChildren.evalValue
		else:
			if(rootChildren.evalValue<node.evalValue):
				node.evalValue=rootChildren.evalValue
		printCharacters(node.x,node.y,node.depth,node.evalValue,numberLines)
		winFlag=False

def alphabeta(node,inputMatrix,depthValue,depth,maximizingPlayer,player,opponent,numberLines,alpha,beta):
	if(depthValue==depth):
		return
	winFlag=False
	cutFlag=False
	neighbourMatrix=findneighbours(node.boardMartix,numberLines)
	neighbourSortValue=[]
	copyMatrix=[]
	neighbourSortValue=evalneighbours(neighbourMatrix,numberLines)
	copyMatrix=deepcopy(node.boardMartix)
	for i in range(len(neighbourSortValue)):
		tempValue=neighbourSortValue[i]
		x=tempValue['x']
		y=tempValue['y']
		if(player==1):
			copyMatrix[x][y]='b'
		else:
			copyMatrix[x][y]='w'
		rootChildren=myTree(copyMatrix,depthValue+1,x,y,player,numberLines)
		rootChildren.parent=node
		rootChildren.alpha=node.alpha
		rootChildren.beta=node.beta
		node.addNode(rootChildren)
		minimaxValue=eval(rootChildren.boardMartix,rootChildren.player,rootChildren.numberLines,rootChildren.x,rootChildren.y)
		if(minimaxValue['isWin']==True):
			winFlag=True
		if(not maximizingPlayer):
			minimaxValue['value']=-1*minimaxValue['value']
		if(rootChildren.depth==depth):
			rootChildren.evalValue=minimaxValue['value']+rootChildren.parent.branchSum
		else:
			rootChildren.branchSum=minimaxValue['value']+rootChildren.parent.branchSum
			bestValue=99999999
			if(maximizingPlayer):
				rootChildren.evalValue=bestValue
			else:
				rootChildren.evalValue=-1*bestValue
			if(winFlag):
				rootChildren.evalValue=rootChildren.branchSum	
		printAlphaBeta(x,y,rootChildren.depth,rootChildren.evalValue,numberLines,rootChildren.alpha,rootChildren.beta)
		if(not winFlag):
			alphabeta(rootChildren,rootChildren.boardMartix,rootChildren.depth,depth,not maximizingPlayer,opponent,player,numberLines,rootChildren.alpha,rootChildren.beta)
		copyMatrix[x][y]='.'
		if(maximizingPlayer):
			if(rootChildren.evalValue>node.evalValue):
				node.evalValue=rootChildren.evalValue
			if(rootChildren.evalValue>node.alpha):
				if(rootChildren.evalValue>=node.beta):
					cutFlag=True
				else:
					node.alpha=rootChildren.evalValue
					rootChildren.alpha=rootChildren.evalValue
		else:
			if(rootChildren.evalValue<node.evalValue):
				node.evalValue=rootChildren.evalValue
			if(rootChildren.evalValue<node.beta):
				if(rootChildren.evalValue<=node.alpha):
					cutFlag=True
				else:
					node.beta=rootChildren.evalValue
					rootChildren.beta=rootChildren.evalValue
		printAlphaBeta(node.x,node.y,node.depth,node.evalValue,numberLines,node.alpha,node.beta)
		if(node.beta<=node.alpha):
			break
		if(cutFlag):
			break
		winFlag=False

def minimax(inputMatrix,minimaxMatrix,depth,player,numberLines):
	f=open("traverse_log.txt","w")
	f.write("Move,Depth,Value")
	f.write("\n")
	f.close()
	depthValue=0
	root = myTree(inputMatrix,depthValue,0,0,player,numberLines)
	root.evalValue=-99999999
	printCharacters(root.x,root.y,root.depth,root.evalValue,numberLines)
	if (player==1):
		traverse(root,root.boardMartix,root.depth,depth,True,root.player,2,root.numberLines)
	else:
		traverse(root,root.boardMartix,root.depth,depth,True,root.player,1,root.numberLines)
	for c in root.children:
		if(root.evalValue==c.evalValue):
			outputX=c.x
			outputY=c.y
	if(player==1):
		inputMatrix[outputX][outputY]='b'
	else:
		inputMatrix[outputX][outputY]='w'
	f=open("next_state.txt","w")
	for innerList in inputMatrix:
		for element in innerList:
			f.write(element)
		f.write('\n')
	f.close()

def alphabetatask(inputMatrix,minimaxMatrix,depth,player,numberLines):
	f=open("traverse_log.txt","w")
	f.write("Move,Depth,Value,Alpha,Beta")
	f.write("\n")
	f.close()
	depthValue=0
	alpha=-99999999
	beta=99999999
	root = myTree(inputMatrix,depthValue,0,0,player,numberLines)
	root.evalValue=-99999999
	root.alpha=alpha
	root.beta=beta
	printAlphaBeta(root.x,root.y,root.depth,root.evalValue,numberLines,root.alpha,root.beta)
	if (player==1):
		alphabeta(root,root.boardMartix,root.depth,depth,True,root.player,2,root.numberLines,root.alpha,root.beta)
	else:
		alphabeta(root,root.boardMartix,root.depth,depth,True,root.player,1,root.numberLines,root.alpha,root.beta)
	for c in root.children:
		if(root.evalValue==c.evalValue):
			outputX=c.x
			outputY=c.y
	if(player==1):
		inputMatrix[outputX][outputY]='b'
	else:
		inputMatrix[outputX][outputY]='w'
	f=open("next_state.txt","w")
	for innerList in inputMatrix:
		for element in innerList:
			f.write(element)
		f.write('\n')
	f.close()

def main():
	inputFile=open(sys.argv[1],"r")
	#inputFile=open("input_50.txt","r")
	if inputFile.mode=='r':
		inputFileLines=inputFile.readlines()
		inputFileLines = [line.strip() for line in inputFileLines]
		task=int(inputFileLines[0])
		player=int(inputFileLines[1])
		depth=int(inputFileLines[2])
		numberLines=int(inputFileLines[3])

		inputMatrix = []
		for inputIndex in range(4,numberLines+4):
			inputRow= [inputCharacter for inputCharacter in inputFileLines[inputIndex]]
			inputMatrix.append(inputRow)

		neighbourMatrix = []
		for inputIndex in range(numberLines):
			inputRow= [inputCharacter for inputCharacter in inputMatrix[inputIndex]]
			neighbourMatrix.append(inputRow)
		
		neighbourMatrix=findneighbours(inputMatrix,numberLines)
		
		if(task==1):
			greedy(inputMatrix,neighbourMatrix,player,numberLines)
		elif(task==2):
			minimax(inputMatrix,neighbourMatrix,depth,player,numberLines)
		else:
			alphabetatask(inputMatrix,neighbourMatrix,depth,player,numberLines)

if __name__ == '__main__':
	main()