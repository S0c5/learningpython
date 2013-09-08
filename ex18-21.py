# This is a file of execerices 18-19-20-21 of learning python.

from sys import argv
from os.path import exists


def print_file(f):
	print f.read()

def line(f):
	return f.readline()

def print_exist(file_name):
	flag = exists(file_name)
	print "Exist file name? ",flag
	return flag
def rewind(f):
	f.seek(0)



script_name, file_name = argv


print "the script name is ", script_name

file_tmp = open(file_name)
print_exist(file_name)

print "line : ",line(file_tmp),"-"*20
rewind(file_tmp)

print "\t*content file: \n","#"*50
print_file(file_tmp)
print "#"*50
