#Purpose: Clean up the SALT transcripts
import sys
import re
import os

#Patterns to remove markup from the SALT transcripts
#Remove everything within square braces
squareBracesPattern=r'(\[.*?\])'
#Remove everything within curly braces
curlyBracesPattern=r'(\{.*?\})'
#Remove everything within round braces
roundBracesPattern=r'( ?\(+.*?\)+)'
#Remove unintelligible segments and utterances
unintelligiblePattern=r'([xX]{2,3})'
#Remove unintelligible words in the middle of sentence
unintelligibleWordsPattern=r'(([ ]|^)[xX](?=[ \.\?\,]))'
#Remove unintelligible words at the begining of a sentence
unintelligibleBeginingPattern=r'(\n *[xX]+[ \.\?!]+)'
#Remove ~:intonation prompt
intonationPromptPattern=r'(~)'
#Remove ^:interrupted utterance
interruptedUtterancePattern=r'(\^)'
#Remove <: abandoned utterance or overlapping speech<>
abandonedUtterancePattern=r'(\<)'
#Remove >:<>:overlapping speech
overlappingSpeechPattern=r'(\>)'
#Pause between utterances of different speakers ::03, pause between utterances of same speaker ;:03
pausesPattern=r'( [:;]{0,1}\s*[0-9]*:[0-9]+)'
#Remove Carriage Return if the file is a windows file being processed on a UNIX machine
carriageReturnPattern=r'(\r)'	
#Remove the markup for the bound morphemes: Possesive inflection
possessiveInflectionPattern=r'(\/[zZ])'
#Remove markup for the plural and possessive bound morphemes
pluralPossessivePattern=r'(\/[Ss]\/[zZ])'
#Remove the / for the rest of the bound morphemes
boundMorphemePattern=r'(\/[3]{0,1})'
#Ommisions of words or morphemes
ommisionPattern=r'(\*.+?(?=[ ?\.!]))'	
#Linked words denoted by | split the words backs
linkedWordsPattern=r'(_)'
#Remove the sound effects pattern
soundEffectsPattern=r'(%)'

squareBP=re.compile(squareBracesPattern)
curlyBP=re.compile(curlyBracesPattern)
roundBP=re.compile(roundBracesPattern)
unintelligibleP=re.compile(unintelligiblePattern)
intonationPromptP=re.compile(intonationPromptPattern)
interruptedUtteranceP=re.compile(interruptedUtterancePattern)
abandonedUtteranceP=re.compile(abandonedUtterancePattern)
overlappingSpeechP=re.compile(overlappingSpeechPattern)
carriageReturnP=re.compile(carriageReturnPattern)
pausesP=re.compile(pausesPattern)
pluralPossessiveP=re.compile(pluralPossessivePattern)
possessiveInflectionP=re.compile(possessiveInflectionPattern)
ommissionP=re.compile(ommisionPattern)
boundMorphemeP=re.compile(boundMorphemePattern)
linkedWordsP=re.compile(linkedWordsPattern)
unintelligibleWordsP=re.compile(unintelligibleWordsPattern)
unintelligibleBeginingP=re.compile(unintelligibleBeginingPattern)
soundEffectsP=re.compile(soundEffectsPattern)

