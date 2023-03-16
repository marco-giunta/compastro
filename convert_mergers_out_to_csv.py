import re

f_in = open('./mergers.out', 'r')
f_out = open('./mergers_out.csv', 'w')

for line in f_in.readlines():
    line = line.lstrip().lstrip('#').lstrip()
    line = re.sub(r'\[[0-9]+\]', '', line)    
    line = re.sub(' +', ',', line)
    f_out.write(line)