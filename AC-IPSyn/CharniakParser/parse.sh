#! /bin/sh
if [ "$1" = "" ] ; then
   echo "Usage is:"
   echo " "
   echo "parse.sh input-file output-file"
   exit
fi
if [ "$2" = "" ] ; then
   echo "Usage is:"
   echo " "
   echo "parse.sh input-file output-file"
   exit
fi
# set some parameters for the run. modified to -s hard by haewon
ulimit -s hard
renice 5 $$
#
# Parser output processing - one sentence per line (no indentation)
#
./CharniakParser/punctuation_sep $1 > /tmp/parse.$$
perl -pi -e 's/^(.*)\n/<s> $1 <\/s>\n/g' /tmp/parse.$$

# Parse it with Charniak parser
./CharniakParser/parseIt ./CharniakParser/DATA/ /tmp/parse.$$ > $2

perl -pi -e 's/^\(S1(.*)/\n\(S1$1/g' $2
perl -pi.bak -e 's/^(\s+)(\S)(.*)\n/$2$3\n/g' $2
perl -pi -e 's/\((\S+)/\( $1/g' $2
perl -pi -e 's/(\S+)\)/$1 \)/g' $2

##If you want one sentence per line
perl -pi -e 's/^(\s+)(.+)\n/ $2\n/g' $2
perl -pi -e 's/(.+)\n/$1/g' $2
perl -pi -e 's/\( /\(/g' $2
perl -pi -e 's/ \)/\)/g' $2
perl -pi -e 's/  / /g' $2
perl -pi -e 's/\n/\n\n/g' $2
perl -pi -e 's/\)\(/\) \(/g' $2

rm -f /tmp/parse.$$
