# Data-Modeling-Postgres

First project submission for based on Udacity's Data Engineering Nanodegree. Project consists of two parts:

1. Data model and the creation of star schema database with Postgres (using the `psycopg2` Python driver)
2. Build an ETL pipeline using Python

## Context

### Project Specification

An analytics team wants to query data which resides in a directory of JSON logs on user activity on an app,
as well as a directory with JSON metadata on the songs on their app.

```commandline
1) Directory of JSON logs on user activity on the app (*/data/log_data*)
2) Directory with JSON metadata on the songs on their app (*/data/song_data*)
```
The minimum project requirement is to create a database schema and ETL pipeline for analysis.

### Data

**Song datasets:** is in JSON format and contains metadata about a song and the artist of that song. All json
files are nested in subdirectories under /data/song_data. A sample of a single row:
```commandline
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

**Log data:** JSON files nested under _/data/log_data_. A sample of a single row:

```commandline
cat data/log_data/2018/11/2018-11-01-events.json| grep 1541016707796.0 | grep 1541109125796 | python -m json.tool
{
    "artist": "Fall Out Boy",
    "auth": "Logged In",
    "firstName": "Ryan",
    "gender": "M",
    "itemInSession": 1,
    "lastName": "Smith",
    "length": 200.72444,
    "level": "free",
    "location": "San Jose-Sunnyvale-Santa Clara, CA",
    "method": "PUT",
    "page": "NextSong",
    "registration": 1541016707796.0,
    "sessionId": 169,
    "song": "Nobody Puts Baby In The Corner",
    "status": 200,
    "ts": 1541109125796,
    "userAgent": "\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36\"",
    "userId": "26"
}
```
## Database Schema

Fact and dimension tables are used to create an organised data model. One main fact table named `songplays`
contains all the measures associated to each table. Four dimensional tables -- each containing a primary
key referenced from the Fact table.

### **Fact Table**

**songplays -** records in log data associated with song plays, i.e. records with psgr `NextSong`

* songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### **Dimension Table**

**users -** users in the app

* user_id, first_name, last_name, gender, level

**songs -** songs in music database

* song_id, title, artist_id, year, duration

**artists -** artists in music database

* artist_id, name, location, latitude, longitude

**time -** timestamp of records in **songplays** broken down into specific units

* start_time, hour, day, week, month, year, weekday

## Project Structure

#### Files used on the project

1. **data** folder nested at the home of the project
2. **sql_queries.py** contains SQL queries needed to initiate the tables, and is imported into the files below
3. **create_tables.py** drops and creates tables. This file is run to reset tables each time before the ETL scripts are run
4. **test.ipynb** displays the first few rows of each table to inspect the database
5. **etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into tables
6. **etl.py** reads and processes all files from song_data and log_data and loads them into your tables.
7. **README.md** current file, provides overview of the project.

#### Step by step overview

1. Write DROP, CREATE, INSERTS statements in `sql_queries.py`
2. Run `create_tables.py` to create database and tables
3. Use `test.ipynb` to confirm creation of tables with the correct columns
4. Complete `etl.py` script using completed code in `etl.ipynb` as a base
5. Run `etl.py` to verify ETL logic is work as expected

## ETL Pipeline Summary

1. Connect to the Sparkify database
2. Cycle through files under `/data/song_data`, and for each file, send to the function named `process_song_file`
3. This function loads each song file into a dataframe and selects only the fields required to generate the table before insertion. Example:
```commandline
    song_data = df[["song_id", "title", "artist_id", "year", "duration"]].values[0].tolist()
```
```commandline
    artist_data = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]].values[0].tolist()
```
4. Cycle through files under `/data/log_data`, and for each file, send to the function named `process_log_file`
5. This function loads each file where `page = NextSong` into a dataframe and selects only the fields required to generate the tables before insertion
   1. Notably the `ts` attribute is converted from Unix time to timestamp. Then this is used as the `start_time` field in the `time_data` and all additional fields are generated using the `datetime` library
```commandline
    time_df = ['timestamp', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']
```
```commandline
    user_df = ['userId', 'firstName', 'lastName', 'gender', 'level']
```
6. Lookup the `songId` and `artistId` from their respective tables by song name, artist name, and song duration in order to complete the `songplay` fact table using the following query
```commandline
    song_select = ("SELECT SONGS.song_id, ARTISTS.artist_id from SONGS JOIN ARTISTS ON SONGS.artist_id = ARTISTS.artist_id \
                WHERE \
                SONGS.title = %s \
                AND ARTISTS.name = %s \
                AND SONGS.duration = %s \
                ")
```
7. The last step is inserting everything into the `songplay` fact table

## Project checklist

  - [x] Table creation script (`create_table.py`) runs without errors
  - [x] Fact and dimensional tables for a star schema are properly defined
  - [x] ETL script (`etl.py`) runs without errors
  - [x] ETL script properly processes transformations in Python 
  - [x] The project shows proper use of documentation
  - [x] The project code is clean and modular
  - [ ] (BONUS) Insert data using the COPY command to bulk insert log files instead of using INSERT on one row at a time
  - [ ] (BONUS) Add data quality checks
  - [ ] (BONUS) Create a dashboard for analytic queries on your new database




