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

#format='.txt'
#out1_file_name = (inp_file_name)+format # adding extension '.txt' to the output file
#out2_file_name = (inp_file_name)+format # adding extension '.txt' to the output file

#write files
out1= open(out1_file_name,'w');


#read files
input=open(inp_file_name, 'r')

##for line in input: ##All lines in the input file

while True:
	line = input.readline() # read the line
        if not line: break
	line=line.split('\t'); # tokenize line into small fragments of strings and store it in an array.
        #print (line)
        length=len(line)
	for i in range (1,length): #writing into the first file
		if length > 1:
			#print length	
			out1.write('%s \t %s \n' % (line[0],line[i]))
                        #out1.write('\n')
		#else:
			#out1.write('%s \t %s' % (line[0],line[i]))
                else: #length==1:
			out1.write('%s \t %s' % (line[0],line[1]))

		
		
	#out1.write('\n') # newline 
		
	
out1.close()
input.close()


	
# end of this script
