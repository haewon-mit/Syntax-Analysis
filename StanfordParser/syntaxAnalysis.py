import os
import nltk
from nltk import tokenize
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import CFG
from nltk.tag.stanford import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree
from nltk.parse.stanford import StanfordDependencyParser

# parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
#
# sent = [['The', 'big', 'dog', '.'],['The', 'big', 'dog', '.']]
#
# p = parser.parse_sents(sent)
#
# # for tree in (p):
# #     print(list(tree))
#
# for line in p:
#     for sentence in line:
#         sentence.draw()
#
# sent = "the big dog."
#
# p = parser.raw_parse(sent)
#
# # for tree in (p):
# #     print(list(tree))
#
# for line in p:
#     for sentence in line:
#         sentence.draw()




st=StanfordPOSTagger('english-bidirectional-distsim.tagger')
parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

# setup corpus of texts
childStoryCorpusDir = '../resources/org_transcripts'
robotStoryCorpusDir = '../resources/robot_stories'

childStoryCorpus = PlaintextCorpusReader(childStoryCorpusDir, ".*\.txt")
robotStoryCorpus = PlaintextCorpusReader(robotStoryCorpusDir, ".*\.txt")


# average word length, average sentence length, and the number of times each vocabulary item appears in the text on average (our lexical diversity score)
# for fileid in childStoryCorpus.fileids():
#     num_chars = len(childStoryCorpus.raw(fileid))
#     num_words = len(childStoryCorpus.words(fileid))
#     num_sents = len(childStoryCorpus.sents(fileid))
#     num_vocab = len(set([w.lower() for w in childStoryCorpus.words(fileid)]))
#     print ((float(num_chars)/float(num_words)), float(num_words)/float(num_sents), float(num_words)/float(num_vocab), fileid)


for fileid in childStoryCorpus.fileids():

    print (fileid)
    file_path = os.path.join(childStoryCorpusDir, fileid)

    with open(file_path, 'r') as orgf:
        for line in orgf:
            for s in tokenize.sent_tokenize(line):
                print(s)
                #print(st.tag(tokenize.word_tokenize(s)))
                #print(st.tag(s.split()))
                print(list(parser.raw_parse(s)))

                # for line in parser.raw_parse(s):
                #     for sentence in line:
                #         sentence.draw()

    #s = robotStoryCorpus.sents(fileid))
    # for s in robotStoryCorpus.sents(fileid):
    #     print (s)
    #     sentences = parser.parse_sents(s)
    #
    #     for tree in sentences:
    #         list(tree)

        # for line in sentences:
        #     for sentence in line:
        #         sentence.draw()

        #for tree in rst:
         #   print(tree)
    # for s in childStoryCorpus.sents(fileid):
    #     print(s)
    #     #print(st.tag(s))
    #     rst = GenericStanfordParser.parse_sents(s)
    #     for tree in rst:
    #         print(tree)







# for infile in sorted(childStoryCorpus.fileids()):
#     print infile
#
# raw_input()
#
# all_text = childStoryCorpus.raw()
#
# print all_text


    # print os.path.abspath(infile)
    # if infile.startswith("sr2"):
    #     with childStoryCorpus.open(infile) as fin:
    #         print fin.read().strip()