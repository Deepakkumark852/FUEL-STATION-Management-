
from flask import Flask,render_template,request,redirect, url_for
from grid import *
from kd_work  import *
from time import time
from brute import *
from recommend import *


app = Flask(__name__)

fuel_stations=[]
customers=[]

@app.route('/')
def mainpage():
    return render_template('home.html')

@app.route('/add_station',methods=['get','post'])
def add_station():
    if request.method=="POST":  
        

        x=request.form.get('X-Coordinate')
        y=request.form.get('Y-Coordinate')
        name=request.form.get('s_name')
        if x and y:
            
            x=int(x)
            y=int(y)
            if x>=0 and y>=0:
                fuel_stations.append([x,y,name,0])
                print(fuel_stations)
                return render_template('add_station.html')
            else:
                return render_template('home.html')
            
    return render_template('add_station.html')


@app.route('/add_customer',methods=['get','post'])
def add_customer():
    if request.method=="POST":  
        

        x=request.form.get('X-Coordinate_cust')
        y=request.form.get('Y-Coordinate_cust')
     
        if x and y:
            
            x=int(x)
            y=int(y)
            if x>=0 and y>=0:
                customers.append([x,y])
                print(customers)
                return render_template('add_customer.html')
            else:
                return render_template('home.html')
            
    return render_template('add_customer.html')

@app.route('/view',methods=['get','post'])
def view():
    plot_graph(customers,fuel_stations)
    return render_template('view.html')


@app.route('/kdimtree',methods=['POST','GET'])
def kdim():
    t1=time()
    kdans(customers,fuel_stations)
    t2=time()
    return render_template('kdim.html',time=t2-t1)

@app.route('/brute-force')
def brute():
    t3=time()
    brute_force(customers,fuel_stations)
    t4=time()
    return render_template('brute.html',time=t4-t3)

@app.route('/newstation')
def newstation():
    d=recommend(customers)
    p=[i for i in d]
    f=[d[i] for i in d]
    return render_template('newstation.html',p=p,f=f)

if __name__ == '__main__':
    app.run(debug=True)

