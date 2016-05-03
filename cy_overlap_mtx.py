#!/usr/bin/env python3

author__ = 'xincheng'
"""
This code is for chaoyang zhao
To calculate the similarity of DNAs

Usage: ./cy_get_dist_mtx.py /path/to/a/DNA/file /path/to/result/mtx/file

For example,
```
example.txt
seq1: aaatttccct atcggggccc aaa
seq2: aaatctttct atcggc-ccc
seq3:                 cggccccc aaa

$./cy_pre_process.py  example.txt  pped_example.txt
$./cy_get_dist_mtx.py pped_example.txt  matrix.txt

matrix.txt
seq1    seq2    seq3
seq1    23-bp  
seq2    19-bp	19-bp
seq3    11-bp   7-bp   13-bp
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
		print(Colors.RED+"Usage: {} <preprocessedDNA_in> <similarMtx_out>".format(sys.argv[0])+Colors.ENDC, file=sys.stderr);
		return;
	seqL,namL=[],[];
	debugcnt=0;
	with open(sys.argv[1], "r") as f:
		for line in f:
			debugcnt+=1;
			lline=line.split(":");
			if(len(lline)!=2):
					print(Colors.RED+"Error on line:{} with content:\n{}"+Colors.ENDC.format(debugcnt, line), file=sys.stderr);
					return;
			namL.append(lline[0]);
			seqL.append(lline[1]);
			print(len(lline[1]))	
			print(lline[1])	
			print('*'*len(lline[1]))	
	f=sys.stdout;
	print("", end=" ", file=f);
	for n in namL:
		print(n, end=" ", file=f);
	print("");
	for i in range(len(namL)):
		print(namL[i], end=" ", file=f);	
		for j in range(i+1):
				print(similar(seqL, i,j), end=" ", file=f);
		print("");

def similar(L,i,j):
	if(i==j):
		return len(L[i])
	s1,s2 = L[i], L[j]
	s1 = s1 + ' '*(len(s2)-len(s1))
	s2 = s2 + ' '*(len(s1)-len(s2))
	return sum([1 if c1==c2 else 0 for c1,c2 in zip(s1,s2)])

if __name__ =="__main__":
	main();
