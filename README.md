# SequenceFilePreProcess
A simple to use PreProcess Python Program to static some useful information 

author__ = 'xincheng'

===================================
Introduction:
This code is for my friends
To calculate the overlap between DNAseqs
ALSO this code can output the simplified DNAseq files


===================================
Usage:
To get the overlap matrix
Usage: $./chaoy_dna.py /path/to/a/DNA/file

To get the simplified dna files
Usage: $./chaoy_dna.py /path/to/a/DNA/file

===================================
For example:
```
dna.txt
    1                            30
fake1_
seq_1_ aaatttccct atcggggccc aaa
seq_2_ aaatctttct atcggc-ccc
seq_3_                 cggccccc aaa
 Consensus ....... .....


dna_simplified.txt
seq_1_:aaatttccct atcggggccc aaa
seq_2_:aaatctttct atcggc-ccc
seq_3_:                cggccccc aaa


matrix.txt
	seq_1_    seq_2_    seq_3_
seq_1_ 25  
seq_2_ 15 21
seq_3_ 3 3 12
```
"""

===================================
Tests:
The code was tested under mac and linux
with Python3.5


===================================
Input Requirment:
raw DNA files should have a very special form:
* the lines begin with a SPACE is assumed as not DNA sequence
* the lines that only contains sequence id is assumed as not DNA sequence

simplified DNA files should have a very special form:
* each line should be <sequenceID>:<DNAsequence with space within body>


==================================
Output:
* the overlap matrix has specila form:
* the first line is all sequnce id. for seq1 to seqN
* the first line begin with a tab '\t'
* from sencond line to (N+1)th line, each line begin with sequence id and apped the overlap value.
* the the overlap values are stored in a lower trianguler matrix.



