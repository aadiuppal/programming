#!/usr/bin/python

def rev_str(str):
	rev_s=""
	for i in str:
		rev_s = i + rev_s
	return rev_s


def rev_str_rec(str):
	if len(str)==1:
		return str
	else:
		return rev_str_rec(str[1:])+str[0] 


def rand_1_to_7(num_1_to_5):
	return (((float(num_1_to_5)-1)/4)*6)+1


def valid_email(str):
	str_present=['@','.']
	str_not=['#','!']
	str_sub=""
	for i in str_present:
		if i not in str:
			return 0
	for i in str_not:
		if i in str:
			return 0
	for i in range(0,len(str)):
		if i == '@':
			str_sub=str[i:]
	print str_sub
str="reverse this string"
print rev_str(str)
print "!!!!!!!!!"
print rev_str_rec(str)
print rand_1_to_7(1)
print rand_1_to_7(5)
print rand_1_to_7(3.5)
valid_email("asd@asd.c")

