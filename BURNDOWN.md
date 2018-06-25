# things left undone

## general

## monolingual

## multilingual

## integration
  * for chipa-from-moses: run any other annotators on input maybe?
  * super important: get a clear answer out of Mike and Sandra whether they'll
  consider it convincing if we can integrate into one PBMT and one RBMT system

  * hack up squoia again if necessary
    * how changed is it? is it very different from before?
  * also need a good evaluation plan for es-qu
  * write up how we hacked up squoia


### integration: possibly obsolete ideas here

  * CANCELED! build tiniest possible cdec system for es-gn (switched to moses??)
  * SKIP Learn to use CMU's morphogen or whatever it's called -- or we could
  just punt and target lemmatized gn.
  * DONE built tiny pb-smt system for es-gn, now pretty good at spinning these
  things up.

  * HARD How hard is it to do phrase-based for cdec? We need to figure out how
  to load PB-SMT tables. Also how to build them . Can cdec tools even generate
  them?

  * SKIP Port cdec-as-python-module stuff to py3k.
  * STARTED Add chipa as phrase table feature 

## outro
  * Look, it's some experiments!
  * Some of them worked!
  * Probably better to crowdsource and get some respectable amount of data
  rather than just using the Bible, unless your language is actually extinct.
  * Hey-o, now I'm a doctor!


# fairly done things

## general done things
  * DONE set up new laptop and latex build environment there
  * SKIP be able to draw curves of word training data size versus accuracy
  * DONE pick a spelling for Guarani. It's probably the one with no accent, right?
    * DONE Yes, use the no-accent version; accented is how you spell it in Spanish.

## baseline done things
  * DONE maybe rerun the experiments from the baseline chapter so we know that the results are comparable; we're using explicit lists of top words now.
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
  * DONE make a list of all of Sandra's notes for monolingual
  * DONE figure out how to sensibly draw dependency trees such that it doesn't
  ruin the whole build process
  * DONE come up with a good bold/italic/whatever scheme to highlight strongest
  result in a table
  * DONE make sure we handled all of Sandra's notes for monolingual

## multilingual
  * DONE make a version of the trainingdata\_for function that loads training
  data for a particular lemma from disk, rather than from memory.
  * DONE data preparation script is going to need to keep track of annotated
  version of *both* input corpora.
    * DONE this probably means that we should refactor how we keep input corpora in
    memory.
    * SKIP the approach where we have these global variables sitting around on
    modules is kind of gross. we have objects for a reason; encapsulate
    everything we need to know about a given corpus in one object. Pass the
    corpora objects around as arguments like you're a marginally competent
    software engineer. 
    * can we actually skip this? Maybe we can. We train classifiers for es-en,
    for example, and then we just need to take the "annotated" version of a
    Spanish sentence and turn it into a classification problem, just extract
    features from it. That's not so hard, right?
  * DONE pick lemmatizer/stemmer to use (can just use FreeLing!)
  * OK NOTED: This is roughly our "classifier stacking" approach, or basically
  "L2", except that in the semeval paper we trained on the real answers and
  tested on classifier answers, which was goofy.
  * DONE Run the classifiers in "annotator" mode -- we blow through an input
  file and we classify with an existing classifier, then just save the
  classification as an annotation.
    * DONE notably, we want to write down the answer *on the particular token*
    that we are going to try to classify later -- it is not a property of the
    sentence as a whole. The sentence as a whole is not a classification
    problem; it could have multiple different tokens that need to get
    classified.
  * BASICALLY DONE make scripts for preparing data for Europarl for the European
  languages we think we're going to do. Should be basically like the en-es data
  preparation script.
  * DONE labeling: es-en, es-fr, es-it, es-de, es-nl
  * SKIP TreeTagger! how did we do nl for semeval? TreeTagger? 
  * DONE pick languages we want to use
    * freeling supports: cs, de, en, es, fr, it, nb, pt, ru, sl... so plenty
    * probably actually just do es, fr, it, de, nl like semeval ?
      * yes: we can use frog (Maarten made it!) to lemmatize Dutch
        * DONE got frog via LaMachine: https://proycon.github.io/LaMachine/
      * DONE?? write a script to lemmatize Dutch with frog
  * DONE make features out of those annotations
  * DONE extra feature: window of stack annotations
  * DONE run stacking-trained-on-europarl experiments: es-gn
  * DONE es-en bible stacking
    * seems to help actually, by a few tenths of a percent
  * get more bibles for other languages!!
    * DONE here you go: https://github.com/christos-c/bible-corpus-tools
    * DONE now extract them into the formats that terere expects
    * DONE annotate es-gn with those classifiers
    * DONE annotate es-qu with those classifiers
  * TRUE so that would suggest... train classifiers on the bible! we have quite
  a few bibles available.  add more bibles if that seems to help?
  * DONE run stacking-trained-on-bible experiments: es-gn
  * DONE run stacking-trained-on-bible experiments: es-qu
  * DONE run stacking-trained-on-europarl experiments: es-gn
  * DONE run stacking-trained-on-europarl experiments: es-qu
  * DONE run stacking-trained-on-europarl experiments with just en stacking
  * DONE measure which/how many words we care about for the es bible have enough
  support in europarl for us to get a classifier.
  * DONE consider running experiment with both kinds of stacking -- does that
  help? -- you know, it really doesn't help.
  * SKIP maybe also be like "here are the sense distinctions present in Europarl"
  * SKIP what's the accuracy of the trained classifiers on europarl? would that be good to report?
  * DONE what if it turns out that the domain mismatch is too bad?
  * SKIP maybe the sense distinctions in europarl aren't similar enough to the bible.
  * NOTED note that there's a bunch of XML markup in the europarl corpus
  sentence pair output, so you can't really count those lines when you're
  talking about the size of the corpus. It looks like you get 2.5 million
  sentences for the es-de and es-it (etc) corpora, but it's really just about
  the same size as the es-en one.
  * DONE report measurements about domain mismatches
  * DONE ... is the writing here mostly done? take a good edit pass and send it in!
  * DONE talk about data sets and data preparation more coherently
  * DONE explain results and write good outro
  * MAYBESKIP do we need to run bible stacking + all sparse features, together?
  that's not hard to do, and it might be nice to see for comparison

