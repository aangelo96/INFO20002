# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:36:41 2017
@author: Arnold,Ethan,Juday
"""
import csv
from csv import DictReader
from flask import Flask,request
from collections import defaultdict

app = Flask(__name__, static_folder='.', static_url_path='')

#About Us Page
@app.route('/about')
def route():
    home_page = '''
<!doctype html>
<html>
<head>
    <title>About Us</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="final_about.css">
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
    
</head>
<body>
<div id="topbar">
    <div class="indexdiv">
        <a href="/"><span id="top">Home</span></a>
        <a href="/fulldata"><span id="top">Data</span></a>
        <a href="/filter"><span id="top">Pivot Table Builder</span></a>
        <a href="/insights"><span id="top">Insights</span></a>
        <a href="/about"><span id="top">About Us</span></a>
        <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/>
    </div>
</div>
<h1 align="center"> Alcoholic Data Set and Pivot Table Builder</h1>
<br>
<div id="content">
                <div class="about" id = "left">
                    <div>
                        <h2>About Our Dataset</h2>
                        <p>
                            Our data set was obtained from 
                            <a href="https://www.kaggle.com/uciml/student-alcohol-consumption">Kaggle</a>
                            , and was generated through a survey
                            of students' math courses in secondary school. It contains
                            alot of information relating to their family situation, school performance,
                            as well as quality of life indicators.
                        </p>
                    </div>
                    <div>
                        <h2>About Us</h2>
                        <p>Arnold Angelo - 783859</p>
                        <p>Ethan Cheng - 762061</p>
                        <p>Jorjilou Reyes - 836917</p>
                    </div>
                </div>            
                <div class="about">
                    <h2>Data Used</h2>
                    <p>
                        For the purpose of discussion, we have decided to omit some 
                        categories, and only include the categories which we felt were
                        more relevant to what we are trying to discuss

                        </br></br>
                        <span style="text-align:left">Data contained:</span> </br>
                    </p>

                    <ul>
                        <li>Sex</li>
                        <li>Age</li>
                        <li>Parent Cohabitation Status</li>
                        <li>Study Time</li>
                        <li>Number of Failed Subjects</li>
                        <li>Weekday Alcohol Consumption</li>
                        <li>Weekend Alcohol Consumption</li>
                        <li>Number of Absences</li>
                        <li>Average Grade</li>
                        <li>Quality of Family Relationships</li>
                </div>    

</div>
</body>
</html>
'''
    return home_page

#Home Page
@app.route('/')
def homeroute():
    home_page = '''
<!doctype html>
<html>
<head>
    <title>Home</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="final_home2.css">
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
</head>
</body>
    <div id="bodydiv">
        <div id="titlediv">
            <h3>Student Alcohol Consumption </h3>
            <img src="https://stevenchasestudios.files.wordpress.com/2012/06/kopandawm.png" 
            title = "Picture from Steven Chase Studios"/>
        </div>
        <div id="linkbar">
            <div class="link"><a href="/fulldata">Data</a></div>
            <div class="link"><a href="/filter">Pivot Table Builder</a></div>
            <div class="link"><a href="/insights">Insights</a></div>
            <div class="link"><a href="/about">About Us</a></div>
            
        </div>
    </div>
</body>
</html>
'''
    return home_page

#Data Page
@app.route('/fulldata')
def fulldata():
    full_page = '''
<!doctype html>
<html>
<head>
    <link rel="icon" href="http://example.com/favicon.png">
    <title>Full Data</title>
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="final_full.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
    
</head>
<body>
<div id="topbar">
    <div class="indexdiv">
        <a href="/"><span id="top">Home</span></a>
        <a href="/fulldata"><span id="top">Data</span></a>
        <a href="/filter"><span id="top">Pivot Table Builder</span></a>
        <a href="/insights"><span id="top">Insights</span></a>
        <a href="/about"><span id="top">About Us</span></a>
        <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/>
    </div>
</div>
</div>
<h1 align="center"> Full Student Alcohol Consumption Data Set</h1>
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
<script src="bubblesorteds2.js"></script>
</body>
</html>
''' 
    #Opening CSV and put the data into table
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
    csvfile.close()

    return full_page % (table)

@app.route('/filter')
def filtering():
    filter_page = '''
<!doctype html>
<html>
<head>
    <title>Pivot Builder</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
    <link rel="stylesheet" href="final_filter.css">
   
</head>
<body>
<div id="topbar">
    <div class="indexdiv">
        <a href="/"><span id="top">Home</span></a>
        <a href="/fulldata"><span id="top">Data</span></a>
        <a href="/filter"><span id="top">Pivot Table Builder</span></a>
        <a href="/insights"><span id="top">Insights</span></a>
        <a href="/about"><span id="top">About Us</span></a>
        <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/>
    </div>
</div>
<h1 align="center"> Alcoholic Pivot Table Builder</h1>
<br>
<hr>
<br>
<br>
  <div class="container"> 
  <div class="row">
      <form method="post" action="handler">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
          <script>
          $(document).ready(function () {
            $("#filter-sect").change(function () {
                var val = $(this).val();
                if (val == "Sex" || val == "Age" || val == "Parent Cohabitation Status") {
                    $("#filter-sign").html("<option value='is anything'> is anything </option><option value='='> = </option> <option value='!='> != </option> <option value='contains'> contains </option> <option value='does not contain'> not contains </option>");
                } else {
                    $("#filter-sign").html("<option value='is anything'> is anything </option><option value='='> = </option> <option value='!='> != </option> <option value='contains'> contains </option> <option value='does not contain'> not contains </option> <option value='>'> > </option> <option value='<'> < </option> <option value='>='> >= </option> <option value='<='> <= </option>");
                }
                
            });
          });
          </script>
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Report Filter :</b></p>
          
          <select name="filter-sect" id="filter-sect">
          <option value="Age"> Age </option>
          <option value="Sex"> Sex </option>
          <option value="Parent Cohabitation Status"> Parent Cohabitation Status </option>
          <option value="Weekday Alcohol Consumption"> Weekday Alcohol Consumption </option>
          <option value="Weekend Alcohol Consumption"> Weekend Alcohol Consumption </option>
          <option value="Quality of Family Relationships">Quality of Family Relationships</option>
          </select>
          <br>
          <br>
          
          <select name="filter-sign" id="filter-sign">
          <option value="is anything"> is anything </option>
          <option value="="> = </option>
          <option value="!="> != </option>
          <option value="contains"> contains </option>
          <option value="does not contain"> does not contain </option>
          <!-- <option value="bigger"> > </option>
          <option value="<"> < </option>
          <option value=">="> >= </option>
          <option value="<="> <= </option> !-->
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
          <option value="Weekday Alcohol Consumption"> Weekday Alcohol Consumption </option>
          <option value="Weekend Alcohol Consumption"> Weekend Alcohol Consumption </option>
          <option value="Quality of Family Relationships">Quality of Family Relationships</option>
          </select>
          <br><br>
      </div>  
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Select Column :</b></p>
          <select name="mycol">
          <option value="Sex"> Sex </option>
          <option value="Age"> Age </option>
          <option value="Parent Cohabitation Status"> Parent Cohabitation Status </option>
          <option value="Weekday Alcohol Consumption"> Weekday Alcohol Consumption </option>
          <option value="Weekend Alcohol Consumption"> Weekend Alcohol Consumption </option>
          <option value="Quality of Family Relationships">Quality of Family Relationships</option>
          </select>
          <br><br>
      </div> 
      <div class="col-md-4 col-lg-3 col-sm-6 col-xs-6"> 
          <p><b>Aggregation :</b></p>
          <select name="agg_calc">
          <option value="Count Of"> Count Of </option>
          <option value="Sum Of"> Sum Of </option>
          <option value="Average Of"> Average Of </option>
          <option value="Minimum Of"> Minimum Of </option>
          <option value="Maximum Of"> Maximum Of </option>
          </select>
          <br><br>
          <select name="agg">
          <option value="Number of Absences"> Number of Absences </option>
          <option value="Average Grade"> Average Grade </option>
          <option value="Number of Failed Subjects"> Number of Failed Subjects </option>
          <option value="Study time"> Study Time </option>
          <option value="Weekday Alcohol Consumption"> Weekday Alcohol Consumption </option>
          <option value="Weekend Alcohol Consumption"> Weekend Alcohol Consumption </option>
          <option value="Quality of Family Relationships">Quality of Family Relationships</option>
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
      </form>
      
  </div>
  </div>
  
</body>
</html>
'''
    return filter_page

#FUNCTIONS

def colorgen(num, bins):
  #Color list is from colorbrewer2.org
  colors = ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#084594']
  #Decide which color group the number is in based on its bin.
  for i in range(len(bins)):
    if num <= bins[i]:
      return colors[i]

def createbins(minnum, maxnum):

  #Calculate the range of data, then create a list of numbers
  #that represent the threshold for each bin.  
  BINNUM = 7
  binrange = maxnum - minnum
  split = binrange/BINNUM
  bins = []
  for i in range(BINNUM):
    bins.append(maxnum)
    maxnum = maxnum-split
  bins.sort()
  return bins

def convert_rows_2_cols(data_2d, header):
	"""
	converts rows of data into columns
	"""
	col_dict = defaultdict(list)
	for row in data_2d:
		i=0
		for elem in row:
			col_dict[header[i]].append(elem)
			i += 1
	return col_dict
        
def get_col_types(col_dict, header):
	"""
	record the types of each column in the dictionary provided in another dict
	and return this dictionary of types
	"""
	types_dict=defaultdict(str)
	
	#go through each element in each column of csv file and get their type
	for key,val in col_dict.items():
		types_lst=[]
		for elem in val:
			#records the type of each element in the row
			types_lst.append(return_type(elem))
		#from the list of types, get the main type of the list of vals
		col_type = get_main_type(types_lst)
		#add type to dict
		types_dict[key]=col_type
		
	return types_dict
	
		
def return_type(elem):
	"""
	tests if elem in string is an integer, float or string
	"""
	if ((' ' in elem or elem.isalpha()) and (not elem.isdigit())):
		return 'str'
	elif (elem.isdigit()):
		return 'int'
	else:
		return 'float'
		
def get_mode(lst_elem):
	"""
	get the most frequent element in the list of elements
	"""
	
    #tally the amount an element is present in the list
	elem_tally=defaultdict(int)
	for elem in lst_elem:
		elem_tally[elem] += 1
	
	#get the highest count of tallies
	max_count=max(elem_tally.values())

	#put into list the most frequent values in vals
	mode_vals=[]
	for (key, val) in elem_tally.items():
		if val == max_count:
			mode_vals.append(key)
	
	return mode_vals
	
	
def get_main_type(lst_types):
	"""
	from a list of types, get the main type
	"""
	modes=get_mode(lst_types)
	if ('str' not in modes) and 'int' in modes:
		if 'float' in modes:
			return 'float'
		else:
			return 'int'
	else:
		return 'str'

def get_sorted_uniques(lst_elem):
    """
    returns a sorted list of unique values of all the values in lst_elem
    """
    uniques = []
    for elem in lst_elem:
        if not(elem in uniques):
            uniques.append(elem)
    uniques.sort()
    
    return uniques
    
def make_data_2d(rowColAgFil_lst, row_col_attr, operatn_str, ag_type, fltr_lst):
	"""
	makes a 2d data by summarising selected row and column by aggregating it 
	by the aggregate value/column and applying operatn_str to it
	"""
	#rowColAgFil_lst = [row lst, col list, aggreg8 list, filter list]
	#fltr_lst = [filter_sector, filter_sign, filter_val]
	data_2d = []
	#for each unique element in row, make a row according to the column
	for r in row_col_attr[0]:
		table_row = []
		for c in row_col_attr[1]:
			#concatenate the string in row and column
			rowcol = r+c
			#look for corresponding row and col elements = rc, and aggregate
			aggreg8ed = aggreg8_rc(rowcol, rowColAgFil_lst, operatn_str, 
				ag_type, fltr_lst)
			table_row.append(aggreg8ed)
		#add row of aggregated values in data_2d
		data_2d.append(table_row)
		
	return data_2d
	
def aggreg8_rc(concaten8ed_rc, rocolagfil_lst, operation, ag_type, fltr_lst):
	"""
	go through selected list to be aggregated and apply operation on 
	elements with their corresponding row and colmn as concaten8d_rc
	"""
	to_be_aggreg8ed = []
	#convert string list to equivalent number
	num_ag_lst = str2num(rocolagfil_lst[2], ag_type)
	
	#filter the elements so that filters are applied and it will only apply 
	#operations if corresponding row and column elements = concaten8ed_rc
	for i in range(len(rocolagfil_lst[0])):
		if(rocolagfil_lst[0][i] + rocolagfil_lst[1][i] == concaten8ed_rc):
			if(apply_filter(rocolagfil_lst[3][i], fltr_lst) == 'GO'):
				to_be_aggreg8ed.append(num_ag_lst[i])
	ans = apply_operation(operation, to_be_aggreg8ed)
	
	return ans
	
def apply_filter(element, fltr_list):
	"""
	apply selected filter by user, returns GO if this element should be included
	in the list to be aggregated
	"""
	
	lst_type = return_type(element)
	if ((fltr_list[1]=='is anything') or (fltr_list[1]=='is True' and element)
		or (fltr_list[1]=='is False' and (not element))):
		return 'GO'
	elif (fltr_list[1]=='contains' or fltr_list[1]=='='):
		if element == fltr_list[2]:
			return 'GO'
	elif ((fltr_list[1]=='does not contain') and (element!=fltr_list[2])):
		return 'GO'
	elif (fltr_list[1] in '>=<='):
		assert(lst_type != 'str')
		if((fltr_list[1]=='<' and element < fltr_list[2]) or
			(fltr_list[1]=='>' and element > fltr_list[2]) or
			(fltr_list[1]=='<=' and element <= fltr_list[2]) or
			(fltr_list[1]=='>=' and element >= fltr_list[2])):
			return 'GO'

def str2num(str_list, elem_type_str):
	"""
	convert a list of string into a list of elem_type_str and return a list
	of converted values
	"""
	conv_list = []
	if (elem_type_str == 'int'):
		conv_list = [int(e) for e in str_list]
	elif (elem_type_str == 'float'):
		conv_list = [float(e) for e in str_list]
	
	return conv_list

	
def apply_operation(operation, lst_vals):
	"""
	applies operation to the lst_vals and returns the answer
	"""
	
	#if list is empty, return '-'
	if (len(lst_vals)==0):
		return '-'
		
	if (operation == "Sum Of"):
		ans = sum(lst_vals)
	elif(operation == "Count Of"):
		ans = len(lst_vals)
	elif(operation == "Average Of"):
		ans = get_average_of(lst_vals)
	elif(operation == "Minimum Of"):
		ans = min(lst_vals)
	elif(operation == "Maximum Of"):
		ans = max(lst_vals)
	return ans
	
def get_average_of(lst_vals):
	"""
	returns the average of the values inside lst_vals
	"""
	return round(float(sum(lst_vals))/len(lst_vals),2)


#MAIN
def main(pRow, pCol, pAg_val, pAg_operatn, fltr_sec, fltr_sign, fltr_val):
	"""
	user-selected attributes from the columns of data are organized and 
	aggregated into a 2d data
	"""

	print pRow, pCol, pAg_val, pAg_operatn, fltr_sec, fltr_sign, fltr_val
	
	fltr_lst = [fltr_sec, fltr_sign, fltr_val]
    #opening csv file
	csv_file = open('EditedData3.csv')
	data = csv.reader(csv_file)
	
	#list of column titles and data converted into list of rows
	header = next(data)
	csv_2d = list(data)
	
	#obtains the csv file's columns from csv's rows
	csv_cols = defaultdict(list)
	csv_cols = convert_rows_2_cols(csv_2d, header)
	csv_file.close()

	#list of type of data values for each column
	coltype_dict = defaultdict(str)

	coltype_dict = get_col_types(csv_cols, header)

	#get columns needed
	rowColAgFil_lst = [csv_cols[pRow], csv_cols[pCol], csv_cols[pAg_val], 
	csv_cols[fltr_sec]]
	
	#get uniques
	uniq_row = get_sorted_uniques(csv_cols[pRow])
	uniq_col = get_sorted_uniques(csv_cols[pCol])
	uniq_lst = [uniq_row, uniq_col]
	
	data_2d = []
	data_2d = make_data_2d(rowColAgFil_lst, uniq_lst, pAg_operatn, 
		coltype_dict[pAg_val], fltr_lst)
	
	return data_2d


#Function that generates the extra information in the pivot table page
def keygen(irow,icol):

    #Use a dictionary with the info in it for the program to choose from, depending
    #On the user's input

    extrainfo = {
    'Age': ['Numeric from 15-22',],
    'Sex': ['F - Female', 'M - Male',],
    'Parent Cohabitation Status': ['T - Living Together', 'A - Living Apart'],
    'Weekday Alcohol Consumption': ['From 1-5', '1 - Very Low', '5- Very High'],
    'Weekend Alcohol Consumption': ['From 1-5', '1 - Very Low', '5- Very High'],
    'Quality of Family Relationships': ['From 1-5', '1 - Very Low', '5- Very High']
    }

    keyhtml = '''<div id = "keydiv">
        <h3>Columns: <span style="color:black">%s</span></h3>
        ''' % icol

    for i in extrainfo[icol]:
        keyhtml += '<p>%s</p>' % i

    keyhtml += '<h3>Rows: <span style="color:black">%s</span></h3>' % irow
    for i in extrainfo[irow]:
        keyhtml += '<p>%s</p>' % i      
    keyhtml += '</div>'
    return keyhtml



@app.route('/handler', methods=['POST'])
def handler():

    fil_sect = request.form['filter-sect']
    fil_sign = request.form['filter-sign']
    fil_val = request.form['filter-value']
    irow = request.form['myrow']
    icol = request.form['mycol']
    agg_val = request.form['agg']
    agg_op = request.form['agg_calc']

    #With this function we get an array that contains the processed data
    data_array = main(irow,icol,agg_val,agg_op,fil_sect,fil_sign,fil_val)
    print data_array
    data = DictReader(open("EditedData3.csv"))
    data = list(data)

    rows = []
    cols = []
    
    #Array of distinct data for row and col
    for i in range(0,395):
        if data[i][irow] not in rows:
            rows.append(data[i][irow])

        if data[i][icol] not in cols:
            cols.append(data[i][icol])
     
    rows.sort()
    cols.sort()
    
    #Find the smallest and largest numbers in the data set.
    
    
    html = '''
    <html>
    <head>
        <title>Pivot Table</title>
        <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
        <link rel="stylesheet" href="final_pivot.css">
    </head>
    <body>
        <div id="topbar">
        <div class="indexdiv">
        <a href="/"><span id="top">Home</span></a>
        <a href="/fulldata"><span id="top">Data</span></a>
        <a href="/filter"><span id="top">Pivot Table Builder</span></a>
        <a href="/insights"><span id="top">Insights</span></a>
        <a href="/about"><span id="top">About Us</span></a>
        <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/>
        </div>
        </div>
        <div id="header">
            <h1 id = "title">Pivot Table</h1> 
            
        </div>
        <div id="about">
            <h3>A comparison of <span id="details">%s</span> and <span id="details">%s</span></h3>
            <h3>With respect to the <span id="details">%s</span> : <span id="details">%s</span></h3>
            <h3>When %s %s %s</span></h3>
        <hr>
        <br>
    <div id="contentdiv">  
    <div id="tablediv">        
    <table id="myTable" align = "right"><tr><td></td>
    '''
    #Add Column categories in first
    for col in cols :
        html += '<td>'+col+'</row>'
    #Add Total column
    html += '<td>Total</td>'
    html += '</tr>'
    
    maxnum = 0;
    minnum = 0;
    #Add Totals to each row
    for row in data_array :
        sumval = 0
        sumcount = 0
        for col in row :
            if (col!='-') :
                sumval += col
                sumcount += 1
                if (col>maxnum) :
                    maxnum=col
                if (col<minnum) :
                    minnum=col
        if (sumcount!=0) :
            row.append(sumval)
        else :
            row.append('-')
        
    #use createbins to find bin ranges
    bins = createbins(minnum, maxnum)
    
    #counter for Row Tag
    counter = 0
    
    for row in data_array :
        html += '<tr>'
        counter= counter+1
        if (row[-1]=='-') :
            continue
        #insert every Row Tag
        html += '<td>'+rows[counter-1]+'</td>'
        #insert every column data
        for i in range(len(row)) :
            if (i!=len(row)-1 and row[i] != '-') :
                html += '<td bgcolor="'+ colorgen(row[i], bins) +'">'+str(row[i])+'</td>'
            else :
                html += '<td>'+str(row[i])+'</td>'
        html += '</tr>'
    
    #Then, we add the total of each column and write it in.
    html += '<tr><td>Total</td>'

    for row in range(len(data_array[0])):
        total = 0
        for col in range(len(data_array)):
            if (data_array[col][row]!='-') :
                total += data_array[col][row]
        html += '<td><strong>%s</strong></td>' % str(total)

    #And then finish off the table
    html += '''
    </tr>
    </table>
    </div>
    '''
    #Add in the key on the right
    html += keygen(irow, icol)
    html += '</div>'
    html += '</body></html>'
    
    
    # print(data_array)
    return html % (irow,icol,agg_op, agg_val,fil_sect,fil_sign,fil_val)

#Function that takes the desired categories, and returns a dictionary of values
#to put into the chart    
def insightgen(category, xaxis, yaxis):
    read_csv = csv.reader(open("EditedData3.csv"))
    data = list(read_csv)
    
    #First go through the first row and identify
    #the indexes of the chosen categories
    for i in data[0]:
        if i == category:
            catindex = data[0].index(i)
        elif i == xaxis:
            xindex = data[0].index(i)
        elif i == yaxis:
            yindex = data[0].index(i)

    #Create a dictionary for each category, each with their own
    #lists of data
    cat_dict = {}
    for row in data[1:]:
        if row[catindex] not in cat_dict:
            cat_dict[row[catindex]] = {}

    #Then go through each row in the data and the yaxis value
    #to the unique xaxis values
    #xaxis_dict = {}
    for row in data[1:]:
        if row[xindex] not in cat_dict[row[catindex]]:
        	cat_dict[row[catindex]][row[xindex]] = [int(row[yindex])]
        else:
        	cat_dict[row[catindex]][row[xindex]].append(int(row[yindex]))

    #After all the data has been written in, replace the list of yaxis values with their 
    #averages (for purpose of the chart)
    for category in cat_dict.keys():
        for xval in cat_dict[category].keys():
            #cat_dict[category][xval] = get_average_of(cat_dict[category][xval])
            cat_dict[category][xval] = get_average_of(cat_dict[category][xval])



    return cat_dict

#Takes as input the key-value pairs to be put into the chart,
#and returns a sorted list for use in the chart.
def sorted_list(pairs):
    pairs.sort()

    final_list = []
    for i in pairs:
        final_list.append(i[1])
    return final_list


def negative(array):
    for i in range (0,len(array)):
        array[i] = -array[i];
    return(array);

@app.route('/test')
def test():


    html = str(insightgen("Sex", "Weekend Alcohol Consumption", "Average Grade"))

    return html

@app.route('/insights')
def insights():

    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Insights</title>
        <script src="/jquery.js"></script>
        <script src="http://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <script src="https://code.highcharts.com/modules/exporting.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="/insight.css">
        <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
        '''

    data_dict0 = insightgen("Sex", "Age", "Weekday Alcohol Consumption")
    html += '''
            <script>
            $(function(){
                var myChart = Highcharts.chart('chart0', {
                    chart: {
                        type: 'area'
                    },
                    title: {
                        text: 'Changes on Weekday Alcohol Consumption'
                    },
                    xAxis: {
                        text: 'Student Age',
                        categories: [15,16,17,18,19,20,21,22]
                    },
                    yAxis: {
                        title: {
                            text: 'Weekday Alcohol Consumption'
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s,
                    }, {
                        name: 'Males',
                        color: '#ADD8E6',
                        data: %s,
                    }]
                });
            });
    ''' % (str(sorted_list(data_dict0['F'].items())), str(sorted_list(data_dict0['M'].items())))
    
    data_dict0 = insightgen("Sex", "Age", "Weekend Alcohol Consumption")
    html += '''
            $(function(){
                var myChart = Highcharts.chart('chart10', {
                    chart: {
                        type: 'area'
                    },
                    title: {
                        text: 'Changes on Weekend Alcohol Consumption'
                    },
                    xAxis: {
                        text: 'Student Age',
                        categories: [15,16,17,18,19,20,21,22]
                    },
                    yAxis: {
                        title: {
                            text: 'Weekend Alcohol Consumption'
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s,
                    }, {
                        name: 'Males',
                        color: '#ADD8E6',
                        data: %s,
                    }]
                });
            });
    ''' % (str(sorted_list(data_dict0['F'].items())), str(sorted_list(data_dict0['M'].items())))
    
        #Create chart one and two, for the effects of weekend/weekday alcohol consumption on grades
    data_dict1 = insightgen("Sex", "Weekend Alcohol Consumption", "Average Grade")
    data_dict2 = insightgen("Sex", "Weekday Alcohol Consumption", "Average Grade")
    html += '''
            $(function(){
                var myChart = Highcharts.chart('chart1', {
                    chart: {
                        type: 'line'
                    },
                    title: {
                        text: 'Weekend'
                    },
                    xAxis: {
                        text: 'Level of Weekend Alcohol Consumption',
                        categories: [1,2,3,4,5]
                    },
                    yAxis: {
                        title: {
                            text: 'Average Grade'
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s
                    }, {
                        name: 'Males',
                        color: '#1D83B2',
                        data: %s
                    }]
                });
            }); ''' % (str(sorted_list(data_dict1['F'].items())), str(sorted_list(data_dict1['M'].items())))


    html += '''
            $(function(){
                var myChart = Highcharts.chart('chart2', {
                    chart: {
                        type: 'line'
                    },
                    title: {
                        text: 'Weekday'
                    },
                    xAxis: {
                        text: 'Level of Weekday Alcohol Consumption',
                        categories: [1,2,3,4,5]
                    },
                    yAxis: {
                        title: {
                            text: 'Average Grade'
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s
                    }, {
                        name: 'Males',
                        color: '#1D83B2',
                        data: %s
                    }]
                });
            });
    ''' % (str(sorted_list(data_dict2['F'].items())), str(sorted_list(data_dict2['M'].items())))
    
	#Create chart three, to show the effect of weekend alcohol consumption on no. of failed subjects
    data_dict1 = insightgen("Sex", "Weekend Alcohol Consumption", "Number of Failed Subjects")
    html += '''
            $(function(){
                var myChart = Highcharts.chart('chart3', {
                    chart: {
                        type: 'line'
                    },
                    title: {
                        text: 'Weekend'
                    },
                    xAxis: {
                        text: 'Level of Weekend Alcohol Consumption',
                        categories: [1,2,3,4,5]
                    },
                    yAxis: {
                        title: {
                            text: 'Failed Subjects'
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s
                    }, {
                        name: 'Males',
                        color: '#1D83B2',
                        data: %s
                    }]
                });
            });
    ''' % (str(sorted_list(data_dict1['F'].items())), str(sorted_list(data_dict1['M'].items())))
    
    data_dict3 = insightgen("Sex", "Quality of Family Relationships", "Weekend Alcohol Consumption")
    data_dict4 = insightgen("Parent Cohabitation Status", "Sex", "Average Grade")
    html += '''
			$(function(){
				var myChart = Highcharts.chart('chart4', {
					chart: {
						type: 'bar'
					},
					
					title: {
						text: 'Quality of Family Relationship vs Weekend Alcohol Consumption'
					},
						
					xAxis: {
						title: {
							text: 'Quality of Family Relationships'
						},
						categories: [1, 2, 3, 4, 5]
					},
						
					yAxis: {
						min: 0,
						title: {
							text: 'Level of Weekend Alcohol Consumption'
						}
					},
					
					legend: {
						reversed: true
					},
					
					plotOptions: {
						series: {
							stacking: 'normal'
						}
					},
					
					series: [{
						name: 'Males',
                     color: '#1D83B2',
						data: %s
					}, {
						name: 'Females',
                     color: '#FFC0CB',
						data: %s
					}]
				});
			});
	'''%(str(sorted_list(data_dict3['M'].items())), str(sorted_list(data_dict3['F'].items())))
    
    html += '''
			$(function(){
				var myChart = Highcharts.chart('chart5', {
					chart: {
						type: 'column'
					},
					title: {
						text: 'Parent Cohabitation Status vs Average Grade'
					},
					xAxis: {
						title: {
							text: 'Sex'
						},
						categories: ['M', 'F'],
						crosshair: true
					},
					yAxis: {
						min: 0,
						title: {
							text: 'Average Grade'
						}
					},
					tooltip: {
						headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
						pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
							'<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
						footerFormat: '</table>',
						shared: true,
						useHTML: true
					},
					plotOptions: {
						column: {
							pointPadding: 0.2,
							borderWidth: 0
						}
					},
					series: [{
						name: 'Apart',
                    color: '#808080',
						data: %s
				
					}, {
						name: 'Together',
                    color: 'black',
						data: %s
				
					}]
				});
			});
	''' % (str(sorted_list(data_dict4['A'].items())), str(sorted_list(data_dict4['T'].items())))
    
    data_dict1 = insightgen("Sex", "Weekend Alcohol Consumption", "Study time")
    html += '''
            $(function(){
                var myChart = Highcharts.chart('chart8', {
                    chart: {
                        type: 'bar'
                    },
                    title: {
                        text: 'Weekend Consumption vs Study Time by Sex'
                    },
                    xAxis: [{
                        title: {
                        text: 'Weekend Alcohol Consumption'
                        },
                        categories: [1,2,3,4,5],
                        reversed: false,
                        labels: {
                                step: 1
                        }
                    },{ // mirror axis on right side
                        title: {
                        text: 'Weekend Alcohol Consumption'
                        },
                        opposite: true,
                        reversed: false,
                        categories: [1,2,3,4,5],
                        linkedTo: 0,
                        labels: {
                                step: 1
                                }
                    }],
                    yAxis: {
                        title: {
                            text: 'Average Study time'
                        },
                        labels: { 
                                formatter: function () {
                                    return Math.abs(this.value);
                                }
                        }
                    },
                    plotOptions: {
                        series: {
                            stacking: 'normal'
                        }
                    },
                    tooltip: {
                        formatter: function () {
                            return '<b>' + this.series.name + ', Consumption ' + this.point.category + '</b><br/>' +
                            'Avg Study Time: ' + Highcharts.numberFormat(Math.abs(this.point.y), 2);
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s
                    }, {
                        name: 'Males',
                        color: '#1D83B2',
                        data: %s
                    }]
                });
            });
    ''' % (str(negative(sorted_list(data_dict1['F'].items()))), str((sorted_list(data_dict1['M'].items()))))
    
    data_dict1 = insightgen("Sex", "Weekday Alcohol Consumption", "Study time")
    html += '''
            $(function(){
                var myChart = Highcharts.chart('chart9', {
                    chart: {
                        type: 'bar'
                    },
                    title: {
                        text: 'Weekdays Consumption vs Study Time by Sex'
                    },
                    xAxis: [{
                        title: {
                        text: 'Weekday Alcohol Consumption'
                        },
                        categories: [1,2,3,4,5],
                        reversed: false,
                        labels: {
                                step: 1
                        }
                    },{ // mirror axis on right side
                        title: {
                        text: 'Weekday Alcohol Consumption'
                        },
                        opposite: true,
                        reversed: false,
                        categories: [1,2,3,4,5],
                        linkedTo: 0,
                        labels: {
                                step: 1
                                }
                    }],
                    yAxis: {
                        title: {
                            text: 'Average Study time'
                        },
                        labels: { 
                                formatter: function () {
                                    return Math.abs(this.value);
                                }
                        }
                    },
                    plotOptions: {
                        series: {
                            stacking: 'normal'
                        }
                    },
                    tooltip: {
                        formatter: function () {
                            return '<b>' + this.series.name + ', Consumption ' + this.point.category + '</b><br/>' +
                            'Avg Study Time: ' + Highcharts.numberFormat(Math.abs(this.point.y), 2);
                        }
                    },
                    series: [{
                        name: 'Females',
                        color: '#FFC0CB',
                        data: %s
                    }, {
                        name: 'Males',
                        color: '#1D83B2',
                        data: %s
                    }]
                });
            });
    ''' % (str(negative(sorted_list(data_dict1['F'].items()))), str((sorted_list(data_dict1['M'].items()))))
    
        
    html += '''
        </script>
    </head>
    <body>
    <div id="topbar">
        <div class="indexdiv">
        <a href="/"><span id="top">Home</span></a>
        <a href="/fulldata"><span id="top">Data</span></a>
        <a href="/filter"><span id="top">Pivot Table Builder</span></a>
        <a href="/insights"><span id="top">Insights</span></a>
        <a href="/about"><span id="top">About Us</span></a>
        <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/>
        </div>
    </div>
    <div id="description" style="text-align:center">
        <h2>Examining the Relationships between home life, alcohol consumption
            and education.</h2>
    </div>
        
    <div class="row" id="age_sex_consumption">
        <div class="col-md-12 col-xs-12 col-lg-12 col-xs-12">
        <h2><strong> Intro : Trends in Alcohol consumption</strong></h2>
        <ul>
        <p> This shows us as they get older on average female students consume less alcohol, while male students consume more.</p>
        </ul>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart0" class="chart" style="width:100%;"></div>
        </div>     
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart10" class="chart" style="width:100%;"></div>
        </div>       
    </div><br>
    
    <div class="row" id="alcohol_average_sex">
        <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12">
        <h2><strong> The Effect of Weekday and Weekend Alcohol Consumption on Student's Average Grade</strong></h2>
        <ul> 
        <p> Interestingly, there doesn't appear to be a clear negative association between level of 
            alcohol consumption and average grade. </p>
        <p>The only hint of declining grades is evident in Males who drink more on the Weekends. </p>
        <p>According to the data, we can all go out and drink as much as we want and still maintain our grades. </p>
        </ul>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart1" class="chart" style="width:100%;"></div>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart2" class="chart" style="width:100%;"></div>
        </div>
    </div><br>
    
    <div class="row" id="weekendalc_fail_sex">
        <div class="col-md-6 col-xs-12 col-lg-6 col-xs-12">
        <h2><strong> The Effect of Weekend Alcohol Consumption on Student's Number of Failed Subjects</strong></h2> 
        <ul>
        <p> This shows us something more intuitive, that the greater people of both sexes consume alcohol 
            on the weekends, the more subjects they fail.</p>
        </>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart3" class="chart" style="width:100%;"></div>
        </div>       
    </div><br>
    
    <div class="row" id="family_weekendalc_sex">
        <div class="col-md-6 col-xs-12 col-lg-6 col-xs-12">
        <h2><strong> The Effect of Family Relationship Quality on Student's Weekend Alcohol Consumption</strong></h2>
        <ul>
        <p> The graph tells us that as the quality of family relationships decreases for males,
            the level of their alcohol consumption will most likely increase.</p>
        <p> On the other hand, this decreasing trend is not evident for females. </p>
        <p> Therefore, it can be concluded that a females' alcohol consumption is not affected by their
            relationship with their family. </p>
        </ul>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart4" class="chart" style="width:100%;"></div>
        </div>       
    </div><br>
    
    <div class="row" id="cohabitation_average_sex">
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <h2><strong> The Effect of Parent's Cohabitation Status on Student's Average Grade</strong></h2>
        <ul>
        <p> This demonstrates similar average grades in males, regardless
            of their parents' cohabitation status.</p>
        <p> Therefore, male youths' grades will not be affected by their 
            parent's cohabitation status. </p>
        <p> However, it is observed that females will have a higher average grade
			when their parents are apart than when they're together. </p>
        </ul>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart5" class="chart" style="width:100%;"></div>
        </div>
    </div><br>
    
    <div class="row" id="alcohol_study_sex">
        <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12">
        <h2><strong> The Effect of Weekday and Weekend Alcohol Consumption on Student's Study Time</strong></h2>
        <ul>
        <p> 
        From the graph we can see that alcohol consumptions during the weekend affect both gender (Female and Male), as they consume more
        alcohol during the weekend, their study time decrease. </p>
        <p> Even so, it seems that alcohol consumptions during the weekdays affect the female group more clearly and significant from
        the data of our graph. </p>
        </ul>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart8" class="chart" style="width:100%;"></div>
        </div>
        <div class="col-md-6 col-sm-12 col-lg-6 col-xs-12">
        <div id="chart9" class="chart" style="width:100%;"></div>
        </div>
    </div>

    </body>
    </html>
    '''

    return html

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)