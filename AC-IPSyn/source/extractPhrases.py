#Purpose: Extract phrases from a parse
def extractPhraseLastBracket(parse):
	i=len(parse)
	stack=[]
	for j in range(i-1,-1,-1):
		if parse[j]==')':
			stack.append(')')
		elif parse[j]=='(':
			if len(stack)!=0:
				stack.pop()
			if len(stack)==0:
				#print parse[j:]
				return parse[j:]
	if len(stack) !=0:
		return parse[:i-len(stack)-1]
	return parse
def extractPhraseFirstBracket(parse):
	#print "ExtractFirstBracket:" +parse
	i=len(parse)
	stack=[]
	for j in range(0,i):
		if parse[j]=='(':
			stack.append('(')
		elif parse[j]==')':
			if len(stack) !=0:
				stack.pop()
			if len(stack)==0:
				#print parse[:j+1]
				return parse[:j+1]
	if len(stack) !=0:
		print "Not encountered the end of brackets"	 
	return parse

