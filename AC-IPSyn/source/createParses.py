#The purpose of this module is to create parses using the charniak parser
import os
import sys
#Function generates parses using the Charniak parses
#Parameters: singleFile - generate a parse for a single file or directory
#            preprocessedFile - will be used if the singleFile is true - gives the preprocessed CHAT or SALT transcript
#            preprocessedDirectory - contains the preprocessed files if batch processing is used
#            parsesDirectory - parses will be stored here if batch processing is used
#	
def parse(preprocessedDirectory="",parsesDirectory=""):
	try:
		#Sort the input files
		file_list=sorted(os.listdir(preprocessedDirectory))
		#Parses are to be generated for a batch of files
		for i in range(len(file_list)):
			print file_list[i].split("/")[-1].split(".")[0]
			os.system("./CharniakParser/parse.sh "+preprocessedDirectory+"/"+file_list[i]+ " " +parsesDirectory+"/"+file_list[i].split(".")[0]+".PARSE")
		return parsesDirectory
	except:
		print "Error occured while parsing"

