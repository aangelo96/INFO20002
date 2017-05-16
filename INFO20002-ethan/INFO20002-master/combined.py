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

@app.route('/')
def route():
    home_page = '''
<!doctype html>
<html>
<head>
    <title>Pivot Table - Filters</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="final_home.css">
    
</head>
<body>
<h1 align="center"> Alcoholic Data Set and Pivot Table Builder <img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/> </h1>
<br>
<hr>
<br>
<p id="aop"> About Our Project : </p>
<ul id="about">
    <li> What is our Data About ? <br>
         Our Data is about <b>Student Alcohol Consumption</b> of some secondary school students </li>
    <li> Where do we obtained this Data ? <br>
         We obtained our data from <a href="https://www.kaggle.com/uciml/student-alcohol-consumption">Keggle</a> !!! </li>
    <li> What are the "attributes" we used for our project ? <br>
         For this project, we are only using these attributes : 
         <ol>
             <li> Sex </li>
             <li> Age </li>
             <li> Parents Cohabitation Status </li>
             <li> Study Time </li>
             <li> Number of Failed Subject </li>
             <li> Daily Alcohol Consumption </li>
             <li> Weekly Alcohol Consumption </li>
             <li> Number of Absences </li>
             <li> Average Grade </li>
         </ol>
</ul>

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
    <p> Jorjilou Reyes - 836917 </p>
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
    <link rel="stylesheet" href="final_full.css">
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
    csvfile.close()

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
    <link rel="stylesheet" href="final_filter.css">
   
    
    
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
          <option value="Daily Alcohol Consumption"> Daily Alcohol Consumption </option>
          <option value="Weekly Alcohol Consumption"> Weekly Alcohol Consumption </option>
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
        <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
        <link rel="stylesheet" href="final_pivot.css">
    </head>
    <body>
        <div id="topbar">
            <div class = "indexdiv"><a href="/"><span id="top">Home</span></a>
            <a href="/filter"><span id="top">Pivot Table Builder</span></a>
            <a href="http://www.nyan.cat"><span id="top">Insights</span></a></div>
        </div>
        <div id="header">
            <h1 id = "title">Pivot Table<img id = "beer" src="https://image.flaticon.com/icons/svg/126/126613.svg"/></h1> 
            
        </div>
        <div id="about">
            <h3>A comparison of <span id="details">%s</span> and <span id="details">%s</span></h3>
            <h3>With respect to the <span id="details">%s</span> : <span id="details">%s</span></h3>
            <h3>When %s %s %s</span></h3>
        <hr>
    '''
    html += '<div id="contentdiv">'          
    html += '<table id="myTable"><tr><td></td>'
    #Add Column Tag
    for col in cols :
        html += '<td>'+col+'</row>'
    #Add Total Tag
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
        
    #use createbins
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
    html +='</tr>'

    html += '''
    </table>
    </div>
    '''
    html += '</body></html>'
    
    
    
    print(data_array)
    return html % (irow,icol,agg_op, agg_val,fil_sect,fil_sign,fil_val)
    


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)