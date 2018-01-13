import csv

def read_players():
    with open("soccer_players.csv", newline = "")as csvfile:
        player = csv.DictReader(csvfile, delimiter=",")
        rows = list(player)

        for row in rows:


        exp = []
        no_exp = []
        for row in rows[1:]:
            if "YES" in row:
                exp.append(row)
            else:
                no_exp.append(row)
        print(exp)
        print(no_exp)



read_players()
