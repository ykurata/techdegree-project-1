import csv

sharks = []
dragons = []
raptors = []
teams = {}

# read csvfile and split players into 3 teams
def split_players():
    with open("soccer_players.csv", newline = "") as csvfile:
        player = csv.reader(csvfile, delimiter = ",")
        rows = list(player)

        # Delete infomation about Height
        for row in rows:
            del row[1]

        exp = []
        no_exp = []

        # Split players to experience and inexperience
        for row in rows[1:]:
            if "YES" in row:
                exp.append(row)
            else:
                no_exp.append(row)
    # Split players into 3 teams
    sharks.extend(exp[:3] + no_exp[:3])
    dragons.extend(exp[3:6] + no_exp[3:6])
    raptors.extend(exp[6:] + no_exp[6:])

    return sharks, dragons, raptors

# Convert lists
def list_in_dict(sharks, dragons, raptors):
    teams.update({"sharks":sharks})
    teams.update({"dragons":dragons})
    teams.update({"raptors":raptors})
    return teams

def write_in_file():
    with open("teams.txt", "a") as file:
        file.write("Sharks \n")
        for value in teams["sharks"]:
            player_info = ", ".join(value)
            file.write(player_info + "\n")

        file.write("\nDragons \n")
        for value in teams["dragons"]:
            player_info = ", ".join(value)
            file.write(player_info + "\n")

        file.write("\nRaptors \n")
        for value in teams["raptors"]:
            player_info = ", ".join(value)
            file.write(player_info + "\n")

if __name__ == '__main__':
    split_players()
    list_in_dict(sharks, dragons, raptors)
    write_in_file()
