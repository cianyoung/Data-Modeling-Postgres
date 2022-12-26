"""
Module contains string constants which contain SQL scripts for creating and dropping tables as well as inserting data into tables
"""

# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays;"
user_table_drop = "DROP table IF EXISTS users;"
song_table_drop = "DROP table IF EXISTS songs;"
artist_table_drop = "DROP table IF EXISTS artists;"
time_table_drop = "DROP table IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp NOT NULL REFERENCES time(start_time),
    user_id INT  NOT NULL REFERENCES users(user_id),
    level varchar NOT NULL,
    song_id varchar REFERENCES songs(song_id),
    artist_id varchar REFERENCES artists(artist_id),
    session_id int NOT NULL,
    location text,
    user_agent text
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    gender varchar,
    level varchar NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar NOT NULL,
    location varchar,
    latitude numeric,
    longitude numeric
);
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY,
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday int NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar NOT NULL,
    artist_id varchar NOT NULL,
    year int NOT NULL,
    duration numeric NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO
        UPDATE SET
        first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name,
        gender = EXCLUDED.gender,
        level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO
        UPDATE SET
        title = EXCLUDED.title,
        artist_id = EXCLUDED.artist_id,
        year = EXCLUDED.year,
        duration = EXCLUDED.duration
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO
        UPDATE SET
        name = EXCLUDED.name,
        location = EXCLUDED.location,
        latitude = EXCLUDED.latitude,
        longitude = EXCLUDED.longitude
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("SELECT SONGS.song_id, ARTISTS.artist_id from SONGS JOIN ARTISTS ON SONGS.artist_id = ARTISTS.artist_id \
                WHERE \
                SONGS.title = %s \
                AND ARTISTS.name = %s \
                AND SONGS.duration = %s \
                ")


# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]