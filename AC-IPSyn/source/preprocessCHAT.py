#Purpose: Clean up CHAT transcripts
import sys
import re
import os
#Patterns to remove markup from the CHAT transcripts
#Remove Overlap Precedes (square brackets)
#Remove everything within square braces - used for multiple purposes
squareBracesPattern=r'(\[.*?\])'
#Remove everything within round braces (denote pauses)
roundBracesPattern=r'( ?\(+.*?\)+)'
#Remove special form markers
specialFormMarkerPattern=r'(@[a-zA-Z][a-zA-Z]*[:]?[a-zA-Z]*(?=[.,! \n]))'
#Remove <: abandoned utterance or overlapping speech<>
abandonedUtterancePattern=r'(\<)'
#Remove >:<>:overlapping speech
overlappingSpeechPattern=r'(\>)'
#Remove Carriage Return if the file is a windows file being processed on a UNIX machine
carriageReturnPattern=r'(\r)'
#Missing word or part of speech starts with 0
missingWordPOSPattern=r'((?<=[ \t])0([a-z]+)?(?=[ .!?]))'
#Special utterances patterns
#Trailing off +... (remove symbol)
#Self completion +, (remove +,)
#Quick uptake +^ (remove +^)
#Lazy overlap +< (remove symbol) (remove +<)
#Other completion (remove ++)
special1UtterancesPattern=r'(\+((\.\.)|(,)|(\^)|(\<)|(\+)))'
#Trailing off of a question +..? (remove +..)
#Questions with exclamation +!? (remove +!)
special2UtterancesPattern=r'(\+(([\.]+)|(\!))(?=\?))'
#Remove words that start with & - denotes disfluencies
#Phonological form of an incomplete or unintelligible phonological string e.g &guga, phonological fragments, nonce and nonsense forms, simple events
disfluenciesPattern=r'(&.*? )'
#Remove unintelligible words in the middle of sentence
unintelligibleWordsPattern=r'(([ ]|^)[xX]+(?=[ \.\?\,]))'
#Remove unintelligible words at the begining of a sentence
unintelligibleBeginingPattern=r'(\n *[xX]+[ \.\?!]+)'
#Joint words
jointWordsPattern=r'((?<=[a-zA-Z])\+(?=[a-zA-Z]))'
#Remove 0 from transcripts - Empty utterances
zeroPattern=r'(\n0[ ]*\.(?=\n))'
#Pause pattern - # or for prefix
pausePattern=r'(#[ ]*)'
#Interruption pattern
interruptionPattern=r'([ ]+\+\/[ ]*(?=\.))'
#Rest pattern
restPattern=r'[:\-]'
#Quotation precedes +" (remove + and add quotes at the begining or end of the utterance as required)
quotationPrecedesPattern=r'((?<=\n)[ ]*\+")'
#Quotation follows +"/ (remove +"/) since it won't add information for us
quotationFollowsPattern=r'([ ]+\+"\/[ ]*(?=\.))'
#Remove the Other-completion pattern

squareBP=re.compile(squareBracesPattern)
roundBP=re.compile(roundBracesPattern)
specialFormMarkerP=re.compile(specialFormMarkerPattern)
carriageReturnP=re.compile(carriageReturnPattern)
abandonedUtteranceP=re.compile(abandonedUtterancePattern)
overlappingSpeechP=re.compile(overlappingSpeechPattern)
missingWordPOSP=re.compile(missingWordPOSPattern)
special1UtterancesP=re.compile(special1UtterancesPattern)
special2UtterancesP=re.compile(special2UtterancesPattern)
disfluenciesP=re.compile(disfluenciesPattern)
unintelligibleWordsP=re.compile(unintelligibleWordsPattern)
unintelligibleBeginingP=re.compile(unintelligibleBeginingPattern)
jointWordsP=re.compile(jointWordsPattern)
zeroP=re.compile(zeroPattern)
pauseP=re.compile(pausePattern)
interruptionP=re.compile(interruptionPattern)
restP=re.compile(restPattern)
quotationFollowsP=re.compile(quotationFollowsPattern)
quotationPrecedesP=re.compile(quotationPrecedesPattern)

