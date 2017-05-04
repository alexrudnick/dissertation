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
  * DONE making it easier to experiment with different featuresets
  * DONE add brown clusters as features
  * DONE pos tags?
  * DONE add word2vec features
    * should figure out best features to extract from word2vec, though
    * what window to use? how best to combine vectors for different words?
    * DONE is it best to have vectors over lemmas or surface forms? lowercasing?
      * almost certainly surface forms -- that's kind of the point of these semi-supervised things.
      * also probably keep case. case has meaning.
    * It is really silly to include the word vectors in the annotated corpus
      file.
      * TODO: just pass the vector file as an argument and load it into memory.
    * make feature extractors use word2vec phrases.
      * how do you get the complete set of phrases out of a word2phrase run?
      * then how do you find the phrases that cover an input sentence?
  * For word2vec, one major interesting question is how are we going to use
  those features? What do they do in the word representations paper? The open
  question is how you use word representation to model a context?
    * You want to take the word vectors from the sentence and combine them
    into a vector representing the current context. There are several things you
    could try to do this combination:
      * DONE Just take a sum of the vectors in some window
      * Take a sum of the vectors for the whole sentence
      * Take a sum of the vectors for the sentece, but weight words closer to
      the current focus word more, like attenuate the weight as you get farther
      out.
      * Weight word vectors by their tf/idf or similar. (wait what? that doesn't sound like a great idea)
  * learn how to train doc2vec
    * DONE-ish understand the doc2vec paper (cited in dissertation)
    * DONE learn how to train doc2vec from Spanish wikipedia!!
    * DONE be able to load up saved models
    * how much text do we use to train a model?
      * DONE how much can we fit in memory for training?
        * we can fit Spanish wikipedia
      * how does training data size affect quality?
    * turn inferred document vectors into features for classification
    * there's just one vector per sentence, so just turn that into one feature
      per vector dimension, and the classifier for the individual lemma can
      figure out what to do with each dimension.
  * parse features if that's not too hard?

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
