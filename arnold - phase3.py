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
    <style>
    h1 {
            font-family:serif;
            font:bookman;
            color : white;
            }
    h2 {
            font-family:serif;
            font:bookman;
            color : black;
            background-color: grey;
            border-radius: 8px;
            }
    
    p {
        font-family:fantasy;
        font:Impact;
        font-size:20px;
        color:white;
        text-align:center;}
    
    #left,#right {
        text-align:center;}
    
    .left_button {
        background-color:orange;
        
    }
    
    .right_button {
        background-color:blue;
        
    }
    
    .left_button:hover {
        opacity:1;
    }
    
    .right_button:hover {
        opacity:1;
    }
    
    body {
            background-image: url("jadon-barnes-1446.jpg");
            opacity:0.9;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            height:100%;
    }
    
    button { font-family:serif;
        font:bookman;
        font-weight:400;
        color:white; 
        border:0;
        border-radius:5px;
        padding: 6px 20px;
        opacity:0.9;
        align-items:center;
    }
    

    </style>
    
</head>
<body>
<h1 align="center"> Alcoholic Data Set and Pivot Table Builder </h1>
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
    <style>
    h1 {
            font-family:serif;
            font:bookman;
            color : black;
            }
    
    #left,#right {
        text-align:center;}
    
    .left_button {
        background-color:orange;
        
    }
    
    .right_button {
        background-color:blue;
        
    }
    
    .left_button:hover {
        opacity:1;
    }
    
    .right_button:hover {
        opacity:1;
    }
    
    
    body {
            background-color: grey;
            opacity:0.9;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            height:100vh;
    }
    
    button { font-family:serif;
        font:bookman;
        font-weight:400;
        color:white; 
        border:0;
        border-radius:5px;
        padding: 6px 20px;
        opacity:0.9;
        align-items:center;
    }
    
    .wrapper {
        text-align:center;
        color:white;
        }
    
    td,th {
        padding:10px;
        border-width:10px;
        background-color:white;
        color:black;
        }
    
    </style>
    
</head>
<body>
<h1 align="center"> Full Student Alcohol Consumption Data Set </h1>
<br>
<hr>
<br>
<p align="center"> *Click Headers For Sort Ascending <p>
<p align="center"> **One more click to Sort Descending <p>
<br>
<div class="wrapper">
%s
</div>
<script>
/*Cited From : https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sort_table_desc */
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("TR");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>

<br>
<div class="container">
    <div class="row">
        <form action="/">
            <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12" id="left">
                <button type="submit" class="left_button"><b> Go Back To Main Page </b></button>
            </div>
        </form>
        <br>
        <br>
        <br>
        <form action="filter">
            <div class="col-md-12 col-lg-12 col-sm-12 col xs-12" id="right">
                <button type="submit" class="right_button"><b> Go To Pivot Table Generator </b></button>
            </div>
        </form>
    </div>
</div>

</body>
</html>
'''
    with open("Edited Data2.csv", "rb") as csvfile :
        counter = 0
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
                     table+= '<th onclick="sortTable('+str(counter2)+')">'+column+'</th>'
                     counter2 = counter2 + 1
                 else :
                     table+= '<td>'+column+'</td>'
            table += '</tr>'
            counter=counter+1
        table += '</table>'
    

    return full_page % (table)

@app.route('/filter')
def filtering():
    filter_page = '''
<!doctype html>
<html>
<head>
    <title>Pivot Table - Filters</title>>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
    h1 {
            font-family:serif;
            font:bookman;
            color : white;}
    p {
        font-family:fantasy;
        font:Impact;
        font-size:20px;
        color:white;}
    
    input,select {
            border-radius:5px;
            padding: 6px 10px;
        }
    
    body {
            background-image: url("jadon-barnes-1446.jpg");
            opacity:0.9;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            height:100vh;
        }
    
    .container,col,row,body {
            min-width:500px;}
    
    #subbutton { font-family:serif;
        font:bookman;
        font-weight:400;
        background-color:grey;
        color:white; 
        border:0;
        border-radius:5px;
        padding: 6px 20px;
        opacity:0.8;
    }
    
    #subbutton:hover {
        opacity:1;    
    }
    </style>
    
</head>
<body>
<h1 align="center"> Alcoholic Pivot Table Builder </h1>
<br>
<hr>
<br>
<br>
<form method="post" action="handler">
  <div class="container"> 
  <div class="row">
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p>Report Filter :</p>
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
          <p>Select Row :</p>
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
          <p>Select Column :</p>
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
          <p>Aggregation :</p>
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
          <input align="center" id="subbutton" type="submit" />
          </p> 
        </div>  
  </div>
  </div>
  
</form>
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