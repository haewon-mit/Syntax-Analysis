/*
 * Copyright 1999, 2005 Brown University, Providence, RI.
 * 
 *                         All Rights Reserved
 * 
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose other than its incorporation into a
 * commercial product is hereby granted without fee, provided that the
 * above copyright notice appear in all copies and that both that
 * copyright notice and this permission notice appear in supporting
 * documentation, and that the name of Brown University not be used in
 * advertising or publicity pertaining to distribution of the software
 * without specific, written prior permission.
 * 
 * BROWN UNIVERSITY DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
 * INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY
 * PARTICULAR PURPOSE.  IN NO EVENT SHALL BROWN UNIVERSITY BE LIABLE FOR
 * ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#include <fstream>
#include <iostream>
#include <unistd.h>
#include <math.h>
#include "GotIter.h"
#include "Wrd.h"
#include "InputTree.h"
#include "Bchart.h"
#include "ECArgs.h"
#include "MeChart.h"
#include "extraMain.h"
#include "AnsHeap.h"
#include "UnitRules.h"
#include "Params.h"
#include "TimeIt.h"
#include "ewDciTokStrm.h"

MeChart* curChart;
Params 		    params;

int
main(int argc, char *argv[])
{
   ECArgs args( argc, argv );
   /* l = length of sentence to be proceeds 0-100 is default
      n = work on each #'th line.
      d = print out debugging info at level #
      t = report timings */

   params.init( args );
   TimeIt timeIt;
   ECString  path( args.arg( 0 ) );
   generalInit(path);

   int      sentenceCount = 0;  //counts all sentences so we can use e.g,1/50;
   int totUnparsed = 0;
   double log600 = log2(600.0);

   ewDciTokStrm testSStream(args.arg(1));
   assert(!(!testSStream));
   for( ; !(!testSStream) ; sentenceCount++)
     {
       SentRep sr(testSStream, SentRep::SGML);
       int len = sr.length();
       if(len > params.maxSentLen) continue;
       if(len == 0) break;
       if( !params.field().in(sentenceCount) ) continue;

       if(args.isset('t')) timeIt.befSent();

       MeChart*	chart = new MeChart( sr );
       curChart = chart;
       
       if(args.isset('t') ) timeIt.lastTime = clock();

       chart->parse( );

       Item* topS = chart->topS();
       if(!topS)
	 {
	   totUnparsed++;
	   cerr << "Parse failed - parseIt.C" << endl;
	   cerr << sr << endl;
	   delete chart;
	   continue;
	 }
       if(args.isset('t') ) timeIt.betweenSent(chart);

       // compute the outside probabilities on the items so that we can
       // skip doing detailed computations on the really bad ones 
       chart->set_Alphas();

       AnsTreeStr& at = chart->findMapParse();
       if( at.probs[0] <= 0 ) error( "mapProbs did not return answer" );

       if(Feature::isLM)
	 {
	   double lgram = log2(at.sum);
	   lgram -= (sr.length()*log600);
	   double pgram = pow(2,lgram);
	   double iptri =chart->triGram();;
	   double ltri = (log2(iptri)-sr.length()*log600);
	   double ptri = pow(2.0,ltri);
	   double pcomb = (0.667 * pgram)+(0.333 * ptri);
	   double lmix = log2(pcomb);
	   cout << lgram << "\t" << ltri << "\t" << lmix << "\n";
	 }

       int numVersions = 0;
       for(numVersions = 0 ; numVersions < NTH ; numVersions++)
	 if(at.probs[numVersions] <= 0) break;
       if(NTH > 1)cout << sentenceCount << "\t" << numVersions << "\n";
       for(int i = 0 ; i < numVersions ; i++)
	 {
	   short pos = 0;
	   InputTree*  mapparse = inputTreeFromAnsTree(&at.trees[i], pos ,sr);
	   double logP =log(at.probs[i]);
	   logP -= (sr.length()*log600);
	   if(NTH > 1) cout <<  logP << "\n";
	   cout << *mapparse << "\n\n";
	   delete mapparse;
	 }
       cout << endl;
       if(args.isset('t') ) timeIt.aftSent();

       delete chart;
     }
   if( args.isset('t') ) timeIt.finish(sentenceCount);

   return 0;
}
