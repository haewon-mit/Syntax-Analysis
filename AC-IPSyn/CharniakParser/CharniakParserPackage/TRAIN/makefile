
#CFLAGS=-I/pro/include/stl -I/opt/SUNWspro/SC4.2/

.C.o:
	g++ $(CFLAGS) -c -O $<
 
RCOUNTS_OBJS = \
	ClassRule.o \
	ECArgs.o \
	EmpNums.o \
	Feat.o \
	Feature.o \
	FeatureTree.o \
	InputTree.o \
	Pst.o \
	Phegt.o \
	Term.o \
	auxify.o \
	ccInd.o \
	headFinder.o \
	treeHistSf.o \
	utils.o \
	rCounts.o


rCounts: $(RCOUNTS_OBJS)
	g++ $(CFLAGS) $(RCOUNTS_OBJS) -o rCounts 
 
RMCOUNTS_OBJS = \
	ECArgs.o \
	EmpNums.o \
	Feat.o \
	Feature.o \
	FeatureTree.o \
	InputTree.o \
	Pst.o \
	Phegt.o \
	Term.o \
	ccInd.o \
	headFinder.o \
	treeHistSf.o \
	utils.o \
	Bllip99Iter.o \
	rMCounts.o


rMCounts: $(RMCOUNTS_OBJS)
	g++ $(CFLAGS) $(RMCOUNTS_OBJS) -o rMCounts 

ISCALE_OBJS = \
	ECArgs.o \
	Feat.o \
	Feature.o \
	FeatureTree.o \
	FeatIter.o \
	FeatTreeIter.o \
	Phegt.o \
	Term.o \
	headFinder.o \
	utils.o \
	iScale.o


iScale: $(ISCALE_OBJS)
	g++ $(CFLAGS) $(ISCALE_OBJS) -o iScale 
 
SELFEATS_OBJS = \
	ECArgs.o \
	Feat.o \
	Feature.o \
	FeatureTree.o \
	FeatIter.o \
	FeatTreeIter.o \
	Pst.o \
	Phegt.o \
	Term.o \
	headFinder.o \
	utils.o \
	selFeats.o


selFeats: $(SELFEATS_OBJS)
	g++ $(CFLAGS) $(SELFEATS_OBJS) -o selFeats 

 
TRAINRS_OBJS = \
	ClassRule.o \
	ECArgs.o \
	EmpNums.o \
	Feat.o \
	Feature.o \
	FeatureTree.o \
	InputTree.o \
	Pst.o \
	Phegt.o \
	Smoother.o \
	Term.o \
	auxify.o \
	ccInd.o \
	headFinder.o \
	treeHistSf.o \
	utils.o \
	trainRs.o


trainRs: $(TRAINRS_OBJS)
	g++ $(CFLAGS) $(TRAINRS_OBJS) -o trainRs 

 
KN3COUNTS_OBJS = \
	ClassRule.o \
	ECArgs.o \
	EmpNums.o \
	Feat.o \
	Feature.o \
	FeatIter.o \
	FeatTreeIter.o \
	FeatureTree.o \
	InputTree.o \
	Pst.o \
	Phegt.o \
	Term.o \
	auxify.o \
	ccInd.o \
	headFinder.o \
	treeHistSf.o \
	utils.o \
	kn3Counts.o


kn3Counts: $(KN3COUNTS_OBJS)
	g++ $(CFLAGS) $(KN3COUNTS_OBJS) -o kn3Counts 

AUXIT_OBJS = \
	BrownIter.o \
	EmpNums.o \
	ECArgs.o \
	InputTree.o \
	Term.o \
	headFinder.o \
	utils.o \
	auxify.o \
	auxIt.o

auxIt: $(AUXIT_OBJS)
	g++ $(AUXIT_OBJS) -o auxIt


PSGT_OBJS = \
	ECArgs.o \
	EmpNums.o \
	InputTree.o \
	Term.o \
	auxify.o \
	headFinder.o \
	utils.o \
	UnitRules.o \
	pSgT.o

pSgT: $(PSGT_OBJS)
	g++ $(PSGT_OBJS) -o pSgT


PTGNT_OBJS = \
	ECArgs.o \
	EmpNums.o \
	InputTree.o \
	Pst.o \
	Phegt.o \
	Term.o \
	headFinder.o \
	utils.o \
	pTgNt.o

pTgNt: $(PTGNT_OBJS)
	g++ $(PTGNT_OBJS) -o pTgNt

PUGT_OBJS = \
	ECArgs.o \
	EmpNums.o \
	InputTree.o \
	Pst.o \
	Phegt.o \
	Term.o \
	auxify.o \
	headFinder.o \
	utils.o \
	pUgT.o

pUgT: $(PUGT_OBJS)
	g++ $(PUGT_OBJS) -o pUgT



