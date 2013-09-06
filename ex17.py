# jojoy copy files into other files :) 



from sys import argv

print "Copy "

init_file = open(argv[1])
data = init_file.read()
print "this file has a len ",len(data)

print "the file ",argv[2]," exist? ",exists(argv[2])

print "do you coninue? CRT + C to ext"

raw_input()


to_file = open(argv[2],'w')
to_file.write(data)

print "success! :D"
to_file.close()
init_file.close()
