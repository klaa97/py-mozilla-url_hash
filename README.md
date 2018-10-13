# py-mozilla-url_hash
Simple Python tool to hash the url, avoiding a corrupt places.sqlite
# Description
Since last version of Mozilla, a column called "url_hash" was added into *places_sqlite*, the DB containing bookmarks. It can be useful to mass update through a python script bookmarks, and SQL could be really useful avoiding restoring and backing up with JSON files.

