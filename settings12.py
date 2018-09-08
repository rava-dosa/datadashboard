import dataset
import hashlib
import unicodedata
import pdb
from datetime import datetime
users = {'admin': {'password': 'secret', 'group':'admin'}}
gmail=""
ggroup=""
project_allowance=[]
user_current=""
i=0
# db1=dataset.connect("sqlite:///mydatabase.db")
# tablu=db1["user"].all()
# if tablu is not None:
#   for x in tablu:
#       global users
#       user1=ununi(x["user"])
#       password1=ununi(x["password"])
#       users={user1:{'password': 'password1', 'group':'user'}}
def ununi(l):
	# pdb.set_trace()
	l2=[]
	for x in range(0,len(l)):
		str1=unicodedata.normalize('NFKD', l[x]).encode('ascii','ignore')
		l2.append(str1)
	str1 = ''.join(map(str, l2))
	str1=str(str1)
	return str1
def init():
	# pdb.set_trace()
	db1=dataset.connect("sqlite:///mydatabase.db")
	tablu=db1["user"].all()
	if tablu is not None:
		for x in tablu:
			global users
			user1=ununi(x["user"])
			password1=ununi(x["password"])
			users.update({user1:{'password': 'password1', 'group':'user'}})
		return users
def hash(string):
	hash_object = hashlib.md5(string.encode())
	str1=hash_object.hexdigest()
	return str1
def no(string,table):

	obj=table.find(id1=string)
	global i
	for item in obj:
		i=i+1
		print item
	# print "i hun main"+ str(i)
	j=i
	i=0
	return j
def no_addpermission(string1,string2,table):

	obj=table.find(uid=string1,pid=string2)
	global i
	for item in obj:
		i=i+1
		print item
	# print "i hun main"+ str(i)
	j=i
	i=0
	return j
def no_adduser(string,table):

	obj=table.find(user=string)
	global i
	for item in obj:
		i=i+1
		print item
	# print "i hun main"+ str(i)
	j=i
	i=0
	return j
def no1(string1,string2,table):
	# pdb.set_trace()
	obj=table.find(id1=string1,url=string2)
	global i
	for item in obj:
		i=i+1
		print item
		print "i hun main"+ str(i)
	# print "i hun main return "+ str(i)
	j=i
	i=0
	return j
def no2(string1,string2,table):
	# pdb.set_trace()
	obj=table.find(id1=string1,keyword=string2)
	global i
	for item in obj:
		i=i+1
		print item
		print "i hun main"+ str(i)
	print "i hun main return "+ str(i)
	j=i
	i=0
	return j

def no3(string1,string2,string3,table):
	# pdb.set_trace()
	obj=table.find(id1=string1,id2=string2,keyword=string3)
	global i
	for item in obj:
		i=i+1
		print item
		print "i hun main"+ str(i)
	print "i hun main return "+ str(i)
	j=i
	i=0
	return j
def add_project(db,string):
	table = db['project']
	hash_object = hashlib.md5(string.encode())
	str1=hash_object.hexdigest()
	if(no(str1,table)<1):
		table.insert(dict(id1=str1, name=string))
	else:
		return '<p>Already Exist, provide something else</p>'

def get_project_list(db):
	table = db['project']
	listofproject=db["project"].all()
	li=[]
	for project in db['project']:
		li.append(project["name"])
		print project["name"]
		# pdb.set_trace()
	return li

def add_user(db,string,password,project_id):
	table = db['user']
	# str1=hash(string)
	str11=hash(password)
	if(no_adduser(string,table)<1):
		table.insert(dict(id1=project_id, user=string, password=str11))
		return string
	else:
		return '<p>Already Exist, provide something else</p>'

def add_permission(db,user_id,project_id):
	table = db['permission']
	print user_id + " "+project_id
	if(no_addpermission(user_id,project_id,table)<1):
		table.insert(dict(uid=user_id, pid=project_id))
	return '<p>Done</p>'

def add_repo(db,pid,string,url):
	table = db['repo']
	hash_object = hashlib.md5(string.encode())
	str1=hash_object.hexdigest()
	url=url.replace(" ","")
	url=url.replace("'","")
	url=url.replace("[","")
	url=url.replace("]","")
	print url
	print string
	str11=hash(url)
	# pdb.set_trace()
	if(no1(pid,url,table)<1):
		print "pid "+pid + " urlid "+str11+" repo "+string+" url "+url
		table.insert(dict(id1=pid,urlid=str11,repo=string ,url=url))
		return '<p>Done</p>'
	else:
		return '<p>Already Exist, provide something else</p>'
def get_repo(db,pid):
	table = db['repo']
	obj=table.find(id1=pid)
	if(no(pid,table)!=0):
		l=[]
		for item in obj:
			l.append(item["url"])
	return l
def get_user(db,pid):
	print "get_user : "+pid
	print "in get_user"
	table = db["permission"]
	obj=table.find(pid=pid)
	l=[]
	print no(pid,table)
	if(no(pid,table)>=0):
		for item in obj:
			l.append(item["uid"])
	return l
def get_project(db,uid):
	table = db["permission"]
	obj=table.find(uid=uid)
	l=[]
	if(no(uid,table)>=0):
		for item in obj:
			l.append(item["pid"])
	return l
