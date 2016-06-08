AC-IPSyn

The AC-IPSyn software automatically computes the Index of Productive Syntax metric. This system runs on Linux and is a command line system. We are currently working towards developing systems that will run on Windows and other operating systems.


SYSTEM REQUIREMENTS

Operating System:
The current version of the software runs on Linux/UNIX systems. If Linux is not installed, you can install a virtual Linux machine on Windows using vmware.

Vmware Installation:
Install vmware for PC (virtual linux machine)
https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0
Download VMware Player for Linux 32-bit if you have a 32 bit machine. If you have a 64 bit machine, download VMware Player for Linux 64-bit.

Programming Language: 
1) Python
To check if python is installed, at the command prompt type:

bash$:python --version

The version should be less than 3. The system does not run with Python version 3 and above.
If python is not installed:
Download Python 2.7.3 from http://www.python.org/download/
Choose Python 2.7.3 compressed source tarball (for Linux, Unix or Mac OS X)

2) Programming Language: Perl
To check if perl is installed, at the command prompt type:

perl --version

If Perl is not installed, download and install the distribution present at 
http://www.perl.org/get.html#unix_like

Other software/toolkits needed:

(A) TreeTagger
 The AC-IPSyn package uses the TreeTagger software for determining unbound morphemes. This package is provided within the IPSyn software package.


(B) Charniak Parser:
The AC-IPSyn software uses the Charniak Parser to generate parses for child utterances. The AC-IPSyn package contains the source package for the Charniak parser.


Charniak Parser Compatibility:

To ensure that the Charniak parser binary is compatible with your system:

Run the following command at the AC_IPSyn directory
 
./CharniakParser/parse.sh test.txt test.txt_parse
test.txt_parse should contain the parse of the sentence as follows:

(S1 (S (NP (DT This)) (VP (AUX is) (NP (DT a) (NN test) (NN sentence))) (. .)))

If there is an error, you may need to recompile the Charniak server on your system.

Navigate to the CharniakParser directory as follows: cd CharniakParser

Extract the source files from the source package as follows:
 tar -zvxf CharniakParserPackage.tar.gz
Navigate to the CharniakParserPackage directory: 
cd CharniakParserPackage

Execute the following commands:
rm *.o
make parseIt

There should be a file called parseIt in the directory. 

Copy this file to the CharniakParser directory using the command:  cp parseIt ..

Navigate to the AC-IPSyn directory using the command: cd ..

Run the following command at the AC-IPSyn directory
 
./CharniakParser/parse.sh test.txt test.txt_parse
test.txt_parse should contain the parse of the sentence as follows:

(S1 (S (NP (DT This)) (VP (AUX is) (NP (DT a) (NN test) (NN sentence))) (. .)))


==============================================================================

INPUT FORMAT

The AC-IPSyn software takes as input transcripts in the SALT and CHAT transcription format.

SALT Transcription Conventions

For a description of the SALT transcription conventions, please refer to the manual at: http://www.saltsoftware.com/salt/TranConvSummary.pdf

CHAT Transcription Conventions

For a description of the CHAT transcription conventions, please refer to the manual at:  http://childes.psy.cmu.edu/manuals/CHAT.pdf

Sample SALT transcripts are present in sample_SALT/input directory. 
Sample CHAT transcripts are present in sample_CHAT/input directory.

=============================================================================

RUNNING THE AC-IPSYN System

Run the command python source/generateIPSyn.py at the shell prompt:
-bash-4.0$ python source/generateIPSyn.py 

The following explains the prompts one by one.  

==Prompt: 
1. Choose 1 if input is a SALT transcript file
2. Choose 2 if input is a CHAT transcript file

==Explanation:
Choose 1 to process a SALT transcript, 2 to process a CHAT transcript

==Prompt:
Enter the speaker ID of the child (case sensitive)

==Explanation:
The speaker ID identifies the speakers in the transcript. The speaker ID is case sensitive. The AC-IPSyn software will extract the utterances with this speaker ID.

NOTE: In case of batch processing of multiple transcripts, the AC-IPSyn system assumes all the transcripts have the same child label.

For the example files provided, enter C for the SALT transcript, and CHI for the CHAT transcripts. 