## sequence
CANCELED!!

## combinations
  * CANCELED?? As a chapter anyway. Just do combinations as we go.
  * try combinations.

## integration done things
  * PROBABLY SKIP consider: integrate chipa into Mike's current RBMT systems.
    * understand Mike's current RBMT systems well enough to hack them up
  * DONE get buy-in from Sandra (Mike is probably OK with this?)
  * SKIP download and set up phrasal
    * see how hard it is to use their discriminative feature situation
      * can you pass the context for the whole sentence?
  * SKIP consider: integrate chipa into Phrasal
  * MAYBESKIP: train surface and lemmatized LMs.
  * DONE figure out what the simplest thing we can do is that demonstrates an
  integration story: SQUOIA and Moses!!
  * DONE be clear about what we're doing here -- surface es to gn lemmas
  * DONE language modeling for gn, maybe?
    * DONE pull all gn text from gn-wikipedia
    * DONE lemmatize it
    * DONE train LM
    * MAYBESKIP? pull all gn text from guarani-nee
  * DONE come up with a plan for evaluation here
    * pick a test set
      * picked a bad test set; need to do better here
    * DONE be able to compute BLEU with Moses tools
      * SKIP although we should use mteval-v14.pl instead apparently
      * DONE actually for reals, we should use sacrebleu
  * DONE sample a dev set and run MERT for moses
  * make a fiforpc server that talks to the ChipaFF client.
    * DONE read sentence over the fifo
    * DONE lemmatize it
    * HANDLED there's the issue of where we should represent MWEs.
      * it's kind of weird to have the training data for Moses have the joined
      collocations, isn't it?
      * but we get those out of preprocessing from freeling
      * ideally you'd just want to have one preprocessing step at the front of
      the whole pipeline rather than having your WSD system futz with running a
      tagger and worrying about tokenization; that's really not great design
    * DONE get classifier for that lemma and return classification
  * DONE train a simple PBMT system for Guarani with Moses
    * DONE default system
    * DONE make default system translate from es surface to gn lemmas
    * DONE system where phrases have 1 es word to many gn words
  * DONE finish building moses feature function that calls out to chipa
