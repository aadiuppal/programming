def form_string(base_str,s):
	i=0
	j=0
	store=[]
	for _ in range(0,256):
		store.append(0)
	while j<len(base_str):
		store[ord(base_str[j])]+=1
		j+=1
		if store[ord(s[i])]>0:
			store[ord(s[i])]-=1
			i+=1
		if i==len(s):
			return True
	return False

s="asdafgh"
s1="aihqwer asd fi gi ii "
s2="asdsadadsdasqweasdasdasdsad"
print form_string(s1,s)
print form_string(s2,s)
