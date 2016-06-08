#include <unistd.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
//#include <iomanip.h>
#include <signal.h>
#include <assert.h>
#include "ECArgs.h"
#include "utils.h"
#include "ECString.h"
//#include <ngram.h>
#include "ParseStats.h"



// Local types


// Global objects
//
//		(or object wannabes)
//

#define MAXN 10


// Misc utility functions.
//

void
usage( char * program )
{
    cerr << program << " usage: " << program
      << " [-w Wordtype] [ <file_prefix> ]" << endl;
    exit( 1 );
}


double lambda_ngram;
double lambda_grammar;
int train_lambdas( ifstream& sentenceStream);
void compute_lambdas(double probs[][2], int num_sents, ofstream& ostrm);

int
  main(int argc, char *argv[])
{
   ECArgs args(argc, argv);
   if( args.nargs() > 1 )	// max one filename allowed.
     usage( *argv );
   
   ECString path = args.arg(0);

   cout.precision(5);

   int totSents = 0;
   int totUnparsed = 0;
   
   ECString fileString(path);
   fileString += "PStats.txt";
   ECString      parseStatsString( fileString );
   ifstream    parseStatsStream( parseStatsString.c_str() );
   if( !parseStatsStream ) error( "unable to open parseStats stream." );

   ParseStats totals;
   while( parseStatsStream )
     {
       int len;
       parseStatsStream >> len;
       if(!parseStatsStream) break;
       if(len == 9999)
	 {
	   int tot;
	   parseStatsStream >> tot;
	   totSents += tot;
	   parseStatsStream >> tot;
	   totUnparsed += tot;
	   continue;
	 }
       
       if(!parseStatsStream) break;
       ParseStats temp;
       parseStatsStream >> temp;
       totals += temp;
     }
   cout << "\n";
   cout << "Tot sentences: " << totSents << "\t";
   cout << "Tot unparsed: " << totUnparsed << "\n";
   cout << "\n" << totals << "\n";
   float precision = (float)totals.numCorrect/(float)totals.numInGuessed;
   float recall = (float)totals.numCorrect/(float)totals.numInGold;
   cout << "Precision: " << precision << "\n";
   cout << "Recall:    " << recall << "\n";
   cout << "F-Measure: " <<(2*precision*recall)/(precision+recall) <<"\n";
   return 0;  
 }

