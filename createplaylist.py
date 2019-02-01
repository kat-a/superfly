#!/usr/bin/env python

import sys
import requests
import sqlite3
from collections import namedtuple

base_url = 'https://superfly.fm/player/playlist/playlist.json'

try:
    conn = sqlite3.connect('tracks.db')
    c = conn.cursor()

    r = requests.get(base_url)
    json = r.json()

    for track in json['tracks']:
        c.execute("INSERT OR IGNORE INTO tracks (id,tracktime,artist,title,url) VALUES (?,?,?,?,?)", (track['id'], track['tracktime'], track['artist'], track['title'], track['url']))

    conn.commit()

except requests.exceptions.RequestException as e:
    print("Catched an error: {}".format(e))
    sys.exit(1)

finally:
    conn.close()
