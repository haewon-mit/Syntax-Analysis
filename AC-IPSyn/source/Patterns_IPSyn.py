#Purpose: This contains the regular expression patterns that will be used for 
#	  extracting the constructs for the IPSyn structure.
Patterns={
		#Proper,Mass or Count Noun
		'N1':r'(\((NNS|NNPS|NN|NNP) ([^)]*)\))',
		#Pronoun or prolocative excluding modifiers
	 	'N2':r'(\((((PRP|WP) ([^)]*))|([W]?RB ([hH]ere|[Tt]here|[Ww]here|[Tt]hereafter|[Hh]ereafter|[Th]ereupon|[Hh]ereabouts|[Ww]hereabouts|[Ww]hereupon|[Tt]hereabouts|[Ss]omewhere|[Ee]verywhere)))\))',
		#Modifier including adjectives, possessives and quantifiers
		'N3':r'(\((DT|PRP\$|WP\$|JJ|JJR|JJS|CD|POS) ((?![Aa]\))(?![Aa]n\))(?![Tt]he\))[^)]+)\))',
		#Two word NP: nominal preceded by article or modifier
		'N4':r'(\((DT|RP|PRP\$|WP\$|JJ|JJR|JJS|CD|POS) ([^)]*)\) \((NNS|NNPS|NN|NNP) ([^)]*)\))',
		#Article used before a noun 
		'N5':r'(\((DT) (([Aa])|([Aa]n)|([Tt]he))\) \((NNS|NNPS|NN|NNP) ([^)]*)\))',
		#Two word NP(as in N4) after verb or preposition
		'N6':r'(\((AUX|VB|VBD|VBG|VBN|VBP|VBZ|MD|(?<=\(PP \()IN|TO) ([^)]*)\)[ )]*(\((NP|ADJP) )+\((DT|RP|PRP\$|WP\$|JJ|JJR|JJS|CD|POS) ([^)]*)\) \((NNS|NNPS|NN|NNP) ([^)]*)\))',
		#Plural Suffix (should end with s) - not looking for irregular plurals
		'N7':r'(\((NNS|NNPS) ([^)]+s)\))',
		#Two-word NP(as in N4) before verb
		'N8':r'(\((DT|RP|PRP\$|WP\$|JJ|JJR|JJS|CD|POS) ([^)]*)\) \((NNS|NNPS|NN|NNP) ([^)]*)\))([ )]*)\((VP)? \((AUX|VB|VBD|VBG|VBN|VBP|VBZ|MD) ([^)]*)\)',
		#Three word NP (Det-Mod-N or Mod-Mod-N)
		'N9':r'(\(((PRP\$)|(WP\$)|(JJ)|(JJR)|(JJS)|(CD)|(POS)|(DT)) ([^)]*)\) \(((PRP\$)|(WP\$)|(JJ)|(JJR)|(JJS)|(CD)|(POS)) ([^)]*)\) \(((NNS)|(NNPS)|(NN)|(NNP)) ([^)]*)\))',
		#Adverb modifying adjective or nominal
		'N10':r'(((\(RB (?![Nn]ot\))(?![Nn]\'t\))([^)]+)\))([ )]*)(\(((NP)|(ADJP)) )?\((NN|NNS|NNP|NNPS|JJ|JJR|JJS|PRP|CD|DT|WP) ([^()]+)\))|(\((NN|NNS|NNP|NNPS|JJ|JJR|JJS|PRP|CD|WP) [^()]+\) \(RB ([^()]+)\))|(\(NP \(PDT ([^()]+)\)))',
		#Other bound morphemes on Nouns or adjectives(not stored as a lexical unit)
		'N11':r'(\((JJR|JJS|JJ) ((?!([Bb]etter)|([Oo]ther)|([Ss]uper)|([Bb]est)|([Ss]ister)|([Oo]ver)|([Uu]nder))(([Uu]n)?[^()]+((er)|(est)|(ies)|(ish)))|(([Uu]n)[^()]+((er)|(est)|(ies)|(ish))?))\))',
		#Other not used
		'N12':'',
		#Verb
		'V1':r'(\((AUX|VB|VBD|VBG|VBN|VBP|VBZ) ([^)]*)\))',
		#Particle or preposition
		#((?<=\(PP \()IN(?= [^)]+\) \(S))|
		'V2':r'(\(((RP)|((?<=\(PP \()((IN)|(TO))(?= [^)]+\) \())|((?<=\(PP \()((IN)|(TO))(?! ([^)]+)\) \(S))) ([^)]*)\))',
		#Prepositional Phrase (Prep + NP)
		'V3':r'(\PP \(((IN)|(TO)) ([^)]*)([ )]*)\(NP( \(([A-Z$]+) ([^)]*)\))+)',
		#Copula linking two nominals
		#NP VP NP or NP VP ADJP
		'V4':r'((( [Ii\']s\))|( [Aa]re\))|( [Aa]m\))|( [Bb]e\))|( [Ww]ere\))|( [Bb]een\))|( [Bb]eing\))|( [Ww]as\))|( [Bb]ec[oa]me)|( [Bb]ecoming\))|( [Ss]eem))|(\(((NP)|(WHNP))( (\([A-Z$]+ ([^()]+)\))+)\) (\(VP ([A-Z]+ [^()]+)+? )?\((VP|SQ) \((AUX|VB|VBZ|VBG|VBN|VBD|VBP) ([^()]+)\) (\(RB [^()]+\) )?\(ADJP( \([A-Z$]+ ([^()]+)\))+\)))',
		#Catenative(pseudo-auxiliary) preceeding a verb
		'V5':r'((gonna)|(hafta)|(wann?t?a)|(s\'pposedt?a))\)+ +\(VP \(((VB)|(AUX)) [^()]+\)',
		#Auxilary do,is,have in VP
		'V6':r'(\(AUX (([dD](o|id|oing|ne))|([Bb]i(een|e|eing))|([Ii\']s)|([Aa\'](m|re))|([Ww](as|ere))|([Hh]a(d|s|ve|ving))))',
		#Progressive suffix
		'V7':r'(\(VP \((VBG) ([^()]+ing)\))',
		#Adverb
		'V8':r'(\(((RB)|(WRB|NP \(PDT)) ([^)]*)\))',
		#Modal preceeding verb
		'V9':r'((\(VP \(MD ([^()]+)\) (\(RB [^()]+\) )?\(VP( \((\w+) ([^)]+)\))+\))|(\(SQ \(MD ([^ ()]+)\)( \(RB [^()]+\))?( \((\w+) ([^)]*)\))+\) \(VP( \((\w+) ([^)]*)\))+\)))',
		#Third person singular present tense suffix
		'V10':r'((\(VBZ ([^)]*)\))|(\(AUX (?![\']?s\))([^)]*s)\)))',
		#Past tense modal
		#Check for the list of all the modals in the PENN Tree bank
		'V11':r'(\(MD ((?i)((could)|(would)|(should)|(might)|(must)|(need)|(ought)|(dared)|(\'ll)))\))',
		#Regular past tense prefix
		'V12':r'(\(VP \(VB[DN] ([^)]+ed)\))',
		#Past tense auxiliary - only looking for Did, Was, Had
		#Check the PENN Tree bank for the entire list
		#Regular past tense ends with ed except for the irregular verbs
		#Need to get a list of the irregular verbs
		'V13':r'(\(AUX ((([Dd]id)|([Ww]as)|([Ww]ere)|([Hh]ad)|(\'d))|([^)]*[^e]ed))\))',
		#Medial adverb
		'V14':r'\n?.*?(\([A-Z$]+ [^()]+\).*?(W?RB|\(NP \(PDT) (?!not)([^()]+)(.*?\([A-Z$]+ [^()]+\)).*\n?)',
		#Copula,Modula or Auxiliary for emphasis or ellipsis
		#Look at this later
		#Common - Yes - positive forms of the modal (no not present after modal)
		#	   No - negative form of the modal present(not or n't present after modal/aux)
		#Need to look at Copula verbs for ellipsis
		'V15':r'(((\(RB [Yy]es\)) |(\((DT [Nn]o)\))).*?(\((MD|AUX) ([^)]*)\)))',
		#Past tense copula
		#Check for past tense auxiliaries?
		'V16':r'((( [Ww]ere\))|( [Bb]een\))|( [Ww]as\))|( [Bb]ecame)|( [Ss]eemed))|(\(((NP)|(WHNP))( (\([A-Z$]+ ([^()]+)\))+)\) (\(VP ([A-Z]+ [^()]+)+? )?\((VP|SQ) \((VBD) ([^()]+)\) (\(RB [^()]+\) )?\(ADJP( \([A-Z$]+ ([^()]+)\))+\)))',
#r'(\((NP|WHNP)( (\((\w+) ([^)]+)\))+)\) \((VP|SQ) \(((AUX (([Dd]id)|([Ww]as)|([Hh]ad)|(\'d))|([^)]*[^e]ed))|(VBD ([^)]+)))\) \((ADJP|NP)( \((\w+) ([^)]+)\))+\))',
		#Bound morpheme on a verb or adjective(to make an adverb)
		#Need to get all the possible rules that go with this
		'V17':r'\(((VB[^G]?)|(RB)) ((((?![Rr]emember)(?![Ii]nside)(?![Rr]ecord)(([Rr]e)|([Ii]n)|([Ee]n)|([uU]n)|([Mm]is)|([Tt]rans)|([eE]x)|([Dd]is))([^ ()]+))|((?![Oo]nly)([^ ()]+)(ly))))\)',
		#r'\((VB|RB|VBZ|VBG|VBD|VBN|VBP|AUX|RB) (((un|re)(\w+)(ly)?)|((\w+)(ly))\))',
		#Intonationally marked question
		'Q1':r'((\(S. \((FRAG|NP|(S \(VP)).*(\. \?))+?)',
		# Routine do/go or existence name question or wh-pronoun alone.
		'Q2':r'((\(S. .*\(((WP(\$)?)|WHNP|WHADP|WHAVP|WHPP) [^)]+\).*(\. \?))+?)',
		#(Simple Negation +X ) neg=no(t), can't don't X=NP,PP,VP,Adj, Adv etc
		'Q3':r'((\(S..*\((RB|DT) ([Nn](o|ot|\'t|ever))\).*\(\. [?.!]\))+?)',
		#Initial Wh-pronoun followed by verb
		'Q4':r'((\(S. (\(([A-Z$]+ ))+(\(WP(\$)? ([^)]+)\))[ )]*(\(([A-Z$]+ ))*\((AUX|VB|VBD|VBP|VBN|VBG|VBZ|MD).*(\. \?))+?)',
		#Negative Morpheme between subject and verb
		'Q5':r'((\(S. (\(S \(NP.*(\(VP(\)| )+((\(((AUX)|(MD)) [^)]+\))? \(RB ((\'nt)|(not)|(n\'t))\) \(VP).*))\(\. [!.?]\))+?)',
		#Wh-question with inverted modal, copula or auxillary
		'Q6':r'((\(S. \(SBARQ.*\(SQ.*(\. \?))+?)',
		#Negation of copula, modal or auxiliary
		'Q7':r'(\(S1.*(\(VP \(((AUX)|(MD)) [^)]+\) (\(ADVP )?\(RB ((not)|(n\'t)|(\'nt)|(never))\)(.*))\(\. [.!?]\))+?',
		#r'((\(S. .*\(((AUX)|(MD)) [^)]+\) \(RB ((not)|(n\'t)).*(\. \?))+?)',
		#Yes/no question with inverted modal, copula or auxiliary
		'Q8':r'((\(S. \(SQ.*(\. \?))+?)',
		#Why, When, Which, Whose
		'Q9':r'((\(S. (\(([A-Z$]+ ))+([Ww](hy|hen|hich|hose)).*(\. \?))+?)',
		# Tag Question
		'Q10':r'(\(S1((?!( \(S((Q)|(BARQ)))).*) \(, ,\) (.*)\(\. \?\))+?',
		#Other: e.g questions with negation and inverted cop/aux/modal
		'Q11':r'((\(S. .*\(((SBARQ)|((SQ)?)|(S)|(SINV)) (?!\(NP).*\((SQ ).*(\(((AUX)|(MD)) [^)]+\) \(RB ((not)|(n\'t))).*(\. \?\)))+?)',
		# Two word combination
		'S1':r'((\(S..*\(\. [.!?]\))+?)',
		# Subject verb sequence
		'S2':r'(\n?.*?\(S ((\(NP [^\n]*\(VP.*\n?)))',
		# Verb object sequence 
		'S3':r'(\n?.*?(\(VP.*?\(NP.*\n?))',
		# Subject Verb Object Sequence
		'S4':r'(\n?.*?\(S ((\(NP [^\n]*\(VP.*?\(NP.*\n?)))',
		# Conjunction(any)
		#'S5':r'(S. .*((\(CC)|((?<!\(PP )\(IN(?= ([^)]+)\) \(S))) ([^)]+)\).*\(\. [!?.]\))+?',
		'S5':r'(S. .*((((\(CC)|((?<!\(PP )\(IN(?= ([^)]+)\) \(S))) ([^)]+)\))|(\(CONJP( \([A-Z$1-9]+ [^)]+\))+\))).*\(\. [!?.]\))+?',
		# Sentence with two VP's
		'S6':r'((\(S. .*(.*(\((VB|VBZ|VBP|VBN|VBD) ([^)]+)\).*?){2,}.*)\(\. [.!?]\))+?)',
		# Conjoined phrases
		'S7':r'((\(S. .*?\([A-Z]+ (\((?P<i>[A-Z]{2,})[A-Z$]? [^)(]+\)(( \(CC [^)]+\) \((?P=i).{,2} [^()]+\)))+)\)?.*\(\. [.!?]\))+?)',
		# Infinitive without catenative marked with to
		'S8':r'((S. .*(\(VP.*?(?=\((VB[GPNZD]?)|(AUX) ).*?\(VP.*?TO.*(?=\(VP.*?\(((VB)|(AUX)) ).*\(\. [!?.]\)))+?)',
		# Let/Make/Help/Watch introducer
		'S9':r'((\(S. (\([A-Z$1-9]+ )+(\(((RB)|(UH)) [^()]+\)+ )?\(VP \(VB (([Ll]et)|([Hh]elp)|([Mm]ake))\).*\((VB|VBD|VBZ|VBN|VBP|VBG|AUX).*\(\. [.?!]\))+?)',
		# Adverbial Conjunction
		'S10':r'(S. .*((((\(CC)|((?<!\(PP )\(IN(?= ([^()]+)\) \(S))) ([^()]+)\))|(\(CONJP( \([A-Z$1-9]+ [^()]+\))+\))).*\(\. [!?.]\))+?',
		# Propositional Complement
		# Need to get a list of words
		'S11':r'(\(S1.*\(VP \(VB.? ((mean)|(forget)|(forgot)|(say)|(said)|(tell)|(told)|(guess)|(know)|(knew)|(remember)|(wonder)|(judj)|(use)|(using)|(show)|(think)|(thought))[^()]*\) (\(SBAR ((\([A-Z]+ )+\([A-Z$]+ [^()]+\)\) )?\(S \(NP.*)\(\. [.!?]\))+?',
		# Conjoined sentences (Except for imperatives, will usually have subj + predicate in each clause)
		#Left to consider Wh conjunctives - right now have considered CC and IN conjunctives
		'S12':r'(S. (((?=\(((S)|(SBAR)|(SBARQ)|(SINV)|(SQ)|(VP)) )(.*)(((?<=\){2} )\(CC)|((?<!\(PP )\(((S)|(SBAR)|(SBARQ)|(SINV)|(SQ)|(VP)) IN(?= ([^)]+)\) \(S))) [^)]+\) (\((S|SBAR|SBARQ|SINV|VP) .*))+)\(\. [.!?]\))+?',
		# Wh-clause
		'S13':r'((\(S. .*\(((SBAR(Q)?)|SINV|SQ|S) \(((WHNP)|(WHADJP)|(WHADVP)|(WHPP)).*\(\. [.!?]\))+?)',
		# Bitransitive predicate
		'S14':r'(\(S1.*(\(VP (\(VB[GDPNZ]? [^()]+\))+\)* *\(NP (\([A-Z]+ [^()]+\))+\) *?(\(PP \(((IN)|(TO)) ((to)|(for))]+\) )?\(NP \((?!RB)[A-Z]+ (?!(tonight)|(tomorrow)|(today))[^()]+\)( \([A-Z]+ [^()]+\))*\)* *?.*)\(\. [.!?]\))+?',
		# Sentence with three or more VPs
		'S15':r'((\(S..*(.*(\((VB|VBZ|VBP|VBN|VBD|AUX) ([^)]+)\).*){3,}.*)\(\. [.!?]\))+?)',
		# Relative clause marked or unmarked
		'S16':r'(\(S1 .*?(\(NP .*?(\(SBAR (?!\(IN ).*?\(S .*))+\(\. [?.!]\)+)+?',
		# Infinitive clause new subject
		'S17':r'(\(S1.*\(VP( \((?!VBG)[A-Z]+ [^()]+\))+( (\(S )\(NP( \([A-Z$]+ [^()]+\))+\)+ *\(VP \(TO to\) \(VP \(((VB)|(AUX)) [^()]+\).*)\(\. [?!.]\))+?',
		# Gerund
		'S18':r'((\(.*\(VBG.*\(\. [.!?]\))+?)',
		# Fronted or center-embedded subordinate clause
		'S19':r'((\(.*?(\(SBAR (\(IN [^)]+\) )?\(S.*)\(\. [?.!]\)+)+?)',
		# Other: e.g passive constructions e.g tag comments/intrusions
		'S20':r''
	}
