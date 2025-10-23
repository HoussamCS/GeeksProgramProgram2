# Fixed version with proper database extraction
import urllib.request
import zipfile
import os
import sqlalchemy
from sqlalchemy import create_engine, func
import pandas as pd

print("=== CHINOOK DATABASE EXERCISES - FIXED VERSION ===")

# Download and extract properly
chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.db'):
    print('Downloading chinook.zip...')
    urllib.request.urlretrieve(chinook_url, 'chinook.zip')
    
    print('Extracting database...')
    with zipfile.ZipFile('chinook.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    
    print('✅ Database extracted successfully!')

# Test database connection
try:
    engine = create_engine('sqlite:///chinook.db')
    
    # Test connection with a simple query
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT name FROM sqlite_master WHERE type='table'"))
        tables = [row[0] for row in result]
        print(f"✅ Database working! Found {len(tables)} tables: {', '.join(tables[:5])}...")

    # Set up ORM
    metadata = sqlalchemy.MetaData()
    metadata.reflect(engine)

    from sqlalchemy.ext.automap import automap_base
    Base = automap_base(metadata=metadata)
    Base.prepare()

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get classes
    Track = Base.classes.tracks
    Album = Base.classes.albums
    Artist = Base.classes.artists
    InvoiceItem = Base.classes.invoice_items

    print("✅ All classes ready!")
    print(f"✅ Exercise 1: ✓ Database connection successful")
    print(f"✅ Exercise 2: ✓ Found {len(metadata.tables)} tables")
    
    # Test a quick query
    track_count = session.query(Track).count()
    print(f"✅ Exercise 3: ✓ Found {track_count} tracks in database")
    
    session.close()
    print("\n🎉 YOUR NOTEBOOK IS NOW READY TO RUN!")
    print("All exercises should work perfectly!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Database file may be corrupted. Please delete chinook.zip and chinook.db and try again.")