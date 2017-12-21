# things left undone

## general
  * SKIP? be able to draw curves of word training data size versus accuracy

## monolingual

## multilingual
  * pick languages we want to use
    * freeling supports: cs, de, en, es, fr, it, nb, pt, ru, sl... so plenty
  * make scripts for preparing data for Europarl for all the European languages
  we think we're going to do. Should be basically like the en-es data
  preparation script.
    * DONE pick lemmatizer/stemmer to use (can just use FreeLing!)
  * make an annotation script to stick classifier answers on all words we have a
  classifier for.
  * make features out of those annotations

  * This is roughly our "classifier stacking" approach, or basically "L2",
  except that in the semeval paper we trained on the real answers and tested on
  classifier answers, which was goofy

  * And furthermore, what we can do is just run the classifiers in "annotator"
  mode -- we blow through an input file and we classify with an existing
  classifier, then just save the classifier as an annotation.
    * notably, we want to write down the answer *on the particular token* that
    we are going to try to classify later -- it is not a property of the
    sentence as a whole. The sentence as a whole is not a classification
    problem; it could have multiple different tokens that need to get
    classified.
  * What we're going to need to do is build preprocessing for Europarl. We need
  to get Europarl text into the format the Chipa expects and aligned in the same
  way as the bibles.

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


# fairly done things

  * DONE maybe rerun the experiments from the baseline chapter so we know that the results are comparable; we're using explicit lists of top words now.

## baseline done things
  * DONE make sure results reported in baseline" chapter are generated on the same test sets and same process as "monolingual"
  * DONE do we need to rerun es-en and en-es for that reason? probably?
  * DONE update discussion in "baseline" chapter to make sure it matches
  reported results

## monolingual done things
  * DONE run experiments for brown clusters AND syntactic features at once
  * DONE try combinations of default features with embeddings.
    * DONE shouldn't be hard: calculate embeddings as before, just add those as some
    more features, right? One feature per dimension, just loop over the
    dimensions.
  * run experiments for brown clusters
    * DONE always use feature prefixes, just cite Turian et al as explanation
    * DONE europarl clusters
    * DONE europarl lemma clusters
    * DONE wikipedia clusters
    * DONE wikipedia lemma clusters
  * SKIP clean and rationalize code for brown cluster features a bit.
  * doc2vec things...
    * DONE turn inferred document vectors into features for classification
      * DONE probably just stick an annotation on the first token in the sentence
    * DONE run experiments with doc2vec features
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
    * DONE vector combination: weighted sum of the vectors, weighting words closer to the focus word more.
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
    * DONE understand and explain the doc2vec paper (cited in dissertation)
    * DONE learn how to train doc2vec from Spanish wikipedia!!
    * DONE be able to load up saved models
    * DONE how much text do we use to train a model?
      * DONE how much can we fit in memory for training?
        * we can fit Spanish wikipedia
      * how does training data size affect quality?
    * turn inferred document vectors into features for classification
    * CONCEPTUALLY DONE there's just one vector per sentence, so there's your
    feature vector.
  * DONE doc2vec features
    * EMPIRICAL QUESTION: does it even really make sense to use doc2vec by
    itself? is the meaning of the sentence as a whole what we want, for
    classifying a particular token
    usage?
  * DONE examine all of our Brown clusters that we found and make nice figures
    * SKIP lemmatized bible
    * SKIP surface bible
    * DONE lemmatized europarl
    * DONE surface europarl
    * DONE lemmatized wikipedia
    * DONE surface wikipedia
  * SKIP MAYBE understand why doc2vec models are so huge for 200 dimensions but
  not 400 dimensions.
  * DONE maybe rerun the word2vec experiements that we did with the regular
  feature file, since those seem to have used lemmas rather than surface forms.
  maybe surface forms help more?
  * DONE try doc2vec on a window around the focus word??
  * SKIP what kinds of words are we likely to do better on?
  * SKIP how does this look for words with more examples, versus fewer?
  * DONE finish up analysis and writeup
  * DONE make charts & graphs
  * DONE make sure we ran all windowbrown variants
  * DONE report results for all windowbrown variants
  * DONE edit text to reflect results for all windowbrown variants

## sequence
CANCELED!!

## combinations
  * CANCELED?? As a chapter anyway. Just do combinations as we go.
  * try combinations.

