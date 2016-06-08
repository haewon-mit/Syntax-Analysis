#Purpose: Find patterns of the form (NN ), (NNS ), (NNP ), (NNPS )
import sys
import string
import re
import os
import extractPhrases
import PorterStemmer
from Patterns_IPSyn import *
#Store the transcript names
FileList={}
#Store the score of each of the IPSyn constructs :0, 1 or 2
Score={}
#Store the actual counts of each of the IPSyn constructs: >=0
RScore={}

#Remove the common plurals for N7
def removeCommonPluralsN7(fileName):
	try:
		#remove plurals that are normally used in plural form
		#clothes, lots, pants
		#Also, we need to look at plurals that have suffixes
		CommonPlurals=["CLOTHES", "LOTS", "PANTS", "SCISSORS","SHORTS", "TROUSERS","TONGS","PLIERS","GLASSES","STAIRS"]
		SecondExamplar=["BLOCKS", "GRAPES", "SHOES"]
		LexicalCriteria=["N1","N2","N3","N4","N5","N6","N7","N8","N9","N10","N11","V1","V2","V8","V10","V11","V14","V17","Q1","Q2","Q4","Q8","Q9","S5","S10"]
		ps=PorterStemmer.PorterStemmer()
		examplesToDelete=[]
		for i in range(len(FileList[fileName]["N7"])):
			if FileList[fileName]["N7"][i][1] in CommonPlurals:
				examplesToDelete.append(FileList[fileName]["N7"][i])
		for i in examplesToDelete:
			FileList[fileName]["N7"].remove(i)
		if len(FileList[fileName]["N7"])==1:
			if FileList[fileName]["N7"][0][1] in SecondExamplar:
				FileList[fileName]["N7"].pop(0)
		for lc in LexicalCriteria:
			l2=[]
			examplesToDelete=[]
			for i in range(len(FileList[fileName][lc])):
				present=False
				for l1 in l2:
					if ps.stem(l1.lower(),0,len(l1)-1)==ps.stem(FileList[fileName][lc][i][1].lower(),0,len(FileList[fileName][lc][i][1].lower())-1):
						present=True
						break
				if present==True:
					examplesToDelete.append(FileList[fileName][lc][i])
				else:
					l2.append(FileList[fileName][lc][i][1])
			FileList[fileName][lc].reverse()
			for l1 in examplesToDelete:
				FileList
				FileList[fileName][lc].remove(l1)
				FileList[fileName][lc].reverse()
	
		return
	except:
		print "Error occured while trying to remove plurals for N7"

