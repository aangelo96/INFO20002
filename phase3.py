# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:36:41 2017

@author: Arnold,Ethan,Juday
"""

from flask import Flask,request
app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/filter')
def filtering():
    filter_page = '''
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
            color : white;}
    p {
        font-family:fantasy;
        font:Impact;
        font-size:20px;
        color:black;}
    img {
            width:100%;
            height:100%;
        }
    
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
            color : white;}
    p {
        font-family:fantasy;
        font:Impact;
        font-size:20px;
        color:black;}
    img {
            width:100%;
            height:100%;
        }
    
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
<br>
<hr>
<br>
<br>
</body>
</html>
'''
    
  filter_sector = request.form['filter-sect']
  filter_sign = request.form['filter-sign']
  filter_value = request.form['filter-value']
  row = request.form['myrow']
  column = request.form['mycol']
  aggregation_value = request.form['agg']
  
  return body 


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)