#Preprocess a given file to remove markup from the transcripts
def cleanFile(inputFile,outputDirPrefix="",childPrefix=""):
	try:
		#Patterns to remove markup from the SALT transcripts
		#Remove the subject prefix at the begining of every sentence
		#CHAT transcripts have actual speech starting with *
		subjectPrefixPattern=r'(\n\*'+childPrefix+':[ \t]\s*)'
		#Remove the subject prefix at the begining of the transcript
		beginingSubjectPattern=r'(^\*'+childPrefix+':[ \t]\s*)'
	
		subjectPrefixP=re.compile(subjectPrefixPattern)
		beginingSubjectP=re.compile(beginingSubjectPattern)
		print inputFile.split("/")[-1].split(".")[0]
		data=file(inputFile).read().split("\n")
		new_data=[]
		#Chat manual specifies that utterances coded on more than one line must be preceded by a tab
		previousChild=False
		for a in data:
			#Extract the utterances for the child prefix
			if a.find("*"+childPrefix) == 0:
				new_data.append(a)
				previousChild=True
			#The sentence has been split and so join the sentences
			elif a.find("\t")==0 and previousChild==True:
				new_data[-1]=new_data[-1]+" "+a[1:]
			else:
				previousChild=False
		#Only contains the child's utterances
		data="\n".join(new_data)
		#Remove carriage return
		data=carriageReturnP.sub("",data)
		#Remove all the square braces (Codes)
		data=squareBP.sub("",data)
		#Remove all the round braces (Pauses)
		data=roundBP.sub("",data)
		#Remove all the special form markers
		data=specialFormMarkerP.sub("",data)
		#Remove the overlapping speech symbol
		data=overlappingSpeechP.sub("",data)
		#Remove the abandoned utterance speech symbol
		data=abandonedUtteranceP.sub("",data)
		#Remove the missing word or POS symbol (starts with 0)
		data=missingWordPOSP.sub("",data)
		#Remove the special utterances
		data=special1UtterancesP.sub("",data)
		#Remove the special utterances
		data=special2UtterancesP.sub("",data)
		#Remove the subject prefix
		data=subjectPrefixP.sub("\n",data)
		#Remove the subject prefix at the begining of the file
		data=beginingSubjectP.sub("",data)
		#Remove the disfluencies that start with &
		data=disfluenciesP.sub("",data)
		#Remove the unintelligible words since we do not want them counted by IPSyn
		data=unintelligibleWordsP.sub("",data)
		#Remove the unintelligible words at the begining of a sentence
		data=unintelligibleBeginingP.sub("\n",data)
		#Split the words
		data=jointWordsP.sub(" ",data)
		#Remove the child's utterances that only has zero
		data=zeroP.sub("",data)
		#Remove the # pattern
		data=pauseP.sub("",data)
		#Remove the interruption pattern +/
		data=interruptionP.sub("",data)
		#Remove the quotation follows pattern +/"
		data=quotationFollowsP.sub("",data)
		#Remove the quotation precedes pattern +"
		data=quotationPrecedesP.sub("",data)
		#Remove the hyphen and semicolon
		data=restP.sub("",data)

		#print data
		#Substitute all contractions by their full form because of differences in performance for Charniak parser
		data=re.sub(r'ain\'t',"are not",data)
		data=re.sub(r'won\'t',"will not",data)
		data=re.sub(r'\'is'," is",data)
		data=re.sub(r' nt '," not ",data)
		data=re.sub(r' nt\.'," not.",data)
		data=re.sub(r' nt\?'," not?",data)
		data=re.sub(r' nt\!'," not!",data)
		data=re.sub(r' re '," are ",data)
		data=re.sub(r' re\.'," are.",data)
		data=re.sub(r' re\?'," are?",data)
		data=re.sub(r' re\!'," are!",data)
		data=re.sub(r' re\n'," are.\n",data)
		data=re.sub(r' s ',"'s ",data)
		data=re.sub(r' m(?=[.?,:! ])'," am",data)
		data=re.sub("0\s+\.\s?\n","",data)
		data=re.sub("\n ","\n",data)
		data=re.sub(r'\n\s?[.?,]\s?\n',"",data)
		data=re.sub(r'( |\t){2}'," ",data)
		data=re.sub(r'\. \n',".\n",data)
		data=re.sub(r'\n +',"\n",data)
		Data=re.sub(r'^ ',"",data)
		data=re.sub(r'\n\.\s*$',"",data)
		data=re.sub(r'  '," ",data)
		data=re.sub(r' \.',".",data)
		data=re.sub(r'\.+',".",data)
		data=re.sub(r'\. ',".\n",data)
		data=re.sub(r'(?<=\w)\.(?=\w)',".\n",data)
		data=re.sub(r'(?<=\w)\?(?=\w)',"?\n",data)
		data=re.sub(r'\n\s*(xx)*[.?!,]\s*(?=\n)',"",data)
		data=re.sub(r'ca not',"can not",data)
		#Final preprocessed data that will be written to the file
		data=data.split("\n")
		preprocessedFileName=outputDirPrefix+"/"+inputFile.split("/")[-1].split(".")[0]+".PRP"
		f1=file(preprocessedFileName,"w")
		for i in range(len(data)):
			if data[i]!='':
				f1.write(data[i]+"\n")
		f1.close()
		return preprocessedFileName
	except:
		print "Error while preprocessing the transcript"
#Called by the generateIPSyn program for preprocessing
def cleanBatch(inputDirectory,preprocessedDirectory,childPrefix=""):
	try:
		#Sort the input files
		file_list=sorted(os.listdir(inputDirectory))
		#Preprocess the files in a given batch
		for i in range(len(file_list)):
			cleanFile(inputDirectory+"/"+file_list[i],preprocessedDirectory,childPrefix)
		return preprocessedDirectory	
	except:
		print "Error while preprocessing the transcripts"
