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
print rows
print cols


html = '''
<html>
<head>
</head>
<body>
    <table>
        %s
    </table>
</body>
</html>
'''

table = '<tr><td></td>'
#First create the first row of the table with the column headers
for col in cols:
    table += '<td>%s</td>' % col
table += '</tr>'
for row in range(len(rows)):
    table += '<tr><td>%s</td>' % rows[row]
    for col in range(len(cols)):
        table += '<td> %s</td>' % data[row][col] 
    table += '</tr>'

with open('output.html', 'w') as output:
    output.write(html % table)


