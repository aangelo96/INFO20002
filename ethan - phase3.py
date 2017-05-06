from csv import DictReader
data = DictReader(open("Edited Data2.csv"))
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


html = '''
<html>
<head>
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
    <link rel="stylesheet" href="pivot.css">
</head>
<body>
    <div id="topbar">
        <div class = "indexdiv"><span>Home</span></div>
        <div class = "indexdiv"><span>Pivot Table Builder</span></div>
        <div class = "indexdiv"><span>Insights</span></div>
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
        table += '<td> %s</td>' % data[row][col] 
    table += '</tr>'

#Then, we add the total of each column and write it in.
table += '<tr><td>Total</td>'
# for row in range(len(data)):
#     total = 0
#     for col in range(len(data[0])):
#         total += 

for row in range(len(data[0])):
    total = 0
    for col in range(len(data)):
        total += data[col][row]

    table += '<td>%s</td>' % str(total)
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
with open('output.html', 'w') as output:
    output.write(html)
