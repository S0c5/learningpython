# this is the 15` Exercise and in this i learn to open files for read.

from sys import argv

script_name,filename = argv

print "this is the script name",script_name

file = open(filename)

print "the text the filename is", file.read()


print "good bye :) Happy hacking"

