from flask import Flask
from flask import render_template, url_for
from flask import request
import settings
import csv
import model
import pdb
app = Flask(__name__)
name=""
itemy=[]
@app.route('/')
def hello_world():
	l=model.get_table()
	return render_template('hello.html',name=l)
	
@app.route('/uploader',methods=['POST'])
def uploader():
	if request.method == 'POST':
		lis=[]
		f = request.files['file']
		ls=f.filename
		ls=str(ls).split(".")
		global name
		name=ls[0]
		print name
		ls=ls[1]
		if(ls=="csv"):
			lines = f.readlines()
			x=0
			for row in lines:
				if x==0:
					x=x+1
					continue
				else:
					row=row.rstrip()
					row=str(row).split(",")
					lis.append(row)
					if(x%100==0):
						# sending data to be inserted in batch
						model.insert(name,lis)
						lis=[]
					elif len(lines)-1==x:
						model.insert(name,lis)
					x=x+1
			return "csv file uploaded successfully"
		else:
			return "not csv"

@app.route('/browse/<name>',methods=['POST'])
def browser(name=None):
	print name
	date1=request.form['date1']
	date2=request.form['date2']
	date1=settings.ununi(date1)
	date2=settings.ununi(date2)
	itemx=model.pag(name,date1,date2)
	global itemy
	itemy=list(itemx)
	if(len(itemy)>=10):
		return render_template("table.html",item=itemy[0:10],flagn=1,flagp=0, name='0')
		print "hi"
	else:
		return render_template("table.html",item=itemy)

@app.route('/browse/pagi/<name>',methods=['GET'])
def pagi(name=None):
	if(len(itemy)-(10*int(name)+10)>=10):
		return render_template("table.html",item=itemy[10*int(name):10*int(name)+10],flagn=1,flagp=1, name=name)
		print "hi"
	else:
		return render_template("table.html",item=itemy[10*int(name):],flagn=0,flagp=1, name=name)

@app.route('/average/<name>',methods=['POST'])
def browser1(name=None):
	print name
	date1=request.form['date1']
	date2=request.form['date2']
	date1=settings.ununi(date1)
	date2=settings.ununi(date2)
	itemx=model.avg(name,date1,date2)
	return render_template("t1.html",x=itemx)

@app.route('/xyz/<name>',methods=['GET'])
def browser2(name=None):
	return render_template("uploader.html",name=name)

app.run(debug=True,threaded=True)
