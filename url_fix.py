from url_hash import url_hash
import sqlite3
import argparse

def url_fix(conn):
    conn.create_function("urlhash",1,url_hash)
    c = conn.cursor()
    c.execute("UPDATE moz_places SET url_hash = urlhash(url) WHERE urlhash(url) <> url_hash")
    conn.commit()
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fullpath",help="Insert the FULLPATH to places.sqlite DB")
    fullpath = parser.parse_args().fullpath
    url_fix(sqlite3.connect(fullpath))
