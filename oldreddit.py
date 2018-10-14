from url_fix import url_fix
import argparse
import sqlite3

def oldreddit(conn):
    c = conn.cursor()
    c.execute("UPDATE moz_places SET url = replace(url, 'https://reddit.com/', 'https://old.reddit.com/'), url_hash = 0 WHERE url like 'https://reddit.com/%'")
    conn.commit()
    url_fix(conn)
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fullpath",help="Insert the path of the DB to update")
    fullpath = parser.parse_args().fullpath
    oldreddit(sqlite3.connect(fullpath))