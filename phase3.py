# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:36:41 2017

@author: Arnold,Ethan,Juday
"""
import csv
from flask import Flask,request
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def route():
    home_page = '''
<!doctype html>
<html>
<head>
    <title>Pivot Table - Filters</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="homepagefinal.css">
    
</head>
<body>
<h1 align="center"> Alcoholic Data Set and Pivot Table Builder <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/> </h1>
<br>
<hr>
<br>
<div class="container">
    <p> Choose Your Option : </p>
    <br>
    <div class="row">
        <form action="fulldata">
        <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12" id="left">
            <button type="submit" class="left_button"><b> Full Data Set </b></button>
        </div>
        </form>
        <br>
        <br>
        <br>
        <form action="filter">
        <div class="col-md-12 col-lg-12 col-sm-12 col xs-12" id="right">
            <button type="submit" class="right_button"><b> Pivot Table Generator </b></button>
        </div>
        </form>
    </div>
    <br>
    <hr>
    <h2 align=center> Our Team Member </h2>
    <br>
    <p> Arnold Angelo - 783859 </p>
    <br>
    <p> Ethan Cheng - </p>
    <br>
    <p> Juday Jorjilou - </p>
    <br>
    <hr>
</body>
</html>
'''
    return home_page

@app.route('/fulldata')
def fulldata():
    full_page = '''
<!doctype html>
<html>
<head>
    <title>Pivot Table - Filters</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="fullfinal.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    
</head>
<body>
<h1 align="center"> Full Student Alcohol Consumption Data Set <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/></h1>
<br>
<hr>
<br>
<p align=center> <span style="color:red;">*red</span> = Underage Alcoholics !!! </p>
<br>
<div class="wrapper">
%s
</div>

<br>
<div class="container">
    <div class="row">
        <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12" id="left">
            <form action="/">        
                <button type="submit" class="left_button"><b> Go Back To Main Page </b></button>
            </form>
            </div>
        <br>
        <br>
        <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12" id="right">
            <form action="filter">
                <button type="submit" class="right_button"><b> Go To Pivot Table Generator </b></button>
            </form>
        </div>
        <br><br>
    </div>
</div><script src="bubblesorteds2.js"></script>

</body>
</html>
'''
    with open("Edited Data2.csv", "rb") as csvfile :
        """Counter for Row"""
        counter = 0 
        """Counter for Column"""
        counter2 = 0 
        data = csv.reader(csvfile, delimiter=",")
        table = '<table border="10" align="center" id="myTable">'
        for row in data :
            if (counter>0) :
                table += '<tr class="item">'
            else :
                table += '<tr>'
            for column in row :
                 if (counter==0) :
                     asc = 0
                     desc = 1
                     table+= '<th>'+column+'<span class="glyphicon glyphicon-chevron-up" onClick="bubbleSort('+str(counter2)+','+str(asc)+')"></span><span class="glyphicon glyphicon-chevron-down" onClick="bubbleSort('+str(counter2)+','+str(desc)+')"></span></th>'
                     counter2 = counter2 + 1
                 else :
                     if ((counter2)==5 or (counter2)==6):
                         table+= '<td>'+column+'<img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/></td>'   
                         counter2 = counter2 + 1
                     elif (counter2==0) :
                         if (column=="F") :
                             table+= '<td style="background-color:pink;">'+column+'</td>'  
                             counter2 = counter2 + 1
                         else :
                             table+= '<td style="background-color:lightblue;">'+column+'</td>'  
                             counter2 = counter2 + 1
                     elif (counter2==1) :
                         if (int(column)<18) :
                             table+= '<td style="background-color:red;">'+column+'</td>'  
                             counter2 = counter2 + 1
                         else :
                             table+= '<td>'+column+'</td>'  
                             counter2 = counter2 + 1
                     else :
                         table+= '<td>'+column+'</td>'
                         counter2 = counter2 + 1
            table += '</tr>'
            counter=counter+1
            counter2=0;
        table += '</table>'
    

    return full_page % (table)

@app.route('/filter')
def filtering():
    filter_page = '''
<!doctype html>
<html>
<head>
    <title>Pivot Table - Filters</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="filtersfinal.css">
    
</head>
<body>
<h1 align="center"> Alcoholic Pivot Table Builder <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/></h1>
<br>
<hr>
<br>
<br>

  <div class="container"> 
  <div class="row">
      <form method="post" action="handler">
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Report Filter :</b></p>
          <select name="filter-sect">
          <option value="age"> Age </option>
          <option value="sex"> Sex </option>
          <option value="pstatus"> Parent Cohabitation Status </option>
          <option value="dalc"> Daily Alcohol Consumption </option>
          <option value="walc"> Weekly Alcohol Consumption </option>
          </select>
          <br>
          <br>
          <select name="filter-sign">
          <option value="any"> is anything </option>
          <option value="equal"> = </option>
          <option value="bigger"> > </option>
          <option value="smaller"> < </option>
          <option value="bigger-equal"> >= </option>
          <option value="smaller-equal"> >= </option>
          <option value="contains"> contains </option>
          <option value="not-contains"> does not contain </option>
          <option value="istrue"> is True </option>
          <option value="isfalse"> is False </option>
          </select>
          <br><br>
          <input type="text" name="filter-value" placeholder="Filter Value" value="">
          <br><br>
          
      </div>
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Select Row :</b></p>
          <select name="myrow">
          <option value="age"> Age </option>
          <option value="sex"> Sex </option>
          <option value="pstatus"> Parent Cohabitation Status </option>
          <option value="dalc"> Daily Alcohol Consumption </option>
          <option value="walc"> Weekly Alcohol Consumption </option>
          </select>
          <br><br>
      </div>  
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Select Column :</b></p>
          <select name="mycol">
          <option value="sex"> Sex </option>
          <option value="age"> Age </option>
          <option value="pstatus"> Parent Cohabitation Status </option>
          <option value="dalc"> Daily Alcohol Consumption </option>
          <option value="walc"> Weekly Alcohol Consumption </option>
          </select>
          <br><br>
      </div> 
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Aggregation :</b></p>
          <select name="agg">
          <option value="absenses"> Number of Absenses </option>
          <option value="g3"> Average Grade </option>
          <option value="failures"> Number of Failure Subjects </option>
          <option value="studytime"> Study Time </option>
          <option value="dalc"> Daily Alcohol Consumption </option>
          <option value="walc"> Weekly Alcohol Consumption </option>
          </select>
          <br><br>
      </div>
     
      <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12"> 
          <br>
          <br>
          <hr>
          <p align="center">
          <input align="center" id="subbutton" type="submit"/>
          </p> 
          <br>
      </div>
      </form>
      <form action="/"> 
      <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12" id="bottom">
          <button type="submit" class="homebutton"><b>Go Back To Main Page</b></button>
      </div>
      </form>
      
  </div>
  </div>
  

</body>
</html>
'''
    return filter_page

@app.route('/handler', methods=['POST'])
def handler():
  body = '''
<!doctype html>
<html>
<head>
    <title>Pivot Table - Result</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
    h1 {
            font-family:serif;
            font:bookman;
            color:white;
            }
    
    p {
    
            font-family:serif;
            font:bookman;
            color:white;
            font-size:50px}
    
    body {
            background-image: url("jadon-barnes-1446.jpg");
            opacity:0.9;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            height:100vh;
        }
    
    </style>
</head>
<body>
<h1 align="center"> Alcoholic Pivot Table Result </h1>
<p>Row : %s</p>
<br>
<p>Column : %s </p>

</body>
</html>
'''
  
  filter_sector = request.form['filter-sect']
  filter_sign = request.form['filter-sign']
  filter_value = request.form['filter-value']
  row = request.form['myrow']
  column = request.form['mycol']
  aggregation_value = request.form['agg']

  return body % (row,column)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)