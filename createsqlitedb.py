#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('tracks.db')
c = conn.cursor()

c.execute('''CREATE TABLE if not exists tracks
             (id integer UNIQUE, tracktime text UNIQUE,
              artist text, title text, url text)''')

conn.commit()
conn.close()
print("done")