==Prompt:
1. Choose 1 if input is a single file
2: Choose 2 if input is a directory

==Explanation:
Choose 1 if you wish to compute the IPSyn score for a single transcript, 2 if you wish to compute the IPSyn score for all the transcripts in a directory.


==Prompt:
Enter the name of the transcript:

==Explanation:
If you choose to process a single transcript, enter the name of the transcript file. Please note the name of the transcript is case sensitive and includes the extension. 

==Prompt:
Enter the name of directory containing transcripts:

==Explanation:
If you choose to process all the transcripts in a directory, enter the name of the directory containing the transcripts.

==Prompt:
Enter the name of the directory where output files will be stored:

==Explanation:
Give the name of the directory where you want to store the output. If this directory does not exist, a new one will be created. If the directory exists, the  directories "preprocessed", "parses", "raw" and "results" within the output directory will be overwritten with the new results. 

Enter the name of the directory where output files will be stored:
Enter the directory name where you want to store the output. There will be 4 sub-directories that will be created: preprocessed, parses, results and raw.

If this directory exists, and contains any of the four subdirectories: preprocessed, parses, results and raw, you will be prompted as follows:

==Prompt:
One of the directories  preprocessed, parses, results or raw is present in the output directory
Do you want to overwrite the contents of these directories (Y/N)?

==Explanation:
Enter 'Y' if you want to overwrite the contents. The contents of the directories preprocessed, parses, results and raw will be overwritten.
Enter 'N' if you want to give a different output directory name. You will see the prompt for entering the output directory. Specify a different output directory name where you want to store the output.


==Prompt:
1. Generate IPSyn Score on first 100 utterances
2. Generate IPSyn Score on entire transcript
3. Generate IPSyn Score on a range of utterances

==Explanation:
The IPSyn score in computed based on the utterances in the preprocessed file. 
Select '1' if you wish to compute the IPSyn score for the first 100 utterances. 
Select '2' if you wish to compute the IPSyn score for the entire transcript. 
Select '3' if you wish to compute the IPSyn score for a range of utterances.
If you select '3', the range is calculated based on the utterances in the preprocessed transcript. If the beginning of the given range is larger than the number of utterances in the preprocessed transcript, the IPSyn score will not be computed. However, the preprocessed transcript and parsed transcript will be stored in the output directory.


=========================================================================
OUTPUT DIRECTORIES

The following directories are created in the output directory:

1)results
This directory contains the IPSyn score for each transcript 
2)raw
This directory contains the IPSyn score where each structure can have a score of more than 2.
3)preprocessed
This directory contains the preprocessed directory. These are intermediate files generated by the AC-IPSyn system.
4)parses
This directory contains the parses of the transcripts. These are intermediate files generated by the AC-IPSyn system.

===========================================================================
TESTING THE AC-IPSYN SYSTEM

The directories sample_SALT_dir and sample_CHAT_dir have sample SALT and CHAT transcripts along with the expected output.

sample_SALT_dir/input contains the input directory with SALT transcripts
sample_SALT_dir/preprocessed contains the preprocessed SALT transcripts
sample_SALT_dir/parses contains the parses of the SALT transcripts
sample_SALT_dir/results contains the IPSyn score for the SALT transcripts
sample_SALT_dir/raw contains the results when the IPSyn score for each structure is not limited at 2

sample_CHAT_dir/input  contains the input directory with CHAT transcripts
sample_CHAT_dir/preprocessed  contains the preprocessed CHAT transcripts
sample_CHAT_dir/parses contains the parses of the CHAT transcripts
sample_CHAT_dir/results contains the IPSyn score for the CHAT transcripts
sample_CHAT_dir/raw contains the results when the IPSyn score for each structure is not limited at 2

In order to test the system, execute the following command at the AC-IPSyn directory:

TEST THE SYSTEM WITH SALT TRANSCRIPTS

python source/generateIPSyn.py

When prompted:
1. Choose 1 if input is a SALT transcript file
2. Choose 2 if input is a CHAT transcript file
Choose 1

When prompted:
Enter the speaker ID of the child (case sensitive)
Enter C

When prompted:
1. Choose 1 if input is a single file
2: Choose 2 if input is a directory
Enter 2

