#!/usr/bin/env python3

author__ = 'xincheng'
"""
This code is for chaoyang zhao
To calculate the overlap between DNAseqs
ALSO this code can output the simplified DNAseq files

To get the overlap matrix
Usage: $./chaoy_dna.py /path/to/a/DNA/file

To get the simplified dna files
Usage: $./chaoy_dna.py /path/to/a/DNA/file

For example,
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

import sys
import os

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
	if(len(sys.argv)==2) :
		filename, file_extension = os.path.splitext(sys.argv[1]);
		get_overlap_mtx(sys.argv[1], filename+"_overlap_mtx.txt");
	elif(len(sys.argv)==3 and "-s" in sys.argv):
		sys.argv.remove("-s");
		filename, file_extension = os.path.splitext(sys.argv[1]);
		simplify_dna(sys.argv[1], filename+"_simplified.txt");
	else:
		print(Colors.RED+"Usage: {} <raw_DNA_in_file>".format(sys.argv[0])+Colors.ENDC, file=sys.stderr);
		print("to get overlap matrix with filename= "+Colors.GRAY+"<raw_DNA>_overlap_mtx.txt"+Colors.ENDC+" or", file=sys.stderr)
		print(Colors.RED+"Usage: {} <raw_DNA_in_file> -s".format(sys.argv[0])+Colors.ENDC+"\nto get simplified DNA files with filename= "+Colors.GRAY+"<raw_DNA>_simplified.txt"+Colors.ENDC, file=sys.stderr);
def get_overlap_mtx(fin_name, fout_name):
	seqL,namL=[],[];
	debugcnt=0
	split =" "
	with open(fin_name, "r") as f:
		if ":" in f.readline():
			split=":";
		f.seek(0);
		for line in f:
			debugcnt+=1;
			if(line=="" or line[0]==" "):
				continue;
			lline=line.rstrip().split(split,1);
			if(len(lline)!=2):
				continue;
			namL.append(lline[0]);
			seqL.append(lline[1]);
	with open(fout_name, "w") as f:  #f=sys.stdout;
		print("\t{}".format(" ".join(namL)),  file=f);
		for i in range(len(namL)):
			print("{} {}".format(namL[i], " ".join([str(n) for n in [overlap(seqL,i,j) for j in range(i+1)]])), file=f);

def overlap(L,i,j):
	if(i==j):
		return len(L[i].lstrip())
	s1,s2 = L[i], L[j]
	s1 = s1 + ' '*(len(s2)-len(s1))
	s2 = s2 + ' '*(len(s1)-len(s2))
	return sum([1 if c1==c2 and c1!=" " else 0 for c1,c2 in zip(s1,s2)])

def simplify_dna(fin_name, fout_name):
	seqL,namL=[],[];
	debugcnt=0;
	with open(fin_name, "r") as fin:
		line=fin.readline();
		if ":" in line: #=fin.readline():
			print("@"+line+"@");
			print(Color.RED+"WARNING! {} seems is not a raw file. The simplified output may not correct!".format(fin_name)+Color.ENDC, file=sys.stderr)
		fin.seek(0)
		with open(fout_name,"w") as fout:
			for line in fin:
				debugcnt+=1;
				if(line=="" or line[0]==" "):
					continue;
				lline=line.rstrip().split(" ",maxsplit=1);
				if(len(lline)!=2):
					continue;
				print(lline[0]+":"+lline[1][1:], file=fout);
	
if __name__ =="__main__":
	main();
