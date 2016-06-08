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

#ifndef TERM_H
#define TERM_H

#include "ECString.h"
#include <list>
#include <map>
#include <assert.h>
#include <iostream>
#include <fstream>

class Term;

typedef Term *		Term_p;
typedef const Term *	Const_Term_p;
typedef const Term     ConstTerm;

#define Terms list<ConstTerm*>
#define ConstTerms const list<ConstTerm*>
#define TermsIter list<Term*>::iterator
#define ConstTermsIter list<ConstTerm*>::const_iterator
typedef map<ECString, Term*, less<ECString> >  TermMap;

class Term 
{
public:
    Term();			// provided only for maps.
    Term( const ECString s, int terminal, int n );
    Term( const Term& src );
    int              toInt() const { return num_; }
    const ECString& name() const {  return name_;  }
    int	  terminal_p() const { return terminal_p_; }
    friend ostream& operator<< ( ostream& os, const Term& t );
    friend ostream& operator>> ( istream& os, const Term& t );
    int		operator== (const Term& rhs ) const;
    bool   isPunc() const { return (terminal_p_ == 2) ? true : false ; }
    bool   openClass() const { return (terminal_p_ == 3) ? true : false ; }
    static Const_Term_p get(const ECString& getname);
    static void  init(ECString & prefix);
    static const Term* fromInt(int i) 
      { assert(i < 400); return array_[i]; }
    static int  lastTagInt() { return lastTagInt_; }
    static int  lastNTInt() { return lastNTInt_; }
    static Term* stopTerm;
    static Term* startTerm;
    static Term* rootTerm;
private:
    ECString* namePtr() { return (ECString*)&name_; }
    int    	terminal_p_;
    int		num_;
    const ECString name_;
    static Term*  array_[400];
    static TermMap termMap_ ;
    static int    lastTagInt_;
    static int    lastNTInt_;
};
  

#endif /* ! TERM_H */