When prompted:
Enter the name of directory containing transcripts:
Enter sample_SALT_dir/input

When prompted:
Enter the name of the directory where output files will be stored:
Enter the directory name where you want to store the output. If this directory exists, the contents of the directory will be overwritten.

There will be 4 sub-directories that will be created: preprocessed, parses, results and raw.

When prompted:
1. Generate IPSyn Score on first 100 utterances
2. Generate IPSyn Score on entire transcript
3. Generate IPSyn Score on a range of utterances
Enter 1

To display the content of a directory, use the command ls 

Screen Shot

-bash-4.0$ python source/generateIPSyn.py 
1. Choose 1 if input is a SALT transcript file
2. Choose 2 if input is a CHAT transcript file
1
Enter the speaker ID of the child (case sensitive)
C
1. Choose 1 if input is a single file
2: Choose 2 if input is a directory
2
Enter the name of directory containing transcripts:
sample_SALT_dir/input
Enter the name of the directory where output files will be stored:
SALT_output
1. Generate IPSyn Score on first 100 utterances
2. Generate IPSyn Score on entire transcript
3. Generate IPSyn Score on a range of utterances
1
Preprocessing the transcripts
Andy-Nar-SSS
Kelina-Con
Laura-APNF
Maria-FWAY-English
Parsing the transcripts
Andy-Nar-SSS
16467: old priority 0, new priority 5
Kelina-Con
16484: old priority 0, new priority 5
Laura-APNF
16501: old priority 0, new priority 5
Maria-FWAY-English
16518: old priority 0, new priority 5
Computing IPSyn score
Andy-Nar-SSS
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
Kelina-Con
Laura-APNF
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
Maria-FWAY-English

