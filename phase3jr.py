#Jorjilou Reyes, Arnold Angelo, Ethan Cheng
#May 2017, Semester 1, Foundations of Informatics
#Phase 3 of 3 of Project
#user-selected attributes from the columns of a csv file are organized and 
#aggregated into a 2d data which is then returned by the main function

import csv
from collections import defaultdict

#FUNCTIONS
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
		return "GO"
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











