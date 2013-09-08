#i'm sorry for my code, jaja i go to sleep i in this moment good bye :) 

from sys import argv
n2 = ['', '', 'twenty', 'thirty', 'forty',  'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
n1 = ['', 'one', 'two', 'three', 'four', 'five', 'six',     'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',     'thirteen',  'fourteen', 'fifteen',  'sixteen', 'seventeen',     'eighteen', 'nineteen']


def number_to_string(n):  # 342 = 3*100 | three hundred + 4 * 10 | forty + 2*1 | two = three hundred and forty-two
	hundred=False
	tmp = ""
	a=False
	if n == 1000:
		 return "onethousand"
	if n/100 > 0: 
		tmp=n1[n/100]+"hundred"
		hundred=True
		n=n%100
	
	if n/10>0:
		if hundred:
			tmp+="and"
		if n/10<2:
			tmp+=n1[n]
			n=0
		else:
			tmp+=n2[n/10]
			n=n%10
		a=True
	if n>0:
		if hundred and not a:
			tmp+="and"
		tmp+=n1[n]

	return tmp

size = 0
 
print number_to_string(int(argv[1]))


if argv[2]=="test":
	c=0

	while c<1000:
		size += len(number_to_string(c+1))
		print number_to_string(c+1)

		c+=1

	print size
 