-bash-4.0$ ls SALT_output/*
SALT_output/parses:
Andy-Nar-SSS.PARSE      Kelina-Con.PARSE.bak  Maria-FWAY-English.PARSE
Andy-Nar-SSS.PARSE.bak  Laura-APNF.PARSE      Maria-FWAY-English.PARSE.bak
Kelina-Con.PARSE        Laura-APNF.PARSE.bak

SALT_output/preprocessed:
Andy-Nar-SSS.PRP  Kelina-Con.PRP  Laura-APNF.PRP  Maria-FWAY-English.PRP

SALT_output/raw:
Andy-Nar-SSS.RAW  Kelina-Con.RAW  Laura-APNF.RAW  Maria-FWAY-English.RAW

SALT_output/results:
Andy-Nar-SSS.IPS  Kelina-Con.IPS  Laura-APNF.IPS  Maria-FWAY-English.IPS

========================================

TEST THE SYSTEM WITH CHAT TRANSCRIPTS
Execute the following command at the AC-IPSyn directory:

python source/generateIPSyn.py

When prompted:
1. Choose 1 if input is a SALT transcript file
2. Choose 2 if input is a CHAT transcript file
Choose 2

When prompted:
Enter the speaker ID of the child (case sensitive)
Enter CHI

When prompted:
1. Choose 1 if input is a single file
2: Choose 2 if input is a directory
Enter 2

When prompted:
Enter the name of directory containing transcripts:
Enter sample_CHAT_dir/input

When prompted:
Enter the name of the directory where output files will be stored:
Enter the directory name where you want to store the output. If this directory exists, the contents of the directory will be overwritten.

There will be 4 sub-directories that will be created: preprocessed, parses, results and raw.

When prompted:
1. Generate IPSyn Score on first 100 utterances
2. Generate IPSyn Score on entire transcript
3. Generate IPSyn Score on a range of utterances
Enter 1

To display the content of a directory, use the command ls 

Screen Shot

-bash-4.0$ python source/generateIPSyn.py 
1. Choose 1 if input is a SALT transcript file
2. Choose 2 if input is a CHAT transcript file
2
Enter the speaker ID of the child (case sensitive)
CHI
1. Choose 1 if input is a single file
2: Choose 2 if input is a directory
2
Enter the name of directory containing transcripts:
sample_CHAT_dir/input
Enter the name of the directory where output files will be stored:
CHAT_output
1. Generate IPSyn Score on first 100 utterances
2. Generate IPSyn Score on entire transcript
3. Generate IPSyn Score on a range of utterances
1
Preprocessing the transcripts
fssli009
fssli058
fssli062
fssli066
fssli108
fssli113
fssli501
fssli519
fssli526
fssli528
fssli536
fssli568
fssli576
fssli589
fssli591
fssli592
fssli599
fssli608
fssli613
Parsing the transcripts
fssli009
16670: old priority 0, new priority 5
fssli058
16687: old priority 0, new priority 5
fssli062
16704: old priority 0, new priority 5
fssli066
16721: old priority 0, new priority 5
fssli108
16738: old priority 0, new priority 5
fssli113
16755: old priority 0, new priority 5
fssli501
16772: old priority 0, new priority 5
fssli519
16789: old priority 0, new priority 5
fssli526
16848: old priority 0, new priority 5
fssli528
16865: old priority 0, new priority 5
fssli536
16882: old priority 0, new priority 5
fssli568
16899: old priority 0, new priority 5
fssli576
16916: old priority 0, new priority 5
fssli589
16933: old priority 0, new priority 5
fssli591
16950: old priority 0, new priority 5
fssli592
16967: old priority 0, new priority 5
fssli599
16984: old priority 0, new priority 5
fssli608
17001: old priority 0, new priority 5
fssli613
17018: old priority 0, new priority 5
Computing IPSyn score
fssli009
fssli058
fssli062
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli066
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli108
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli113
fssli501
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli519
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli526
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli528
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli536
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli568
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli576
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli589
fssli591
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli592
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli599
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
fssli608
fssli613
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
using tree-tagger
	reading parameters ...
	tagging ...
	 finished.
-bash-4.0$ ls CHAT_output/*
CHAT_output/parses:
fssli009.PARSE      fssli113.PARSE      fssli536.PARSE      fssli592.PARSE
fssli009.PARSE.bak  fssli113.PARSE.bak  fssli536.PARSE.bak  fssli592.PARSE.bak
fssli058.PARSE      fssli501.PARSE      fssli568.PARSE      fssli599.PARSE
fssli058.PARSE.bak  fssli501.PARSE.bak  fssli568.PARSE.bak  fssli599.PARSE.bak
fssli062.PARSE      fssli519.PARSE      fssli576.PARSE      fssli608.PARSE
fssli062.PARSE.bak  fssli519.PARSE.bak  fssli576.PARSE.bak  fssli608.PARSE.bak
fssli066.PARSE      fssli526.PARSE      fssli589.PARSE      fssli613.PARSE
fssli066.PARSE.bak  fssli526.PARSE.bak  fssli589.PARSE.bak  fssli613.PARSE.bak
fssli108.PARSE      fssli528.PARSE      fssli591.PARSE
fssli108.PARSE.bak  fssli528.PARSE.bak  fssli591.PARSE.bak

CHAT_output/preprocessed:
fssli009.PRP  fssli108.PRP  fssli526.PRP  fssli576.PRP  fssli599.PRP
fssli058.PRP  fssli113.PRP  fssli528.PRP  fssli589.PRP  fssli608.PRP
fssli062.PRP  fssli501.PRP  fssli536.PRP  fssli591.PRP  fssli613.PRP
fssli066.PRP  fssli519.PRP  fssli568.PRP  fssli592.PRP

CHAT_output/raw:
fssli009.RAW  fssli108.RAW  fssli526.RAW  fssli576.RAW  fssli599.RAW
fssli058.RAW  fssli113.RAW  fssli528.RAW  fssli589.RAW  fssli608.RAW
fssli062.RAW  fssli501.RAW  fssli536.RAW  fssli591.RAW  fssli613.RAW
fssli066.RAW  fssli519.RAW  fssli568.RAW  fssli592.RAW

CHAT_output/results:
fssli009.IPS  fssli108.IPS  fssli526.IPS  fssli576.IPS  fssli599.IPS
fssli058.IPS  fssli113.IPS  fssli528.IPS  fssli589.IPS  fssli608.IPS
fssli062.IPS  fssli501.IPS  fssli536.IPS  fssli591.IPS  fssli613.IPS
fssli066.IPS  fssli519.IPS  fssli568.IPS  fssli592.IPS

