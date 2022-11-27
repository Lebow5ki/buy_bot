import csv
import sqlite3
from request_edit import request


def main():
    with open("out.csv", encoding="utf-8", newline="") as f, \
            sqlite3.connect("contacts.db") as conn:
        conn.execute("""DROP TABLE IF EXISTS  contacts""")
        conn.execute("""
                        CREATE TABLE
                        if not exists
                        contacts (
                        classid text,
                        instanceid text,
                        price text,
                        offers text,
                        market_hash_name text
                        )""")
        conn.executemany("INSERT INTO contacts VALUES (?,?,?,?,?)",
                         csv.reader(f))

if __name__ == "__main__":
    request()
    main()
