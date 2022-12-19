# Data-Modeling-Postgres

First project submission for Udacity Data Engineering Nanodegree. Project consists of two parts:

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

Files used on the project








