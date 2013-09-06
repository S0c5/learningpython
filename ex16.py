# MMMM write files in python :) yeah




from sys import argv

script_name,file_name=argv

print "Welcome to Script"


file = open(file_name,'w')


line_one = raw_input('>')

file.write(line_one+"\n")

file.close()