#Find the patterns from the given data
def extractPhrase(data,Result_Patterns,generateScoreEntireTranscript,beginingRange,endingRange):
	global Patterns
	Sentence_Result_Patterns={}
	Result_Patterns={}
	#Find all the matches
	data=data.split("\n\n\n\n\n")
	if data[-1].strip("\n")=="":
		data=data[:-1]
	if generateScoreEntireTranscript==True:
		noUtterances=len(data)
	else:
		noUtterances=min(len(data)-beginingRange+1,endingRange-beginingRange+1)
	sentenceNo=beginingRange
	for sentence in data[beginingRange-1:beginingRange+noUtterances-1]:
		for construct in Patterns:
			Sentence_Result_Patterns[construct]=re.findall(Patterns[construct],sentence)
		#Extract all the instances from the structure
		for construct in Sentence_Result_Patterns:
			#Proper, Mass or Count Noun
			if construct=='N1':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])) for v in Sentence_Result_Patterns[construct]]
			#Pronoun, prolocative excluding modifiers
			elif construct=='N2':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in Sentence_Result_Patterns[construct]]
			#Modifier including adjectives,possessives and quantifiers
			elif construct=='N3':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])) for v in Sentence_Result_Patterns[construct]]
			#Two word NP preceded by article or modifier
			elif construct=='N4':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])+" " +string.upper(v[4])) for v in Sentence_Result_Patterns[construct]]
			#Article used before a noun
			elif construct=='N5':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in Sentence_Result_Patterns[construct]]
			#Two word NP(as in N4) after verb or preposition
			elif construct=='N6':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in Sentence_Result_Patterns[construct]]
			#Plural suffix
			elif construct=='N7':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])) for v in Sentence_Result_Patterns[construct]]
			#Two word NP(as in N4 before verb)
			elif construct=='N8':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])+ " "+ string.upper(v[4])) for v in  Sentence_Result_Patterns[construct]]
			#Three word NP (Det-Mod-N or Mod-Mod-N)
			elif construct=='N9':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Adverb modifying adjective or nominal
			#The adverb can be a pre-modifier or a post-modifier	
			elif construct=='N10':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					if v[3]!='':
						l.append((sentenceNo,string.upper(v[3])))
					elif v[10]!='':
						l.append((sentenceNo,string.upper(v[10])))
					elif v[12]!='':
						l.append((sentenceNo,string.upper(v[12])))
				Sentence_Result_Patterns[construct]=l
			#Right now am just considering adjectives and especially the 
			#comparative and superlative form that end with er and est	
			#Any other bound morpheme on N or adjective(if judged not to be stored as lexical unit
			elif construct=='N11':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			elif construct=='N12':
				Sentence_Result_Patterns[construct]=[]
			#Verb
			elif construct=='V1':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])) for v in  Sentence_Result_Patterns[construct]]
			#Particle or preposition
			elif construct=='V2':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Prepositional Phrase (Prep+NP)
			#Modify to look for the end of the prepositional phrase
			elif construct=='V3':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Copula linking two nominals (nominal + copula + nominal, copula)
			elif construct=='V4':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Catenative (pseudo-auxiliary) preceeding a verb (catenative,verb)
			elif construct=='V5':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[0])) for v in  Sentence_Result_Patterns[construct]]
			#Auxiliary be, do, have in VP
			elif construct=='V6':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Progressive Suffix
			elif construct=='V7':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(v[2])) for v in  Sentence_Result_Patterns[construct]]
			#Adverb
			elif construct=='V8':
				 Sentence_Result_Patterns[construct]=[(sentenceNo, string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Modal preceeding verb
			elif construct=='V9':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					l.append((sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))))
				Sentence_Result_Patterns[construct]=l
			#Third person singular prefix
			elif construct=='V10':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Past tense modal
			elif construct=='V11':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Regular past tense suffix
			elif construct=='V12':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Past tense auxiliary
			elif construct=='V13':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Medial Adverb
			elif construct=='V14':
				adverbList=[]
				for i in  Sentence_Result_Patterns[construct]:
					r=re.sub(r'((?!\(NP \(PDT)\([A-Z$.,]+ (?=\())|( \(\. .\))|(\){1,}(?=\)))','',i[0]).split(") (")
					for j in range(1,len(r)-1):
						a=r[j].rstrip('(').lstrip(')')
						if a.find("RB ")==0:
							b=string.upper(r[j].split("RB ")[1])
							adverbList.append((sentenceNo,b))
						elif a.find("WRB")==0:
							b=string.upper(r[j].split("WRB ")[1])
							adverbList.append((sentenceNo,b))
						elif a.find("NP (PDT")==0:
							b=string.upper(r[j].split("NP (PDT ")[1])
							adverbList.append((sentenceNo,b))
				Sentence_Result_Patterns[construct]=adverbList
			#Copula, Modal or Auxiliary used for emphasis or ellipsis(uncontractible context)
			elif construct=='V15':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Past tense copula
			elif construct=='V16':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$,:]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			# Bound morpheme on a verb or an adjective(to make an adverb) Tag,Word
			elif construct=='V17':
				l=[]
				for i in  Sentence_Result_Patterns[construct]:
					if i[3].upper() in l:
						continue
					if i[3][-2:]=="ly":
						s=file("source/s","w")
						s.write(i[3][:-2].lower()+"\n")
						s.write(i[3][:-2].lower()+"y\n")
						s.write(i[3][:-2].lower()+"e\n")
						s.write(i[3][:-1].lower()+"\n")
						s.write(i[3][:-2].lower()+"le\n")
						s.write(i[3][:-4].lower())
						s.close()
						print "using tree-tagger"
						os.system("./TreeTagger/bin/tree-tagger ./TreeTagger/english-par-linux-3.1.bin -lemma  -token source/s source/a1")
						data=file("source/a1").read().split()
						j=0
						while (j <= len(data)-3):
							if data[j+1]=="JJ" and data[j+2]!="<unknown>":
								l.append((sentenceNo,string.upper(i[3])))
								break
							j+=3
					else:
						s=file("source/s","w")
						s.write(i[3][2:].lower()+"\n")
						s.close()
						print "using tree-tagger"
						os.system("./TreeTagger/bin/tree-tagger ./TreeTagger/english-par-linux-3.1.bin -lemma  -token source/s source/a1")
						data=file("source/a1").read().split()
						if data[1][:2]=="VV" and data[2]!="<unknown>":
							l.append((sentenceNo,string.upper(i[3])))
				Sentence_Result_Patterns[construct]= l
			#Intonationally marked question
			elif construct=='Q1':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Routine do/go existence name question or wh-pronoun alone
			elif construct=='Q2':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Simple Negation +X ) neg=no(t), can't don't X=NP,PP,VP,Adj, Adv etc
			elif construct=='Q3':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Initial Wh-pronoun followed by verb
			elif construct=='Q4':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Negative Morpheme between subject and verb
			elif construct=='Q5':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					VP=extractPhrases.extractPhraseFirstBracket(v[3])
					l.append((sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",VP))))
				Sentence_Result_Patterns[construct]=l
			# Wh-question with inverted modal, copula or auxillary
			elif construct=='Q6':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Negation of copula, modal or auxiliary
			elif construct=='Q7':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					vp= re.sub(r'([A-Z$,:1-9. ]+ )|\)|\(',"",extractPhrases.extractPhraseFirstBracket(v[1]))
					l.append((sentenceNo,string.upper(vp)))
				Sentence_Result_Patterns[construct]=l
			#Yes/no question with inverted modal, copula or auxiliary
			elif construct=='Q8':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Why, When, Which, Whose
			elif construct=='Q9':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Tag Question
			elif construct=='Q10':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					len_tag=len((re.sub(r'([A-Z$,: ]+ )|\)|\(',"",v[1])).rstrip().split())
					tag=string.upper(re.sub(r'([A-Z$,: ]+ )|\)|\(',"",v[6])).rstrip()
					if len(tag.split())<=4 and len_tag>=3 and (tag.rfind("RIGHT")==0 or tag.rfind("ALL RIGHT")==0 or tag.rfind("OKAY")==0 or tag.rfind("HMM")==0 or tag.rfind("eh")==0 or tag.rfind("HUH")==0 or tag.rfind("OK")==0):
						l.append((sentenceNo,tag))
					else:
						if len_tag >=3:
							prp_list=re.findall(r'^\(VP \(((AUX)|(MD)) [^)]+\) (\(RB ((not)|(n\'t)|(\'nt))\)+ )?(\(S )?\(NP \(PRP [^)]+\)+(( \(NP )?\(NN.? [^)]+\)+)? *($|(\(, ,\)))',v[6])
							for a in prp_list:
								l.append((sentenceNo,tag))
				Sentence_Result_Patterns[construct]=l
			#Other: e.g questions with negation and inverted cop/aux/modal
			elif construct=='Q11':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					p=string.rfind(v[1],v[9])
					for i in range(p-1,-1,-1):
						if v[1][i]=='(':
							VP=extractPhrases.extractPhraseFirstBracket(v[1][i:])
							s=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",VP))
							l.append((sentenceNo,s))
							break
				Sentence_Result_Patterns[construct]=l
			#Two word combination
			elif construct=='S1':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					a=string.upper(string.rstrip(re.sub(r'([A-Z1-9$.,:]+ )|\)|\(|[.,:-;!?]',"",v[0]))).split()
					if len(a)>=2:	
						l.append((sentenceNo," ".join(a)))
				Sentence_Result_Patterns[construct]=l
			#Subject verb sequence
			elif construct=='S2':
				subjectVerbList=[]
				for i in  Sentence_Result_Patterns[construct]:
					np=extractPhrases.extractPhraseFirstBracket(i[1])
					vp=extractPhrases.extractPhraseFirstBracket(i[1][len(np)+1:])
					#Is a verb phrase following the noun phrase
					if vp.find("(VP")==0:
						npPosition=vp.find("(NP")
						adjpPosition=vp.find("(ADJP")
						ppPosition=vp.find("(PP")
						sbarPosition=vp.find("SBAR")
						setsPosition=set([npPosition,adjpPosition,ppPosition,sbarPosition])
						if -1 in setsPosition:
							setsPosition.remove(-1)
						if len(setsPosition)==0:
							minPosition=-1
						else:	
							setsPosition=[v for v in setsPosition]
							minPosition=min(setsPosition)
						if minPosition == -1:
							minPosition=len(vp)
						b=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",np+" "+vp[:minPosition]))
						subjectVerbList.append((sentenceNo,b))
					a=vp.find("(S (NP")
					while (a!=-1):
						np=extractPhrases.extractPhraseFirstBracket(vp[a+3:])
						vp=extractPhrases.extractPhraseFirstBracket(vp[a+3+len(np)+1:])
						if vp.find("(VP")==0:
							npPosition=vp.find("(NP")
							adjpPosition=vp.find("(ADJP")
							ppPosition=vp.find("(PP")
							sbarPosition=vp.find("SBAR")
							setsPosition=set([npPosition,adjpPosition,ppPosition,sbarPosition])
							if -1 in setsPosition:
								setsPosition.remove(-1)
							if len(setsPosition)==0:
								minPosition=-1
							else:	
								setsPosition=[v for v in setsPosition]
								minPosition=min(setsPosition)
							if minPosition == -1:
								minPosition=len(vp)
							b=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",np+" "+vp[:minPosition]))
							subjectVerbList.append((sentenceNo,b))
						vp=vp[a+3:]
						a=vp.find("(S (NP")
				Sentence_Result_Patterns[construct]=subjectVerbList
			#Verb object sequence
			elif construct=='S3':
				subjectVerbList=[]
				for i in  Sentence_Result_Patterns[construct]:
					vp=extractPhrases.extractPhraseFirstBracket(i[1])
					#Is a verb phrase following the noun phrase
					if vp.find("(VP")==0:
						if not(vp.find("(NP")==-1 and vp.find("(ADJP")==-1):
							b=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",vp))
							subjectVerbList.append((sentenceNo,b))
					vp=vp[3:]
					a=vp.find("(VP")
					while (a!=-1):
						vp=extractPhrases.extractPhraseFirstBracket(vp[a:])
						if not(vp.find(") (NP")==-1 and vp.find("(ADJP")==-1):
							b=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",vp))
							subjectVerbList.append((sentenceNo,b))
						vp=vp[a+3:]
						a=vp.find("(VP")
				Sentence_Result_Patterns[construct]=subjectVerbList
			#Subject Verb Object Sequence
			elif construct=='S4':
				subjectVerbList=[]
				for i in  Sentence_Result_Patterns[construct]:
					np=extractPhrases.extractPhraseFirstBracket(i[1])
					vp=extractPhrases.extractPhraseFirstBracket(i[1][len(np)+1:])
					#Is a verb phrase following the noun phrase
					if vp.find("(VP")==0:
						if not(vp.find("(NP")==-1 and vp.find("(ADJP")==-1):
							b=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",np+" "+vp))
							subjectVerbList.append((sentenceNo,b))
					a=vp.find("(S (NP")
					while (a!=-1):
						np=extractPhrases.extractPhraseFirstBracket(vp[a+3:])
						vp=extractPhrases.extractPhraseFirstBracket(vp[a+3+len(np)+1:])
						if vp.find("(VP")==0:
							if not(vp.find("(NP")==-1 and vp.find("(ADJP")==-1):
								b=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",np+" "+vp))
								subjectVerbList.append((sentenceNo,b))
						vp=vp[a+3:]
						a=vp.find("(S (NP")
				Sentence_Result_Patterns[construct]=subjectVerbList
			#Conjunction (any)
			elif construct=='S5':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					sent=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))
					if not v[8]=='':
						conj=string.upper(re.sub(r'([A-Z$1-9., ]+ )|\)|\(',"",v[8]))
					else:
						conj=string.upper(v[7])
						if string.find(sent,"AS SOON AS")!=-1:
							conj="AS SOON AS"
						elif conj == "IF":
							if string.find(sent,"THEN") !=-1:
								conj="IF..THEN"
					l.append((sentenceNo,conj))
				Sentence_Result_Patterns[construct]=l
			#Sentence with two VP's
			elif construct=='S6':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Conjoined phrases
			elif construct=='S7':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",v[2]))) for v in  Sentence_Result_Patterns[construct]]
			#Infinitive without catenative, marked with to
			elif construct=='S8':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",extractPhrases.extractPhraseFirstBracket(c[2])))) for c in  Sentence_Result_Patterns[construct]]
			# Let/Make/Help/Watch introducer
			elif construct=='S9':
				 Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			# Adverbial Conjunction
			elif construct=='S10':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					sent=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[0]))
					if not v[8]=='':
						conj=string.upper(re.sub(r'([A-Z$1-9.,: ]+ )|\)|\(',"",v[8]))
					else:
						conj=string.upper(v[7])
						if conj in ["AND","OR","THEN"]:
							continue
						elif string.find(sent,"AS SOON AS")!=-1:
							conj="AS SOON AS"
						elif conj == "IF":
							if string.find(sent,"THEN") !=-1:
								conj="IF..THEN"
					l.append((sentenceNo,conj))
				Sentence_Result_Patterns[construct]=l
			# Propositional Complement
			elif construct=='S11':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					vp=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",extractPhrases.extractPhraseFirstBracket(v[18])))
					s=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",v[0])+ " , "+ vp+"\n")
					l.append((sentenceNo,vp))
				Sentence_Result_Patterns[construct]=l
			# Conjoined sentences (Except for imperatives, will usually have subj + predicate in each clause
			elif construct=='S12':
				l=[]
				for v in  Sentence_Result_Patterns[construct]:
					beforeConj=extractPhrases.extractPhraseLastBracket(v[10])
					afterConj=extractPhrases.extractPhraseLastBracket(v[22])
					subjPredicatePattern=r'\(NP.*\(VP.*'
					impPattern=r'.*\(VP \((VB|AUX) .*'
					bcList_subjPred=re.findall(subjPredicatePattern,beforeConj)
					acList_subjPred=re.findall(subjPredicatePattern,afterConj)
					bcList_imp=re.findall(impPattern,beforeConj)
					acList_imp=re.findall(impPattern,afterConj)
					if (len(bcList_subjPred)!=0 or len(bcList_imp) !=0) and (len(acList_subjPred)!=0 or len(acList_imp)!=0):
						l.append((sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",v[1]))))
				Sentence_Result_Patterns[construct]=l
			# Wh-Clause
			elif construct=='S13':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",v[0]))) for v in  Sentence_Result_Patterns[construct]]
			#Bitransitive predicate
			elif construct=='S14':
				l=[]
				for v in Sentence_Result_Patterns[construct]:
					vp=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",extractPhrases.extractPhraseFirstBracket(v[1])))
					s=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",v[0])+ " , "+ vp+"\n")
					l.append((sentenceNo,vp))
				Sentence_Result_Patterns[construct]=l	
			# Sentence with three or more VPs
			elif construct=='S15':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",v[0]))) for v in Sentence_Result_Patterns[construct]]
			# Relative clause marked or unmarked
			elif construct=='S16':
				l=[]
				for v in Sentence_Result_Patterns[construct]:
					sbar_begins=string.find(v[1],v[2])
					sbar=extractPhrases.extractPhraseFirstBracket(v[2])
					sbar_ends=sbar_begins+len(sbar)-1
					if string.find(extractPhrases.extractPhraseLastBracket(v[1][:sbar_ends+2]),"(NP")==0:
						l.append((sentenceNo,string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",extractPhrases.extractPhraseLastBracket(v[1][:sbar_ends+2])))))
				Sentence_Result_Patterns[construct]=l
			#Infinitive clause new subject
			elif construct=='S17':
				l=[]
				for v in Sentence_Result_Patterns[construct]:
					vp=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",extractPhrases.extractPhraseFirstBracket(v[2])))
					s=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",v[0])+ " , "+ vp+"\n")
					l.append((sentenceNo,vp))
				Sentence_Result_Patterns[construct]=l
			#Gerund
			elif construct=='S18':
				Sentence_Result_Patterns[construct]=[(sentenceNo,string.upper(re.sub(r'([A-Z$1-9.,?: ]+ )|\)|\(',"",v[0]))) for v in Sentence_Result_Patterns[construct]]
			# Fronted or center-embedded subordinate clause	
			elif construct=='S19':
				l=[]
				for v in Sentence_Result_Patterns[construct]:
					v_str=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",v[0]))
					i=len(v[2])
					stack=[]
					for j in range(i):
						if v[2][j]=='(':
							stack.append('(')
						elif v[2][j]==')':
							if len(stack)!=0:
								stack.pop()
							if len(stack)==0:
								so_str=string.upper(re.sub(r'([A-Z1-9$.,: ]+ )|\)|\(',"",v[2][:j+1]))		
								start_pos=string.find(v_str,so_str)
								if start_pos<=len(v_str)/2 and start_pos+len(so_str)<len(v_str)*5/6:
									l.append((sentenceNo,so_str))
								break
				Sentence_Result_Patterns[construct]=l				
			#Other: e.g passive constructions e.g tag comments/intrusions
			elif construct=='S20':
				Sentence_Result_Patterns[construct]=[]
			if construct not in Result_Patterns:
				Result_Patterns[construct]=[]
			for a in Sentence_Result_Patterns[construct]:
				Result_Patterns[construct].append(a)
		sentenceNo=sentenceNo+1
		#Generate the IPSyn score on a select no of utterances
		if sentenceNo>(beginingRange+noUtterances):
			break
	#Construct a unique list of the instances	
	for construct in Result_Patterns:
		Result_Patterns[construct]=list(set(Result_Patterns[construct]))
	return Result_Patterns, noUtterances
#Function to find the patterns
def findPatterns(inputFile,generateScoreEntireTranscript,beginingRange,endingRange):
	global FileList
	print inputFile.split("/")[-1].split(".")[0]
	data=file(inputFile).read()
	new_data=data.split("\n\n\n\n\n")
	if new_data[-1].strip("\n")=="":
		new_data=new_data[:-1]
	#Check that the range is fine
	if generateScoreEntireTranscript==False and beginingRange>len(new_data):
		print "Begining range given exceeds the number of child utterances in the transcript. Not processing transcript.."
		return 0
	Results_Patterns={}
	Results_Patterns,utterancesConsidered=extractPhrase(data,Results_Patterns,generateScoreEntireTranscript,beginingRange,endingRange)
	FileList[inputFile]=Results_Patterns
	return utterancesConsidered
def getFilteredList(constructList):
	filteredL=[]
	examplesToDelete=[]
	for e2 in constructList:
		#If the construct is not a string
		if type(e2[1]) != type(""):
			present=True
			break
		e1=e2[1].split()
		lene1=len(e1)
		#For those constructs that have empty strings
		if lene1==0:
			present=True
			break
		present=False
		for (sNo,l1) in filteredL:
			common=0
			if l1==e2[1]:
				present=True
				break
			l2=l1.split()
			lenl2=len(l2)
			for i in range(min(lene1, lenl2)):
				if l2[i]==e1[i]:
					common+=1
				if lene1==lenl2:
					if common>(lene1/2.0):
						present=True
						break
				elif lene1>lenl2:
					if common>(lenl2/2.0)+lene1-lenl2:
						present=True
						break
				else:
					if common+lenl2-lene1>(lene1/2.0):
						present=True
						break	
		if present==False:
			filteredL.append(e2)
	return filteredL
#Function to score the transcripts
def scoreTranscripts(fileName):
	global FileList
	global Score
	score=0
	rscore=0
	nounTotal=0
	rnounTotal=0
	verbTotal=0
	rverbTotal=0
	questionTotal=0
	rquestionTotal=0
	sentenceTotal=0
	rsentenceTotal=0
	c={}
	rc={}

	#Score the noun constructs
	for construct in Nouns:
		e=FileList[fileName][construct]
		if len(e)==0:
			c[construct]=0
			rc[construct]=0
			continue
		filteredL=getFilteredList(e)
#		filteredL=e
		#Increment the score by zero
		if len(filteredL)==0:
			c[construct]=0
		#Increment the score by 1
		elif len(filteredL)==1:
			c[construct]=1
			score=score+1
		#Incremement the score by 2
		elif len(filteredL)>=2:
			c[construct]=2
			score=score+2
		rc[construct]=len(filteredL)
		rscore+=rc[construct]
		rnounTotal+=rc[construct]
		nounTotal+=c[construct]

	#Score the verb constructs
	for construct in Verbs:
		e=FileList[fileName][construct]
		if len(e)==0:
			c[construct]=0
			rc[construct]=0
			continue
		filteredL=getFilteredList(e)
#		filteredL=e
		#Increment the score by zero
		if len(filteredL)==0:
			c[construct]=0
		#Increment the score by 1
		elif len(filteredL)==1:
			c[construct]=1
			score=score+1
		#Incremement the score by 2
		elif len(filteredL)>=2:
			c[construct]=2
			score=score+2
		rc[construct]=len(filteredL)
		rscore+=rc[construct]
		rverbTotal+=rc[construct]
		verbTotal+=c[construct]

	#Score the question constructs
	for construct in Questions:
		e=FileList[fileName][construct]
		if len(e)==0:
			c[construct]=0
			rc[construct]=0
			continue
		filteredL=getFilteredList(e)
		#filteredL=e
		#Increment the score by zero
		if len(filteredL)==0:
			c[construct]=0
		#Increment the score by 1
		elif len(filteredL)==1:
			c[construct]=1
			score=score+1
		#Incremement the score by 2
		elif len(filteredL)>=2:
			c[construct]=2
			score=score+2
		rc[construct]=len(filteredL)
		rscore+=rc[construct]
		rquestionTotal+=rc[construct]
		questionTotal+=c[construct]

	#Score the sentence constructs
	for construct in Sentences:
		e=FileList[fileName][construct]
		if len(e)==0:
			c[construct]=0
			rc[construct]=0
			continue
		filteredL=getFilteredList(e)
		#filteredL=e
		#Increment the score by zero
		if len(filteredL)==0:
			c[construct]=0
		#Increment the score by 1
		elif len(filteredL)==1:
			c[construct]=1
			score=score+1
		#Incremement the score by 2
		elif len(filteredL)>=2:
			c[construct]=2
			score=score+2
		rc[construct]=len(filteredL)
		rscore+=rc[construct]
		rsentenceTotal+=rc[construct]
		sentenceTotal+=c[construct]
	#Child earns 2 points on Q1 and Q2 if they earn two points on items in Q4 and/or Q8
	score=score-c["Q1"]-c["Q2"]
	questionTotal=questionTotal-c["Q1"]-c["Q2"]
	maxScore=max(c["Q4"],c["Q8"],min(2,c["Q4"]+c["Q8"]))
	if c["Q1"]<maxScore:
		c["Q1"]=maxScore
	if c["Q2"]<maxScore:
		c["Q2"]=maxScore
	questionTotal=questionTotal+c["Q1"]+c["Q2"]
	score=score+c["Q1"]+c["Q2"]
	
	score=score-c["V5"]
	verbTotal=verbTotal-c["V5"]
	if c["V5"]<2:
		c["V5"]=min(c["V5"]+c["V6"],2)
	if c["V5"]<2:
		c["V5"]=min(c["V5"]+c["V9"],2)
	score=score+c["V5"]
	verbTotal=verbTotal+c["V5"]
	
	c['NTOTAL']=nounTotal
	c['VTOTAL']=verbTotal
	c['QTOTAL']=questionTotal
	c['STOTAL']=sentenceTotal
	c['TOTAL']=score
	rc['NTOTAL']=rnounTotal
	rc['VTOTAL']=rverbTotal
	rc['QTOTAL']=rquestionTotal
	rc['STOTAL']=rsentenceTotal
	rc['TOTAL']=rscore
	Score[fileName]=c
	RScore[fileName]=rc	

#This function generates the IPSyn files for a directory
def generateIPSynScores(parseDir,outputDir,rawDir,generateScoreEntireTranscript,beginingRange,endingRange):
	global FileList
	try:
		print "Computing IPSyn score"
		#Sort the input files
		file_list=sorted(os.listdir(parseDir))

		for i in range(len(file_list)):
			parsed_file=file_list[i]
			if ".bak" in parsed_file:
				continue
			fileName=parseDir+"/"+parsed_file
			noUtterancesConsidered=findPatterns(fileName,generateScoreEntireTranscript,beginingRange,endingRange)
			#Range given which lies outside the number of utterances
			if noUtterancesConsidered==0:
				continue
			removeCommonPluralsN7(fileName)
			scoreTranscripts(fileName)
			#All output files have the extension IPS
			outputFile=file(outputDir+"/"+parsed_file.split(".")[0]+".IPS","w")
			#All files with the raw count have the extension RAW
			rawFile=file(rawDir+"/"+parsed_file.split(".")[0]+".RAW","w")
			if generateScoreEntireTranscript==True:
				beginingRange=1
				endingRange=noUtterancesConsidered
			#Write the IPSyn results
			writeOutputRawFile(fileName,outputFile,rawFile,noUtterancesConsidered,beginingRange,endingRange)
			inputFile=file(parseDir+"/"+parsed_file)
			#Add a sentence listing to the end of the file
			writeSentenceListing(inputFile,outputFile,rawFile)
			#Add a sentence listing to the end of the file
			inputFile.close()
			outputFile.close()
			rawFile.close()
	except:
		print "Error occured when generating IPSyn"

#This function writes the output files
def writeOutputRawFile(fileName,outputFile,rawFile,noUtterancesConsidered,beginingRange,endingRange):
	global FileList
	global Score
	strippedFileName=""
	#Extract only the file name
	if "/" in fileName:
		strippedName=fileName.split("/")[-1].split(".")[0]
	else:
		strippedName=fileName.split(".")[0]
	outputFile.write("FILENAME:"+strippedName+"\n\n")
	rawFile.write("FILENAME:"+strippedName+"\n\n")
	for c in Nouns:
		outputFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		rawFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		for (lineNo,examplar) in sorted(FileList[fileName][c]):
			outputFile.write(str(lineNo)+"\t"+examplar+"\n")
			rawFile.write(str(lineNo)+"\t"+examplar+"\n")
		outputFile.write("\nSCORE:\t"+str(Score[fileName][c])+"\n\n")
		rawFile.write("\nCOUNTS:\t"+str(RScore[fileName][c])+"\n\n")

	for c in Verbs:
		outputFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		rawFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		for (lineNo,examplar) in sorted(FileList[fileName][c]):
			outputFile.write(str(lineNo)+"\t"+examplar+"\n")
			rawFile.write(str(lineNo)+"\t"+examplar+"\n")
		outputFile.write("\nSCORE:\t"+str(Score[fileName][c])+"\n\n")
		rawFile.write("\nCOUNTS:\t"+str(RScore[fileName][c])+"\n\n")
	for c in Questions:
		outputFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		rawFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		for (lineNo,examplar) in sorted(FileList[fileName][c]):
			outputFile.write(str(lineNo)+"\t"+examplar+"\n")
			rawFile.write(str(lineNo)+"\t"+examplar+"\n")
		outputFile.write("\nSCORE:\t"+str(Score[fileName][c])+"\n\n")
		rawFile.write("\nCOUNTS:\t"+str(RScore[fileName][c])+"\n\n")
	for c in Sentences:
		outputFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		rawFile.write("\n###"+c+"\t"+Description[c]+"###\n\n")
		for (lineNo,examplar) in sorted(FileList[fileName][c]):
			outputFile.write(str(lineNo)+"\t"+examplar+"\n")
			rawFile.write(str(lineNo)+"\t"+examplar+"\n")
		outputFile.write("\nSCORE:\t"+str(Score[fileName][c])+"\n\n")
		rawFile.write("\nCOUNTS:\t"+str(RScore[fileName][c])+"\n\n")
	try:
		outputFile.write("RANGE OF UTTERANCES GIVEN: "+str(beginingRange)+ "-"+str(endingRange)+"\n")
		outputFile.write("NO OF UTTERANCES CONSIDERED: "+str(noUtterancesConsidered)+"\n")
		outputFile.write("\n\n#########################\nNOUN SCORE: "+str(Score[fileName]["NTOTAL"])+"\n")
		outputFile.write("VERB SCORE: "+str(Score[fileName]["VTOTAL"])+"\n")
		outputFile.write("QUESTION SCORE: "+str(Score[fileName]["QTOTAL"])+"\n")
		outputFile.write("SENTENCE SCORE: "+str(Score[fileName]["STOTAL"])+"\n")
		outputFile.write("IPSYN SCORE: "+str(Score[fileName]["TOTAL"])+"\n##########################\n")
	except:
		print "Error occured while writing the IPS results file"
	try:
		#Write the counts into the raw file
		rawFile.write("RANGE OF UTTERANCES GIVEN: "+str(beginingRange)+ "-"+str(endingRange)+"\n")
		rawFile.write("NO OF UTTERANCES CONSIDERED: "+str(noUtterancesConsidered)+"\n")
		rawFile.write("\n\n#########################\nNOUN COUNTS: "+str(RScore[fileName]["NTOTAL"])+"\n")
		rawFile.write("VERB COUNTS: "+str(RScore[fileName]["VTOTAL"])+"\n")
		rawFile.write("QUESTION COUNTS: "+str(RScore[fileName]["QTOTAL"])+"\n")
		rawFile.write("SENTENCE COUNTS: "+str(RScore[fileName]["STOTAL"])+"\n")
		rawFile.write("TOTAL NO OF STRUCTURES COUNTS: "+str(RScore[fileName]["TOTAL"])+"\n##########################\n")
	except:
		print "Error occured while writing the RAW counts file"

#This function prints the sentence listing to the end of the file for easy reference (CP format)
def writeSentenceListing(inputFile,outputFile,rawFile):
	try:
		data=inputFile.read().split("\n\n\n\n\n")
		sentenceNo=1
		outputFile.write("\n###Sentence Listing###\n\n")
		rawFile.write("\n###Sentence Listing###\n\n")
		for sentence in data:
			sentence.rstrip("\n")
			sentence.lstrip("\n")
			lineToBeWritten=str(sentenceNo)+"\t"+string.upper(re.sub(r'([A-Z$,.:1-9]+ )|\)|\(|\n',"",sentence))+"\n"
			outputFile.write(lineToBeWritten)
			rawFile.write(lineToBeWritten)
			
			sentenceNo+=1
	except:
		print "Error occured while writing sentence listing."			