#Preprocess a given file to remove markup from the transcripts
def cleanFile(inputFile,outputDirPrefix="",childPrefix=""):
	try:
		#Patterns to remove markup from the SALT transcripts
		#Remove the subject prefix at the begining of every sentence
		subjectPrefixPattern=r'(\n'+childPrefix+' \s*)'
		#Remove the subject prefix at the begining of the transcript
		beginingSubjectPattern=r'(^'+childPrefix+' \s*)'
	
		subjectPrefixP=re.compile(subjectPrefixPattern)
		beginingSubjectP=re.compile(beginingSubjectPattern)
		print inputFile.split("/")[-1].split(".")[0]
		data=file(inputFile).read().split("\n")
		new_data=[]
		previousChild=False
		for a in data:
			#Extract the utterances for the child prefix
			if a.find(childPrefix) == 0:
				new_data.append(a)
				previousChild=True
			#The sentence has been split and so join the sentences
			elif a.find(" ")==0 and previousChild==True:
				new_data[-1]=new_data[-1]+a
			else:
				previousChild=False
		#Only contains the child's utterances
		data="\n".join(new_data)
		#Remove all the square braces (Codes)
		data=squareBP.sub("",data)
		#Remove all the curly braces (Comments)
		data=curlyBP.sub("",data)
		#Remove all the round braces (Mazes. Filled pauses, false starts, repetitions, reformulations, and interjections)
		data=roundBP.sub("",data)
		#Remove the unintelligible utterances symbol
		data=unintelligibleP.sub("",data)
		#Remove the intonation prompt
		data=intonationPromptP.sub("",data)
		#Remove the interrupted utterance symbol
		data=interruptedUtteranceP.sub("",data)
		#Remove the abandoned utterance symbol
		data=abandonedUtteranceP.sub("",data)
		#Remove the overlapping speech symbol
		data=overlappingSpeechP.sub("",data)
		#Remove carriage return
		data=carriageReturnP.sub("",data)
		#Remove the subject prefix
		data=subjectPrefixP.sub("\n",data)
		#Remove the subject prefix at the begining of the file
		data=beginingSubjectP.sub("",data)
		#Remove the pauses
		data=pausesP.sub("",data)
		#Replace the plural possesive pattern with an s
		data=pluralPossessiveP.sub("s",data)
		#Replace the possessive inflection pattern with an 's
		data=possessiveInflectionP.sub("'s",data)
		#Remove the ommited words as it will bias the IPSyn results
		data=ommissionP.sub(" ",data)
		#The rest of the bound morphemes remove the / retain the morphemes
		data=boundMorphemeP.sub("",data)
		#Separate the linked words (joined together by an underscore)
		data=linkedWordsP.sub(" ",data)
		#Remove the unintelligible words since we do not want them counted by IPSyn
		data=unintelligibleWordsP.sub("",data)
		#Remove the unintelligible words at the begining of a sentence
		data=unintelligibleBeginingP.sub("\n",data)
		#Remove the sound effects pattern %
		data=soundEffectsP.sub("",data)

		data=re.sub("(\++ )","",data)
		data=re.sub(r'\++\.',".",data)

		#Substitute all contractions by their full form because of differences in performance for Charniak parser
		data=re.sub(r'ain\'t',"are not",data)
		data=re.sub(r'won\'t',"will not",data)
	
		data=re.sub(r'n\'t '," not ",data)
		data=re.sub(r'n\'t\.'," not.",data)
		data=re.sub(r'n\'t\?'," not?",data)
		data=re.sub(r' n\'t\!'," not!",data)
		data=re.sub(r'\'re '," are ",data)
		data=re.sub(r'\'re\.'," are.",data)
		data=re.sub(r'\'re\?'," are?",data)
		data=re.sub(r'\'re\!'," are!",data)
		data=re.sub(r'\'re\n'," are.\n",data)
	
		data=re.sub(r' s ',"'s ",data)
		data=re.sub(r' m(?=[.?,:! ])'," am",data)
		data=re.sub("0\s+\.\s?\n","",data)
		data=re.sub("\n ","\n",data)
		data=re.sub(r'\n\s?[.?,]\s?\n',"",data)
		data=re.sub(r'( |\t){2}'," ",data)
		data=re.sub(r'\. \n',".\n",data)
		data=re.sub(r'\n +',"\n",data)
		data=re.sub(r'^ ',"",data)
		data=re.sub(r'\n\.\s*$',"",data)
		data=re.sub(r'  '," ",data)
		data=re.sub(r' \.',".",data)
		data=re.sub(r'\.+',".",data)
		data=re.sub(r'\. ',".\n",data)
		data=re.sub(r'(?<=\w)\.(?=\w)',".\n",data)
		data=re.sub(r'(?<=\w)\?(?=\w)',"?\n",data)
		data=re.sub(r'\n\s*(xx)*[.?!,]\s*(?=\n)',"",data)
		data=re.sub(r'ca not',"can not",data)
		data=re.sub(":[0-9]+\s?","",data)
		data=re.sub(" \?","?",data)
		#Remove repeating punctuation
		data=re.sub(r'[.,?!]+(?=[.,?!])',"",data)
		#Remove the * that is left over
		data=re.sub(r'\*',"",data)
		#Take care of root identification
		data=data.split("|")
		if len(data)>1:
			for i in range(1,len(data)):
				#print "***",data[i]
				data[i]=" ".join(data[i].split(" ")[1:])
				#print "$$$$$$$$$$$",data[i]
		data=" ".join(data)
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
		print "Error happened while preprocessing"

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
		print "Error occured while preprocessing"
