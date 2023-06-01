# Output Parser
<pre>
Sentence: Holmes sat and lit his pipe<br/>
                S<br/>
         _______|________<br/>
        S       |        S<br/>
   _____|___    |     ___|___<br/>
  NP        VP  |    VP      NP<br/>
  |         |   |    |    ___|___<br/>
  N         V  Conj  V  Det      N<br/>
  |         |   |    |   |       |<br/>
holmes     sat and  lit his     pipe<br/>

Noun Phrase Chunks<br/>
holmes<br/>
his pipe<br/>

Sentence: I had a little moist red paint in the palm of my hand<br/>
              S<br/>
  ____________|____________________<br/>
 |                                 VP<br/>
 |    _____________________________|____<br/>
 |   |                                  NP<br/>
 |   |                __________________|___________<br/>
 |   |               NP                             PP<br/>
 |   |    ___________|_____________      ___________|____<br/>
 |   |   |           AP            |    |                NP<br/>
 |   |   |     ______|____         |    |        ________|___<br/>
 |   |   |    |           AP       |    |       |            PP<br/>
 |   |   |    |       ____|___     |    |       |         ___|___<br/>
 NP  |   |    |      |        AP   |    |       NP       |       NP<br/>
 |   |   |    |      |        |    |    |    ___|___     |    ___|___<br/>
 N   V  Det  Adj    Adj      Adj   N    P  Det      N    P  Det      N<br/>
 |   |   |    |      |        |    |    |   |       |    |   |       |<br/>
 i  had  a  little moist     red paint  in the     palm  of  my     hand<br/>

Noun Phrase Chunks<br/>
i<br/>
a little moist red paint<br/>
the palm<br/>
my hand<br/>
<pre/>
