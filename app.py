import pandas
import sqlite3
from sqlalchemy import create_engine
from flask import Flask
from flask import render_template

app = Flask(__name__)

# # Remove me later, just here for reference when adding other tables
# db = create_engine('sqlite:///data.db')
# df = pandas.read_csv('database/csvdata/knicks.csv')
# df.to_sql(
#     name = 'knicks',
#     con=db,
#     if_exists='replace',
#     index=False
# )
# df = pandas.read_csv('database/csvdata/knicksreg.csv')
# df.to_sql(
#     name = 'knicksreg',
#     con=db,
#     if_exists='replace',
#     index=False
# )

@app.route("/")
def homepage():
    return render_template('home.html.jinja')

@app.route("/<playerid>")
def playerid(playerid):
    connection = sqlite3.connect('data.db')
    term = connection.cursor()

    allshots = []
    allmakes = [0,0,0,0,0]
    allmisses = [0,0,0,0,0]
    fgpercent = [0,0,0,0,0]
    term.execute("SELECT * FROM KNICKS WHERE Playeradditional = '" + playerid + "'")
    for row in term.fetchall():
        if "make" in row[10]:
            match row[2]:
                case "2026-06-03":
                    allmakes[0] += 1
                case "2026-06-05":
                    allmakes[1] += 1
                case "2026-06-08":
                    allmakes[2] += 1
                case "2026-06-10":
                    allmakes[3] += 1
                case "2026-06-13":
                    allmakes[4] += 1
        else:
            match row[2]:
                case "2026-06-03":
                    allmisses[0] += 1
                case "2026-06-05":
                    allmisses[1] += 1
                case "2026-06-08":
                    allmisses[2] += 1
                case "2026-06-10":
                    allmisses[3] += 1
                case "2026-06-13":
                    allmisses[4] += 1
        allshots.append(row)

    for i in range(5):
        if (allmakes[i] + allmisses[i]) == 0:
            fgpercent[i] = 0
        else:
            fgpercent[i] = round(allmakes[i] / (allmakes[i] + allmisses[i]), 3)

    term.execute("SELECT * FROM KNICKSREG WHERE Playeradditional = '" + playerid + "'")
    playerstats =  term.fetchone()
    connection.commit()
    connection.close()
    # print(allshots)
    return render_template('player_id.html.jinja', allshots=allshots, url=1, playerstats = playerstats, makes=allmakes, misses=allmisses, percent = fgpercent, playerid=playerid)

@app.route("/<playerid>/threes")
def playeridthrees(playerid):
    connection = sqlite3.connect('data.db')
    term = connection.cursor()

    threeshots = []
    threemakes = [0,0,0,0,0]
    threemisses = [0,0,0,0,0]
    threepercent = [0,0,0,0,0]
    term.execute("SELECT * FROM KNICKS WHERE Playeradditional = '" + playerid + "' AND Description LIKE '%3-pt%'")
    for row in term.fetchall():
        if "make" in row[10]:
            match row[2]:
                case "2026-06-03":
                    threemakes[0] += 1
                case "2026-06-05":
                    threemakes[1] += 1
                case "2026-06-08":
                    threemakes[2] += 1
                case "2026-06-10":
                    threemakes[3] += 1
                case "2026-06-13":
                    threemakes[4] += 1
        else:
            match row[2]:
                case "2026-06-03":
                    threemisses[0] += 1
                case "2026-06-05":
                    threemisses[1] += 1
                case "2026-06-08":
                    threemisses[2] += 1
                case "2026-06-10":
                    threemisses[3] += 1
                case "2026-06-13":
                    threemisses[4] += 1
        threeshots.append(row)

    for i in range(5):
        if (threemakes[i] + threemisses[i]) == 0:
            threepercent[i] = 0
        else:
            threepercent[i] = round(threemakes[i] / (threemakes[i] + threemisses[i]), 3)

    term.execute("SELECT * FROM KNICKSREG WHERE Playeradditional = '" + playerid + "'")
    playerstats =  term.fetchone()
    connection.commit()
    connection.close()
    # print(allshots)
    return render_template('player_id.html.jinja', allshots=threeshots, url=3, playerstats=playerstats, makes=threemakes, misses=threemisses, percent = threepercent, playerid=playerid)

@app.route("/<playerid>/twos")
def playeridtwos(playerid):
    connection = sqlite3.connect('data.db')
    term = connection.cursor()

    twoshots = []
    twomakes = [0,0,0,0,0]
    twomisses = [0,0,0,0,0]
    twopercent = [0,0,0,0,0]
    term.execute("SELECT * FROM KNICKS WHERE Playeradditional = '" + playerid + "' AND Description LIKE '%2-pt%'")
    for row in term.fetchall():
        if "make" in row[10]:
            match row[2]:
                case "2026-06-03":
                    twomakes[0] += 1
                case "2026-06-05":
                    twomakes[1] += 1
                case "2026-06-08":
                    twomakes[2] += 1
                case "2026-06-10":
                    twomakes[3] += 1
                case "2026-06-13":
                    twomakes[4] += 1
        else:
            match row[2]:
                case "2026-06-03":
                    twomisses[0] += 1
                case "2026-06-05":
                    twomisses[1] += 1
                case "2026-06-08":
                    twomisses[2] += 1
                case "2026-06-10":
                    twomisses[3] += 1
                case "2026-06-13":
                    twomisses[4] += 1
        twoshots.append(row)

    for i in range(5):
        if (twomakes[i] + twomisses[i]) == 0:
            twopercent[i] = 0
        else:
            twopercent[i] = round(twomakes[i] / (twomakes[i] + twomisses[i]), 3)

    term.execute("SELECT * FROM KNICKSREG WHERE Playeradditional = '" + playerid + "'")
    playerstats =  term.fetchone()

    connection.commit()
    connection.close()
    # print(allshots)
    return render_template('player_id.html.jinja', allshots=twoshots, url=2, playerstats=playerstats, makes=twomakes, misses=twomisses, percent = twopercent, playerid=playerid)