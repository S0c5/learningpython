# raw_input() and arguments of console (argv)


from sys import argv

name, script = argv

print "hello ", name
print "script ", script

a=raw_input("your name is?")

print "%r",a