Nouns=["N1","N2","N3","N4","N5","N6","N7","N8","N9","N10","N11","N12"]
Verbs=["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17"]
Questions=["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11"]
Sentences=["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13","S14","S15","S16","S17","S18","S19","S20"]
Description={
		'N1':"Proper Mass or Count Noun",
	    	'N2':"Pronoun,Prolocative excluding modifiers",
		'N3':"Modifier including adjectives, possessives and quantifiers",
		'N4':"Two word NP preceded by article or modifier",
		'N5':"Article used before a noun",
		'N6':"Two word NP(as in N4) after verb or preposition",
		'N7':"Plural suffix",
		'N8':"Two word NP (as in N4 before verb)",
		'N9':"Three word NP (Det-Mod-N or Mod-Mod-N)",
		'N10':"Adverb modifying adjective or nominal",
		'N11':"Any other bound morpheme on N or adjective(if judged not to be stored as lexical unit",
		'N12':"Others",
		'V1':"Verb",
		'V2':"Particle or preposition",
		'V3':"Prepositional Phrase (Prep+NP)",
		'V4':"Copula linking two nominals (nominal + copula + nominal, copula)",
		'V5':"Catenative (pseudo-auxiliary) preceeding a verb (catenative,verb)",
		'V6':"Auxiliary be, do, have in VP",
		'V7':"Progressive Suffix",
		'V8':"Adverb",
		'V9':"Modal preceeding verb",
		'V10':"Third person singular present tense suffix",
		'V11':"Past tense modal",
		'V12':"Regular past tense suffix",
		'V13':"Past tense auxiliary",
		'V14':"Medial adverb",
		'V15':"Copula, Modal or Auxiliary used for emphasis or ellipsis(uncontractible context)",
		'V16':"Past tense copula",
		'V17':"Bound morpheme on a verb or an adjective(to make an adverb)",
		'Q1':"Intonationally marked question",
		'Q2':"Routine do/go existence name question or wh-pronoun alone",
		'Q3':"Simple Negation +X ) neg=no(t), can't don't X=NP,PP,VP,Adj, Adv etc",
		'Q4':"Initial Wh-pronoun followed by verb",
		'Q5':"Negative Morpheme between subject and verb",
		'Q6':"Wh-question with inverted modal, copula or auxillary",
		'Q7':"Negation of copula, modal or auxiliary",
		'Q8':"Yes/no question with inverted modal, copula or auxiliary",
		'Q9':"Why, When, Which, Whose",
		'Q10':"Tag Question",
		'Q11':"Other: e.g questions with negation and inverted cop/aux/modal",
		'S1':"Two word combination",
		'S2':"Subject verb sequence",
		'S3':"Verb object sequence",
		'S4':"Subject Verb Object Sequence",
		'S5':"Conjunction (any)",
		'S6':"Sentence with two VP's",
		'S7':"Conjoined phrases",
		'S8':"Infinitive without catenative, marked with to",
		'S9':"Let/Make/Help/Watch introducer",
		'S10':"Adverbial Conjunction",
		'S11':"Propositional Complement",
		'S12':"Conjoined sentences (Except for imperatives, will usually have subj + predicate in each clause)",
		'S13':"Wh-clause",
		'S14':"Bitransitive predicate",
		'S15':"Sentence with three or more VPs",
		'S16':"Relative clause marked or unmarked",
		'S17':"Infinitive clause new subject",
		'S18':"Gerund",
		'S19':"Fronted or center-embedded subordinate clause",
		'S20':"Other: e.g passive constructions e.g tag comments/intrusions"
	}
		

