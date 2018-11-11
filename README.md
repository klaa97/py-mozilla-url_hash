# py-mozilla-url_hash
Simple Python tool to hash the url, avoiding a corrupt places.sqlite
# Description
Since last version of Mozilla, a column called "url_hash" was added into *places_sqlite*, the DB containing bookmarks. It can be useful to mass update through a python script bookmarks, and SQL could be really useful avoiding restoring and backing up with JSON files.
# Usage
You can import the python file in your library, or you can mass-fix a DB with url_fix with:

` python url_fix.py fullpathdoplacesqlite `

Importing the file, you'll need to pass as argument the connection to the database.
A toy example is oldreddit.py, that lets you convert all of your https://reddit.com links into https://old.reddit.com link, usage is the same as url_fix.py.
# Reference
https://dxr.mozilla.org/mozilla-central/source/mfbt/HashFunctions.h
https://github.com/bencaradocdavies/sqlite-mozilla-url-hash
