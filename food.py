import json
import sqlite3
from datetime import date

expirations = {"BEEF": 4,
               "CHICKEN": 4,
               "PORK": 4,
               "CABBAGE": 30,
               "CORN": 4,
               "CUCUMBER": 10,
               "EGGPLANT": 11,
               "SPINACH": 11,
               "MUSHROOM": 7,
               "TOMATO": 5,
               "AVOCADO": 10,
               "POTATO": 60,
               "CARROT": 45,
               "ONION": 60,
               "SHELLFISH": 1,
               "FISH": 1}

base = sqlite3.connect("FoodItems.db")
cursor = base.cursor()

cursor.execute("""CREATE TABLE food (foodsort TEXT, foodtype TEXT, date TEXT,
                                     quantity TEXT, expiration INTEGER)""")


# JSON to python
def processin(data):
    retrieve = json.loads(data)

    retrieve["expdate"] = expirations[retrieve["foodtype"].upper()]

    cursor.execute("INSERT INTO food VALUES (?, ?, ?, ?, ?)",
                   (retrieve["foodsort"],
                    retrieve["foodtype"],
                    retrieve["date"],
                    retrieve["quantity"],
                    retrieve["expdate"]))
    base.commit()


# python -> JSON
def processout():
    tup = ["foodsort", "foodtype", "date", "quantity", "expiration"]
    datapull = cursor.execute("""SELECT foodsort,
                                foodtype,
                                date,
                                quantity,
                                expiration
                                FROM food""").fetchall()
    ret = []
    for i in datapull:
        ret.append(dict(zip(tup, i)))
    print(json.dumps(ret))


# take date and compare
def calendar(n):
    day = date(int(n.split(".")[2]),
               int(n.split(".")[0]),
               int(n.split(".")[1]))
    past = None
    if day != past:
        # edit database
        if past is None:
            past = day
            quit()
        delta = day - past
        for i in range(len(cursor.execute
                           ("SELECT foodsort FROM food").fetchall())):
            expdatedelta = cursor.execute("""SELECT expiration FROM food""").fetchone()[0]
            cursor.execute("""UPDATE food SET expiration = ? - ?""",
                           (expdatedelta, delta.days))
    past = day
    cursor.execute("DELETE FROM food WHERE expiration < -3")

    base.commit()
