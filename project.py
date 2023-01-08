from flask import Flask,render_template,request,redirect
import pymysql

x=Flask(__name__)
@x.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="itvchennai")
        cu=db.cursor()
        sql="select * from itv"
        cu.execute(sql)
        data=cu.fetchall()
        return render_template('page1.html',d=data)
    except Exception as e:
        print(e)

@x.route('/form')
def form():
    return render_template('page2.html')

@x.route('/store',methods=['POST'])
def store():
    si=request.form['ITV_ID']
    sn=request.form['NAME']
    ss=request.form['EMAIL']
    sc=request.form['PHONE']
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="itvchennai")
        cus=db.cursor()
        insertsql="insert into itv(ITV_ID,NAME,EMAIL,PHONE) values('{}','{}','{}','{}')".format(si,sn,ss,sc)
        cus.execute(insertsql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print(e)


@x.route('/edit/<rrid>')
def edit(rrid):
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="itvchennai")
        cu=db.cursor()
        sql="select * from itv where rid='{}'".format(rrid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('page3.html',d=data)
    except Exception as e:
        print(e)



@x.route('/update/<rrid>',methods=['POST'])
def update(rrid):
    si = request.form['ITV_ID']
    sn = request.form['NAME']
    ss = request.form['EMAIL']
    sc = request.form['PHONE']
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="itvchennai")
        cu=db.cursor()
        sql="update itv set ITV_ID='{}',NAME='{}',EMAIL='{}',PHONE='{}' where rid='{}'".format(si,sn,ss,sc,rrid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print(e)

@x.route('/delete/<rrid>')
def delete(rrid):
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="itvchennai")
        cu=db.cursor()
        sql="delete from itvchennai where rid={}".format(rrid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print(e)
    #if__name__=='__main__':
x.run(debug=True)





