from __future__ import division
import dataset
import settings
import pdb

def insert(name,lis):
	db=dataset.connect('sqlite:///mydatabase.db')
	Table=db[name]
	for l in lis:
		print(l[0])
		Table.insert(dict(instant=l[0],dteday=l[1],season=int(l[2]),yr=int(l[3]),mnth=int(l[4]),holiday=int(l[5]),weekday=int(l[6]),workingday=int(l[7]),weathersit=int(l[8]),temp=l[9],atemp=l[10],hum=l[11],windspeed=l[12],casual=int(l[13]),registered=int(l[14]),cnt=int(l[15])))

def pag(name,date1,date2):
	l=[]
	db=dataset.connect('sqlite:///mydatabase.db')
	Table=db[name]
	statement = "SELECT * FROM %s WHERE dteday between %s and %s "%(name,"'"+date1+"'","'"+date2+"'")
	x=db.query(statement)
	# for row in db.query(statement):
	# 	s=[row['instant'],row['dteday'],row['season'],row['yr'],row['mnth'],row['holiday'],row['weekday'],row['workingday'],row['weathersit'],row['temp'],row['atemp'],row['hum'],row['windspeed'],row['casual'],row['registered'],row['cnt']]
	# 	l.append(s)
	# print
	return x

def avg(name,date1,date2):
	l=[]
	avg=[0,0,0,0,0,0,0]
	db=dataset.connect('sqlite:///mydatabase.db')
	Table=db[name]
	statement = "SELECT * FROM %s WHERE dteday between %s and %s "%(name,"'"+date1+"'","'"+date2+"'")
	x=db.query(statement)
	for row in db.query(statement):
		s=[row['temp'],row['atemp'],row['hum'],row['windspeed'],row['casual'],row['registered'],row['cnt']]
		l.append(s)
	i=len(l)
	for x in l:
		print x[0]
		print x[1]
		print x[6]
		# pdb.set_trace()	
		for y in range(0,7):
			avg[y]=avg[y]+float(x[y])
	for x in range(0,7):
		avg[x]=avg[x]/i

	return avg