def save_keywords(db,rid,url,l,pid):
	table = db["keywords"]
	# obj=table.find(uid=uid)
	url=url.replace(" ","")
	url=url.replace("'","")
	for x in range(0,len(l)):
		strx=l[x]
		str123=strx.replace(" ","")
		str123=str123.replace("'","")
		str123=str123.replace("[","")
		str123=str123.replace("]","")
		# pdb.set_trace()
		if(no3(rid,pid,str123,table)<1):
			print "in keywords automatic wala"
			print "repo_id "+rid+" url "+url + " keyword "+str123
			table.insert(dict(id1=rid,id2=pid ,url=url, keyword=str123))
		else:
			pass
	return 'done'
def save_keywords1(db,rid,url,l,pid):
	table = db["keywords"]
	# obj=table.find(uid=uid)
	for x in range(0,len(l)):
		if(no2(rid,l,table)<1):
			print "repo_id "+rid+" url "+url + " keyword "+l
			table.insert(dict(id1=rid,id2=pid ,url=url, keyword=l))
		else:
			pass
	return 'done'

def compa(item,date,flag):
	date=datetime.strptime(date, '%Y-%m-%d')
	if flag==0:
		for x in range(0,len(item)):
			item1=item[x]
			date1=item1["date"]
			date1=ununi(date1)
			# pdb.set_trace()
			date1=date1.replace("\n","")
			date1=date1.replace(" ","")
			try:
				date12=datetime.strptime(date1, '%Y-%m-%d')
				if(date12>=date):
					return item[x:]
			except:
				return item[x:]

	else:
		for x in range(0,len(item)):
			item1=item[x]
			date1=item1["date"]
			date1=ununi(date1)
			date1=date1.replace("\n","")
			date1=date1.replace(" ","")
			try:
				date12=datetime.strptime(date1, '%Y-%m-%d')
				if(date12>date):
					return item[0:x-1]
				elif date12==date and x==len(item)-1:
					return item[0:x+1]
				elif date12<date and x==len(item)-1:
					return item[0:x+1]
			except:
				return item[0:x]
			# elif date




def csvmakedate(db,project_name,date1,date2):
	pdb.set_trace()
	return_list=[]
	l=[]
	f=open("2111.csv", "w")
	str1="repo_name"+","+"keyword"+","+"url"+","+"heading of issue"+"\n"
	f.write(str1)
	table=db["repo"]
	table1=db["keywords"]
	pid=hash(project_name)
	obj=table.find(id1=pid)
	for item in obj:
		url=item["url"]
		# REPO_NAME=item["repo"]
		url=ununi(url)
		# REPO_OWNER=url.split("/")
		# len1=len(REPO_OWNER)
		REPO_NAME=item["repo"]
		REPO_NAME=ununi(REPO_NAME)
		# REPO_OWNER=str(REPO_OWNER[len1-2])
		obj1=table1.find(id1=hash(REPO_NAME),id2=pid)
		for item1 in obj1:
			l.append(REPO_NAME)
			string1=item1["keyword"]
			string1=ununi(string1)
			string2=pid+REPO_NAME+string1
			table2=db[string2]
			datestr1=str(date1)
			item3=table2.find(order_by=['id1'])
			l123=[]
			for x in item3:
				l123.append(x)
				# print x
			item334=compa(l123,datestr1,0)
			# pdb.set_trace()
			if item334 is None:
				n=0
			else:
				n=len(item334)
			if n==0:
				pass
			else:
				datestr2=str(date2)
				# print "item34 "+item34
				item4=compa(item334,datestr2,1)
				# print "item4 "+item4
				# item5=item4.intersection(item34)
				# print "item5 " + item5
				if item4 is not None:               
					for item6 in item4:
						str13=REPO_NAME+","+string1+","+item6["url"]+","+item6["title"].strip("\n")
						str13=ununi(str13)
						return_list.append(str13)
						str14=str13+"\n"
						f.write(str14)
				else:
					pass

		if REPO_NAME not in l:
			string2=pid+REPO_NAME+""
			table2=db[string2]
			datestr1=str(date1)
			item3=table2.find(order_by=['id1'])
			l123=[]
			for x in item3:
				l123.append(x)
				# print x
			item334=compa(l123,datestr1,0)
			# pdb.set_trace()
			if item334 is None:
				n=0
			else:
				n=len(item334)
			if n==0:
				pass
			else:
				datestr2=str(date2)
				# print "item34 "+item34
				item4=compa(item334,datestr2,1)
				# print "item4 "+item4
				# item5=item4.intersection(item34)
				# print "item5 " + item5
				if item4 is not None:               
					for item6 in item4:
						str13=REPO_NAME+","+"None"+","+item6["url"]+","+item6["title"].strip("\n")
						str13=ununi(str13)
						return_list.append(str13)
						str14=str13+"\n"
						f.write(str14)
				else:
					pass
	f.close()           
	return return_list
	# gemail.sending()

# pdb.set_trace()
if __name__ == "__main__":
	db = dataset.connect('sqlite:///mydatabase.db')
	print add_project("ps4")
	print add_project("ps5")
