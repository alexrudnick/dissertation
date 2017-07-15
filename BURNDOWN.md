## general

We want to make it faster to train classifiers, and I suspect that the issue
here is that it takes a long time to get the relevant training data. So maybe
what we should do is list the words for which we know we'll need a classifier
ahead of time, then on loading the training data, stick the relevant sentences
in memory where we can get them *quickly*. Then on demand, just extract features
from those sentences.  We're going to need to store multilingual corpora here
too, to do the multilingual features.

Wait, did we already do that?

## monolingual

### things left undone

  * finish up analysis and writeup
  * make charts & graphs
  * word2vec features
    * what window to use?
    * vector combination: weighted sum of the vectors, weighting words closer to
    the focus word more.
  * doc2vec features
    * does it even really make sense to use doc2vec by itself? is the meaning
    of the sentence as a whole what we want, for classifying a particular token
    usage?
    * understand and explain the doc2vec paper (cited in dissertation)
      * how does training data size affect quality?
    * turn inferred document vectors into features for classification
    * run experiments with doc2vec features

### fairly done things
  * DONE making it easier to experiment with different featuresets
  * DONE add brown clusters as features
  * DONE pos tags?
    * still need to redo pos tag experiments? ...
  * parse features if that's not too hard
    * DONE syntactic head like "head:lemma"
    * DONE also "head:surface"
    * DONE syntactic child if any, as above
    * DONE going to need to write an annotator that goes through and adds these
    to tokens, having run <del>freeling</del> MaltParser on the input
    sentence.
      * DONE question here is whether it's going to be easier to use FreeLing again,
      or some other parser. Maybe MaltParser? Extract dependencies out of the
      CONLL format?
      * DONE for running MaltParser, we want to also get coarse POS tags,
      specifically ones in the Universal Tag Set. Where do we find a conversion
      table for that tag set? What tag set is it even?
        * DONE these seem really close to the universal POS tags anyway. If there's
        no conversion table written down, we can just make one ourselves.
    * SKIP Alternatively, the POS tags are generated during the initial "annotated"
    file generation, so maybe we could do it in a similar way?
      * SKIP Find out what the "parsed" format looks like for FreeLing.
  * word2vec features
    * DONE how best to combine vectors for different words: addition seems to
      be the done thing.
    * DONE is it best to have vectors over lemmas or surface forms? lowercasing?
      * DONE almost certainly surface forms -- that's kind of the point of these semi-supervised things.
      * DONE also probably keep case. case has meaning.
    * DONE It is really silly to include the word vectors in the annotated corpus
      file.
      * DONE just pass the vector file as an argument and load it into memory.
    * DONE how do you get the complete set of phrases out of a word2phrase run?
    * DONE then how do you find the phrases that cover an input sentence?
      * DONE just greedily take the longest first, that's not too hard
    * DONE more importantly: how to safely replace sequences of tokens on source
    side with the MWEs that we know about without messing up indices into the
    sentences? --> it doesn't seem to be that hard, really. Just have to do the
    substitution and then recompute the source-side index after the fact.
      * FIXED does this sometimes introduce a problem in the training data
      though? --> have to keep track of the surface form, not the lemma.
        * REALLY FIXED worse than that -- the "surface form" might contain
        underscores because it was an MWE found my earlier preprocessing.
    * You want to take the word vectors from the sentence and combine them
    into a vector representing the current context. There are several things you
    could try to do this combination:
      * DONE Take a sum of the vectors for the whole sentence
      * DONE Just take a sum of the vectors in some window
      * MAYBE SKIP? Weight word vectors by their tf/idf or similar.
  * DONE learn how to train doc2vec
    * does it even really make sense to use doc2vec by itself? is the meaning
    of the sentence as a whole what we want, for classifying a particular token
    usage?
    * understand and explain the doc2vec paper (cited in dissertation)
    * DONE learn how to train doc2vec from Spanish wikipedia!!
    * DONE be able to load up saved models
    * DONE how much text do we use to train a model?
      * DONE how much can we fit in memory for training?
        * we can fit Spanish wikipedia
      * how does training data size affect quality?
    * turn inferred document vectors into features for classification
    * CONCEPTUALLY DONE there's just one vector per sentence, so there's your
    feature vector.

## multilingual
  * train systems to target any other European languages we can get a
  target-language stemmer for. Anything snowball is fair game, maybe? We don't
  even really need a proper lemmatizer.
Then use output of those systems as features.
  * This is our "classifier stacking" approach, or basically "L2".  What did we
  do in the semeval paper, exactly? We trained on the real answers and tested
  on the classifier answers, right?
  * But we should train on classifier output.
  * And furthermore, what we can do is just run the classifiers in "annotator"
  mode -- we blow through an input file and we classify with an existing
  classifier, then just save the classifier as an annotation.
  * What we're going to need to do is build preprocessing for Europarl. We need
  to get Europarl text into the format the Chipa expects.

That looks like...
  * need lemmatizers and perhaps POS taggers.

## sequence
CANCELED!!

## combinations
  * try combinations.

## integration
hack up squoia again if necessary

  * CANCELED! build tiniest possible cdec system for es-gn (switched to moses)
  * SKIP Learn to use CMU's morphogen or whatever it's called -- or we could
  just punt and target lemmatized gn.
  * DONE built tiny pb-smt system for es-gn, now pretty good at spinning these
  things up.

  * HARD How hard is it to do phrase-based for cdec? We need to figure out how
  to load PB-SMT tables. Also how to build them . Can cdec tools even generate
  them?

  * pull all gn text from guarani-nee and gn-wikipedia.
  * train surface and lemmatized LMs.

  * SKIP Port cdec-as-python-module stuff to py3k.
  * STARTED Add chipa as phrase table feature 

## outro
  * Look, it's some experiments!
  * Some of them worked!
  * Probably better to crowdsource and get some respectable amount of data
  rather than just using the Bible, unless your language is actually extinct.
  * Hey-o, now I'm a doctor!