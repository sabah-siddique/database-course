#!/usr/bin/python3

## data set and info and stuff


# Imports
import cgi
import sqlite3

# to support debugging
import cgitb
cgitb.enable()

print ("Content-Type: text/html\r\n\r\n")
print("<html>")
## HTML head tag
print("<head>")
print("\t<title>FIFA 2017-2018 Player Stats - Results</title>")
print('<link rel="icon" type="image/png" href="soccer-ball.png">')
print('\t<link rel="stylesheet" type="text/css" href="fifa.css">')
print('\t<link href="https://fonts.googleapis.com/css?family=Montserrat|Roboto|Spectral+SC" rel="stylesheet">')
print("</head>")
## HTML body tag
print("<body>")
print("\t<header>")
print("\t\t<h1>FIFA 2017-2018 Player Stats</h1>")
print("\t\t<p>A complete record of statistics for every FIFA player</p>")
print("\t</header>")

# Get and store form results
#form = cgi.FieldStorage()   ## this is a dictionary!
#club_name = form["club"].value
#num_players = form["quantity"].value
#sort_key = form["sorting"].value

# Open the database
#conn = sqlite3.connect("fifa.db")
#c = conn.cursor()

# Store the query in a string
#query = 'SELECT name, age, nationality, pac, sho, pas, dri, def, phy, crossing, finishing, heading_accuracy, volleys, free_kick_accuracy, ball_control, acceleration, sprint_speed, reactions, balance, stamina, gk_diving, gk_kicking'
#query += 'FROM fifa WHERE club = "' + club_name + '"'
#query += 'ORDER BY ' + sort_key + ' LIMIT ' str(num_players) + ';'

print("\t<main>")
print('\t\t<section class="description">')
print('\t\t\t<p>Here is the query: ' + '</p>')
print('\t\t\t<p>View your results below!</p>')
print('\t\t</section>')
## Table section
'''print('\t\t<section class="table">')
print('\t\t\t<table>')
print('\t\t\t\t<tr>')
print('\t\t\t\t\t<th>Name</th>')
print('\t\t\t\t\t<th>Full Name</th>')
print('\t\t\t\t\t<th>Age</th>')
print('\t\t\t\t\t<th>Nationality</th>')
print('\t\t\t\t\t<th>PC</th>')
print('\t\t\t\t\t<th>SHO</th>')
print('\t\t\t\t\t<th>PAS</th>')
print('\t\t\t\t\t<th>DRI</th>')
print('\t\t\t\t\t<th>DEF</th>')
print('\t\t\t\t\t<th>PHY</th>')
print('\t\t\t\t\t<th>CRO</th>')
print('\t\t\t\t\t<th>FI</th>')
print('\t\t\t\t</tr>')

print('\t\t\t</table>')
## Key for table
print('\t\t\t<p></p>')
print('\t\t</section>')
'''

print('</main>')
print('</body>')
print("</html>")

#c.close()
