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

#include "ccInd.h"
#include "InputTree.h"
#include "Term.h"
#include "Feature.h"

int
ccIndFromTree(InputTree* tree)
{
  InputTreesIter  subTreeIter = tree->subTrees().begin();
  ECString trm = tree->term();
  bool sawComma = false;
  bool sawColen = false;
  bool sawCC = false;
  bool sawOTHNT = false;
  int numTrm = 0;
  int pos = 0;
  int tint = Term::get(trm)->toInt();

  /*Change next line to indicate which non-terminals get specially
    marked to indicate that they are conjoined together */
  if(trm != "NP" && trm != "S" && trm != "VP") return tint;
  for( ; subTreeIter != tree->subTrees().end() ; subTreeIter++ )
    {
      InputTree* subTree = *subTreeIter;
      ECString strm = subTree->term();
      //Change next two lines depending on possible conjunction parts of speech
      ECString CCInd[2] = {"CC", "CONJP"};
      if(pos != 0 && (strm == CCInd[0] || strm == CCInd[1])) sawCC = true;
      else if(strm == trm) numTrm++;
      else if(pos != 0 && (strm == ",")) sawComma = true;
      else if(pos != 0 && (strm == ":")) sawColen = true;
      //else if(!scorePunctuation(strm)) return tint;
      else if(!Term::get(strm)->terminal_p()) sawOTHNT = true;
      pos++;
    }
  if(trm == "NP" && numTrm == 2 && !sawCC) return Term::lastNTInt()+1;
  if((sawComma || sawColen || sawCC) && numTrm >= 2) return tint+Term::lastNTInt();
  return tint;
}
