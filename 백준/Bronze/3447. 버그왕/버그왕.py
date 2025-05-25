import sys

line_list = sys.stdin.readlines()

for line in line_list:
    line = line.rstrip()

    while 'BUG' in line:
        line = line.replace('BUG', '')
    
    print(line)