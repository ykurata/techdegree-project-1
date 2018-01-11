import csv

with open("soccer_players.csv")as csvfile:
    readfile = csv.DictReader(csvfile, ddelimiter=",")
    rows = clist(readfile)
    print(rows)
