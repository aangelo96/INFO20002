# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:36:41 2017
@author: Arnold,Ethan,Juday
"""
import csv
from csv import DictReader
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
    <link rel="stylesheet" href="fulldatafinal.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
    
</head>
<body>
<h1 align="center"> Full Student Alcohol Consumption Data Set <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/></h1>
<br>
<hr>
<br>
<p align=center> <span style="color:red;">*red</span> = Underage Alcoholics !!! </p>
<br>
<div class="row">
<div class="col-lg-1 col-md-1 col-sm-1 col-xs-0">
</div>
<div class="col-lg-10 col-md-10 col-sm-10 col-xs-12">
<div class="wrapper">
%s
</div>
</div>
<div class="col-lg-1 col-md-1 col-sm-1 col-xs-0">
</div>
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
    with open("EditedData3.csv", "rb") as csvfile :
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
                     elif (counter2==2) :
                         if (column=="A") :
                             table+= '<td>'+column+'<i class="em em-bust_in_silhouette"></i></td>'  
                             counter2 = counter2 + 1
                         else :
                             table+= '<td>'+column+'<i class="em em-busts_in_silhouette"></i></td>'  
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
          <option value="Age"> Age </option>
          <option value="Sex"> Sex </option>
          <option value="Parent Cohabitation Status"> Parent Cohabitation Status </option>
          <option value="Daily Alcohol Consumption"> Daily Alcohol Consumption </option>
          <option value="Weekly Alcohol Consumption"> Weekly Alcohol Consumption </option>
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
          <option value="Age"> Age </option>
          <option value="Sex"> Sex </option>
          <option value="Parent Cohabitation Status"> Parent Cohabitation Status </option>
          <option value="Daily Alcohol Consumption"> Daily Alcohol Consumption </option>
          <option value="Weekly Alcohol Consumption"> Weekly Alcohol Consumption </option>
          </select>
          <br><br>
      </div>  
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Select Column :</b></p>
          <select name="mycol">
          <option value="Sex"> Sex </option>
          <option value="Age"> Age </option>
          <option value="Parent Cohabitation Status"> Parent Cohabitation Status </option>
          <option value="Daily Alcohol Consumption"> Daily Alcohol Consumption </option>
          <option value="Weekly Alcohol Consumption"> Weekly Alcohol Consumption </option>
          </select>
          <br><br>
      </div> 
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Aggregation :</b></p>
          <select name="agg_calc">
          <option value="countof"> Count Of </option>
          <option value="sumof"> Sum Of </option>
          <option value="avgof"> Average Of </option>
          <option value="minof"> Minimum Of </option>
          <option value="maxof"> Maximum Of </option>
          </select>
          <br><br>
          <select name="agg">
          <option value="Number of Absences"> Number of Absences </option>
          <option value="Average Grade"> Average Grade </option>
          <option value="Number of Failed Subjects"> Number of Failed Subjects </option>
          <option value="Study time"> Study Time </option>
          <option value="Daily Alcohol Consumption"> Daily Alcohol Consumption </option>
          <option value="Weekly Alcohol Consumption"> Weekly Alcohol Consumption </option>
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
          <br><br>
      </div>
      </form>
      
  </div>
  </div>
  
</body>
</html>
'''
    return filter_page

def colorgen(num, bins):
  #Color list is from colorbrewer2.org
  colors = ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#084594']
  for i in range(len(bins)):
    if num <= bins[i]:
      return colors[i]

def createbins(minnum, maxnum):
  BINNUM = 7
  binrange = maxnum - minnum
  split = binrange/BINNUM
  bins = []
  for i in range(BINNUM):
    bins.append(maxnum)
    maxnum = maxnum-split
  bins.sort()
  return bins


@app.route('/handler', methods=['POST'])
def handler():

  #filter_sector = request.form['filter-sect']
  #filter_sign = request.form['filter-sign']
  #filter_value = request.form['filter-value']
  #row = request.form['myrow']
  #column = request.form['mycol']
  #aggregation_value = request.form['agg']

    #Row is Sex
    #Column is Age
    data = DictReader(open("EditedData3.csv"))
    data = list(data)


    #Row is Sex
    #Column is Age
    rows = []
    cols = []
    for i in range(0,100):
        if data[i]['Sex'] not in rows:
            rows.append(data[i]['Sex'])

        if data[i]['Age'] not in cols:
            cols.append(data[i]['Age'])
     
    rows.sort()
    cols.sort()

    data = [[1,19,31,4],[18,67,41,12]]

    #Find the smallest and largest numbers in the data set.
    maxnum = minnum = data[0][0]
    for row in data:
      if min(row) < minnum:
        minnum = min(row)
      if max(row) > maxnum:
        maxnum = max(row)
    bins = createbins(minnum, maxnum)

    html = '''
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
        <link rel="stylesheet" href="pivot.css">
    </head>
    <body>
        <div id="topbar">
            <div class = "indexdiv"><span><a href="/">Home</a></span></div>
            <div class = "indexdiv"><span><a href="/filter">Pivot Table Builder</a></span></div>
            <div class = "indexdiv"><span><a href="http://www.nyan.cat">Insights</a></span></div>
        </div>
        <div id="header">
            <h1 id = "title">Pivot Table<img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/></h1> 
            <h3>A comparison of absences with respect to Age and Sex</h3>
        </div>
    '''


    table = '<tr><td></td>'

    #First create the first row of the table with the column headers

    for col in cols:
        table += '<td>%s</td>' % col
    table += '<td>Total</td>'

    #Then find the total of each row and add it in
    for row in data:
        row.append(sum(row))

    table += '</tr>'

    #Then create the data inside the table.
    
    for row in range(len(rows)):
        table += '<tr><td>%s</td>' % rows[row]
        for col in range(len(cols)+1):
            lastcol = len(rows[0])
            if data[row][col] != data[row][-1]:
              table += ('<td bgcolor="'
              + colorgen(data[row][col], bins) +'"> %s</td>' % data[row][col] )
            else:
              table += '<td>%s</td>' % data[row][col]
        table += '</tr>'

    #Then, we add the total of each column and write it in.
    table += '<tr><td>Total</td>'

    for row in range(len(data[0])):
        total = 0
        for col in range(len(data)):
            total += data[col][row]
        table += '<td><strong>%s</strong></td>' % str(total)
    table +='</tr>'


    html += '''
        <div id = "tablediv">
            <table cellspacing = "0">
            ''' + table + '''
            </table>
        </div>
        </body>
    </html>
    '''

    return html


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)
