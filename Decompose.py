#!/usr/bin/python

#Created by Parth Patel, DBI @ University of Delaware, Newark, Delaware 19717
#Date created: 4/23/2014
##This script is to read file line-by-line, tokenizing by tabs, and outputting certain fields to certain files.
##Usage : python Decompose.py <input file name> <output file name 1> <output file name 2> <first split index> <last split index> 
		  #i.e., Decompose.py instr_dept.txt instructor.txt department.txt 4 6


import re
import sys
import os


inp_file_name = str(sys.argv[1]) #user defined name for the input file
out1_file_name = str(sys.argv[2]) #user defined name for the first file
out2_file_name = str(sys.argv[3]) #user defined name for the second file
ini_range = int(str(sys.argv[4]))# begin index for splitting the file
end_range = int(str(sys.argv[5]))# last index for splitting the file

#format='.txt'
#out1_file_name = (inp_file_name)+format # adding extension '.txt' to the output file
#out2_file_name = (inp_file_name)+format # adding extension '.txt' to the output file

#write files
out1= open(out1_file_name,'w');
out2= open(out2_file_name,'w');

#read files
input=open(inp_file_name, 'r')

##for line in input: ##All lines in the input file

while True:
	line = input.readline() # read the line
        if not line: break
	line=line.split('\t'); # tokenize line into small fragments of strings and store it in an array.
        #print (line)
	for i in range (0,ini_range): #writing into the first file
                #print (ini_range)
                #print (line[i])
		out1.write('%s \t' % (line[i]))#writing each token in to file 1
		i=i+1
	out1.write('\n') # newline 
		
	for j in range (ini_range,end_range): #writing into the second file
		out2.write('%s \t' % (line[j]))#writing each token in to file 2
                j=j+1
	out2.write('\n')# new line

input.close()
out1.close()
out2.close()
	
# end of this script
