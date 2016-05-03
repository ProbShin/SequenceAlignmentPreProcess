#!/usr/bin/env python3

author__ = 'xincheng'
"""
This code is for chaoyang zhao
To pre process the DNA files into simplified files

Usage: ./cy_pre_process.py /path/to/a/DNA/file /path/to/simplified/DNA/file

For example,
```
DNA.txt
   1                  130
B_DN15774_                                  
B_DN16498_  GGAAATTTTA ATGATATTCT GCATAAATAA AATATATAAA TTGTGTTTGG TATTTAATTA 
B_DN11029_        GTCG TTGTCAAATC GATTTTTTCC CGTGTTGAAC TTACGGATTG 
  Consensus       ..... .......... .......... .......... .......... ........


example.txt
B_DN16498_:GGAAATTTTA ATGATATTCT GCATAAATAA AATATATAAA TTGTGTTTGG TATTTAATTA
B_DN11029_:      GTCG TTGTCAAATC GATTTTTTCC CGTGTTGAAC TTACGGATTG

$./cy_pre_process.py  example.txt  pped_example.txt
$./cy_get_dist_mtx.py pped_example.txt  matrix.txt

matrix.txt
seq1    seq2   
seq1    ??
```
"""

import sys

class Colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
	if(len(sys.argv)!=3) :
		print(Colors.RED+"Usage: {} <orgDNA_in> <simplifiedDNA_out>".format(sys.argv[0])+Colors.ENDC, file=sys.stderr);
		return;
	seqL,namL=[],[];
	debugcnt=0;
	with open(sys.argv[1], "r") as fin:
		with open(sys.argv[2],"w") as fout:
			for line in fin:
				debugcnt+=1;
				if(line==""):
					continue;
				if(line[0]==" "):
					print("fake:"+line[:10]);
					continue;
				lline=line.rstrip().split(" ",maxsplit=1);
				if(len(lline)!=2):
					continue;
				namL.append(lline[0]);
				seqL.append(lline[1]);
				#print("line :"+line[:20])
				#print("|name:"+lline[0])
				#print("|seq :"+lline[0][:10])
				print(lline[0]+":"+lline[1], file=fout);
'''
	print("", end=" ", file=f);
	for n in namL:
		print(n, end=" ", file=f);
	print("");
	for i in range(len(namL)):
		print(namL[i], end=" ", file=f);	
		for j in range(i+1):
				print(similar(seqL, i,j), end=" ", file=f);
		print("");
'''
def similar(L,i,j):
	if(i==j):
		return len(L[i])
	s1,s2 = L[i], L[j]
	s1 = s1 + ' '*(len(s2)-len(s1))
	s2 = s2 + ' '*(len(s1)-len(s2))
	return sum([1 if c1==c2 else 0 for c1,c2 in zip(s1,s2)])

if __name__ =="__main__":
	main();
