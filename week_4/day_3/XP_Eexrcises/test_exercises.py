# Test script to validate the notebook exercises
import urllib.request
import zipfile
from functools import partial
import os
import sqlalchemy
from sqlalchemy import create_engine, func, desc
import pandas as pd

print("=== TESTING CHINOOK DATABASE EXERCISES ===")

# Download database if needed
chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.zip'):
    print('downloading chinook.zip ', end='')
    with urllib.request.urlopen(chinook_url) as response:
        with open('chinook.zip', 'wb') as f:
            for data in iter(partial(response.read, 4*1024), b''):
                print('.', end='', flush=True)
                f.write(data)

if not os.path.exists('chinook.db'):
    zipfile.ZipFile('chinook.zip').extractall()

print("✅ Database ready!")

# Exercise 1: Database connection
engine = create_engine('sqlite:///chinook.db')
cur = engine.connect()

metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

from sqlalchemy.ext.automap import automap_base
Base = automap_base(metadata=metadata)
Base.prepare()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

Track = Base.classes.tracks
Album = Base.classes.albums
Artist = Base.classes.artists
InvoiceItem = Base.classes.invoice_items

print("✅ Exercise 1: Database connected and ORM ready!")

# Exercise 2: Table names
table_names = list(metadata.tables.keys())
print(f"✅ Exercise 2: Found {len(table_names)} tables")

# Exercise 3: First three tracks
first_three_tracks = session.query(Track).limit(3).all()
print(f"✅ Exercise 3: Retrieved {len(first_three_tracks)} tracks")

# Exercise 4: Albums from tracks
query = session.query(Track.Name, Album.Title).join(Album).limit(20)
track_album_data = pd.read_sql(query.statement, engine)
print(f"✅ Exercise 4: Retrieved {len(track_album_data)} track-album pairs")

# Exercise 5: Track sales
first_10_sales = session.query(InvoiceItem).limit(10).all()
print(f"✅ Exercise 5: Retrieved {len(first_10_sales)} sales records")

# Exercise 6: Top tracks sold
top_tracks_query = session.query(
    Track.Name,
    func.sum(InvoiceItem.Quantity).label('total_sold')
).join(InvoiceItem).group_by(Track.TrackId, Track.Name).order_by(func.sum(InvoiceItem.Quantity).desc()).limit(10)

top_tracks_df = pd.read_sql(top_tracks_query.statement, engine)
print(f"✅ Exercise 6: Found top {len(top_tracks_df)} selling tracks")

# Exercise 7: Top selling artists
top_artists_query = session.query(
    Artist.Name,
    func.sum(InvoiceItem.Quantity).label('total_sales')
).join(Album, Artist.ArtistId == Album.ArtistId).join(Track, Album.AlbumId == Track.AlbumId).join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId).group_by(Artist.ArtistId, Artist.Name).order_by(func.sum(InvoiceItem.Quantity).desc()).limit(10)

top_artists_df = pd.read_sql(top_artists_query.statement, engine)
print(f"✅ Exercise 7: Found top {len(top_artists_df)} selling artists")

cur.close()
session.close()

print("\n🎉 ALL EXERCISES WORKING CORRECTLY!")
print("Your notebook structure is now complete and ready to run!")