#The purpose of this script is to generate the IPSyn scores for a SALT or CHAT transcript
#This program takes as input a SALT or CHAT transcript and computes the IPSyn score
import os
import sys
import createParses
import preprocessCHAT
import preprocessSALT
import findN1_with_linenos
#single or batch processing - default= single file
singleFile=True
#SALT or CHAT transcript - default=SALT 
saltTranscript=True
inputChoice="1"
#SALT or CHAT transcript
print "1. Choose 1 if input is a SALT transcript file"
print "2. Choose 2 if input is a CHAT transcript file"
try:
	inputChoice=raw_input()
except:
	print "Error in input. Exiting.."
if inputChoice not in ["1","2"]:
	print "Please enter '1' or '2'. Exiting.."
	sys.exit()
if inputChoice =="1":
	saltTranscript=True
elif inputChoice=="2":
	saltTranscript=False		 
childPrefix=""
print "Enter the speaker ID of the child (case sensitive)"
try:
	childPrefix=raw_input()
except:
	print "Error in input. Exiting..."
	sys.exit()
inputChoice="1"
#Single File or Batch Processing 
print "1. Choose 1 if input is a single file"
print "2: Choose 2 if input is a directory"
try:
	inputChoice=raw_input()
except:
	#An error in the input
	print "Error in input. Exiting.."
	sys.exit()
#If the user enters an input other than 1 or 2
if inputChoice not in ["1","2"]:
	print "Please enter '1' or '2'. Exiting.."
	sys.exit()
inputFile=""
outputFile=""
inputDir=""
preprocessedDir=""
parsesDir=""
outputDir=""
rawDir=""
#Single file
if inputChoice=="1":
	#Generate IPSyn score for a single file
	singleFile=True
	print "Enter the name of the transcript:"
	inputFile=raw_input().strip()
	#Check if the file exists
	if not os.path.isfile(inputFile):
		print "Input file does not exist. Please enter an input file name. Exiting.."
		sys.exit()
#Batch processing
elif inputChoice=="2":
	#Generate IPSyn score for a batch of files
	singleFile=False
	#Input directory
	print "Enter the name of directory containing transcripts:"
	inputDir=raw_input().strip()
	if not os.path.isdir(inputDir):
		print "Input directory does not exist. Please enter a valid directory name. Exiting.."
		sys.exit()
else:
	print "Wrong input...Exiting!"
	sys.exit()
#Directory where the output files will be stored
askOutputDir=True
while askOutputDir:
	print "Enter the name of the directory where output files will be stored:"
	preprocessed_Present=False
	parses_Present=False
	results_Present=False
	raw_Present=False
	outputDir=raw_input().strip()
	#If the output directory 
	if not os.path.isdir(outputDir):
		os.mkdir(outputDir)
		askOutputDir=False
	elif len(os.listdir(outputDir))!=0:
		#Get user prompt if files are not empty
		if "preprocessed" in os.listdir(outputDir):
			preprocessed_Present=True
		if "parses" in os.listdir(outputDir):
			parses_Present=True
		if "results" in os.listdir(outputDir):
			results_Present=True
		if "raw" in os.listdir(outputDir):
			raw_Present=True
		if preprocessed_Present or parses_Present or results_Present or raw_Present:
			print "One of the directories - preprocessed, parses, results or raw is present in the output directory"
			print "Do you want to overwrite these contents of these directories (Y/N)?"
			overwrite=raw_input().strip()
			if overwrite.lower()=="y":
				os.system("rm -fr "+outputDir+"/preprocessed")
				os.system("rm -fr "+outputDir+"/parses")
				os.system("rm -fr "+outputDir+"/results")
				os.system("rm -fr "+outputDir+"/raw")
				askOutputDir=False
		else:
			askOutputDir=False

#Make directory for preprocessed files
preprocessedDir=outputDir+"/preprocessed"
os.mkdir(preprocessedDir)
#Make directory for parses
parsesDir=outputDir+"/parses"
os.mkdir(parsesDir)
#Make directory for results
resultsDir=outputDir+"/results"
os.mkdir(resultsDir)
#Make directory for raw counts
rawDir=outputDir+"/raw"
os.mkdir(rawDir)

#Give options to user to generate the IPSyn score for the first 100 utterances, a specified range of utterances or the entire transcript
print "1. Generate IPSyn Score on first 100 utterances"
print "2. Generate IPSyn Score on entire transcript"
print "3. Generate IPSyn Score on a range of utterances"
generateChoice="1"
try:
	generateChoice=raw_input()
	if generateChoice not in ["1","2", "3"]:
		print "Enter 1, 2 or 3."
		sys.exit()
except:
	print "Exiting ..."
	sys.exit()

#Generate the score for the entire transcript
generateScoreEntireTranscript=False
#Examining constructs starting from utterance no
beginingRange=1
#End examining constructs at this utterance
endRange=100

#Generate IPSyn score for the first 100 utterances of a transcript
if generateChoice=="1":
	generateScoreEntireTranscript=False
	beginingRange=1
	endRange=100
#Generate the IPSyn score for the entire transcript
elif generateChoice=="2":
	generateScoreEntireTranscript=True
#Generate the IPSyn score for a range of utterances
elif generateChoice=="3":
	generateScoreEntireTranscript=False
	print "Enter the 1st child utterance to be considered"
	#Expect a number
	try:
		beginingRange=int(raw_input())
		if beginingRange<1:
			print "The starting range should be a number >=1"
			sys.exit()
	except:
		print "Error in range. Please enter a number greater than 1."
		sys.exit()
	print "Enter the last child utterance to be considered"
	try:
		endRange=int(raw_input())
		if endRange<beginingRange:
			print "The end of the range should be less than the begining. Exiting.."
			sys.exit()
	except:
		print "Error in range. Exiting.."
		sys.exit()
#Wrong choice
else:
	print "Wrong input...Exiting!"
	sys.exit()

#Preprocessing the transcripts
print "Preprocessing the transcripts"
#Use the module for preprocessing the SALT transcript
if saltTranscript==True:
	if singleFile==True:
		preprocessedFileName=preprocessSALT.cleanFile(inputFile,preprocessedDir,childPrefix)
	else:
		preprocessSALT.cleanBatch(inputDir,preprocessedDir,childPrefix)
#Use the module for preprocessing the CHAT transcript
else:
	if singleFile==True:
		preprocessedFileName=preprocessCHAT.cleanFile(inputFile,preprocessedDir,childPrefix)
	else:
		preprocessCHAT.cleanBatch(inputDir,preprocessedDir,childPrefix)

#Parsing the transcripts
#The most time consuming part
print "Parsing the transcripts"
#Generate a parse for all the files in the preprocessed directory
createParses.parse(preprocessedDir,parsesDir)			

#Generate the IPSyn scores
findN1_with_linenos.generateIPSynScores(parsesDir,resultsDir,rawDir,generateScoreEntireTranscript,beginingRange,endRange)	

