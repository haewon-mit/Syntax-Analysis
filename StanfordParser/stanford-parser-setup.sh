# Requires JDK 1.8
wget http://nlp.stanford.edu/software/stanford-parser-full-2015-12-09.zip
wget http://nlp.stanford.edu/software/stanford-english-corenlp-2016-01-10-models.jar
wget http://nlp.stanford.edu/software/stanford-ner-2015-12-09.zip
wget http://nlp.stanford.edu/software/stanford-postagger-full-2015-12-09.zip

unzip stanford-parser-full-2015-12-09.zip
unzip stanford-ner-2015-12-09.zip
unzip stanford-postagger-full-2015-12-09.zip

export STANFORDTOOLSDIR=$HOME/Dropbox/PycharmProjects/lib/

mv stanford-parser-full-2015-12-09/ stanford-ner-2015-12-09/ stanford-postagger-full-2015-12-09/ stanford-english-corenlp-2016-01-10-models.jar $STANFORDTOOLSDIR

export CLASSPATH=$STANFORDTOOLSDIR/stanford-parser-full-2015-12-09/stanford-parser.jar:$STANFORDTOOLSDIR/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar:$STANFORDTOOLSDIR/stanford-ner-2015-12-09/stanford-ner.jar:$STANFORDTOOLSDIR/stanford-postagger-full-2015-12-09/stanford-postagger.jar:$STANFORDTOOLSDIR/stanford-english-corenlp-2016-01-10-models.jar

export STANFORD_MODELS=$STANFORDTOOLSDIR/stanford-ner-2015-12-09/classifiers:$STANFORDTOOLSDIR/stanford-postagger-full-2015-12-09/models

echo $CLASSPATH
echo $STANFORD_MODELS


rm stanford-parser-full-2015-12-09.zip stanford-ner-2015-12-09.zip stanford-postagger-full-2015-12-09.zip




