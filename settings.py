import unicodedata

def ununi(l):
	# pdb.set_trace()
	l2=[]
	for x in range(0,len(l)):
		str1=unicodedata.normalize('NFKD', l[x]).encode('ascii','ignore')
		l2.append(str1)
	str1 = ''.join(map(str, l2))
	str1=str(str1)
	return str1

