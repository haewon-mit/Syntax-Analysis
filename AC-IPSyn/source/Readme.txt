generateIPSyn.py
	0. preprocessSALT, preprocessCHAT
	1. createParses.py
		input: preprocessedDir, parseDir
		output: parsedfiles output

		1.1 charniakParser/parse.sh

	2. findN1_with_linenos.py
		input: parseDir, resultsDir, rawDir, (bool) generateScoreEntireTranscript
		output: IPSyn result and raw files

		2.1 generateIPSynScores()

			2.1.1 findPatterns()
				input: inputfile
				output: # of utterances considered, result patterns ( (sentence#,word) pair per construct)

				2.1.1.1 extractPhrase()
					input: inputfile data, results_patterns
					output: results_patterns, # of utterances considered

					2.1.1.1.1 split data (parse per sentences)
					2.1.1.1.2 per each sentence parse, find all Patterns/words per construct (ex. N1, N2, ...)

				2.1.1.2	populate FileList with result_patterns
	
			2.1.2 removeCommonPluralsN7()

			2.1.3 scoreTranscripts()

			2.1.4 writeOutputRawFile()
