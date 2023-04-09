# Twitch data pipeline

## Overview
This project aims to collect data from a specific Twitch streamer using an API, load it to a local database and visualize data using a data visualization tool. The streamer we collected data on is Gaules, one of the top Twitch streamers wordlwide and the most popular streamer in Brazil. Data was collected from March 29th to Abril 5th (1 week).

## Architecture
![Data architecture](/images/twitch_viewers_chart.png "Data architecture")
1. Extract current data from Twtich using the [Twitch API hosted on RapidAPI](https://rapidapi.com/kingsizeblock/api/gwyo-twitch/)
2. Use [Docker Compose](https://docs.docker.com/compose/) to manage and run both [Postgres](https://www.postgresql.org/) and [Metabase](https://www.metabase.com/) images
3. Clean and write current data to the [Postgres](https://www.postgresql.org/) database
4. Visualize data using personalized queries inside [Metabase](https://www.metabase.com/)

## Output
![Dashboard](/images/dashboard.png "Dashboard")

## Local setup
To execute the project locally, you will need Docker and Postgres running on your personal computer. 

1_ First, clone this repository into your home directory

```
git clone https://github.com/ribeiroluan/twitch-viewers
cd Reddit-API-Pipeline
```

2_ Next, install all projects requirements

```
pip install -r requirements.txt
```

3_ Create a `.env` file in the `gaules` directory with the following format:
```
KEY = your_rapid_api_key
```

4_ Edit `main.py` according to your needs. You will need to select both the streamer you want to collect data for `streamer` and the period you want the data to be collected `start_time` and `end_time`.


5_ Open Docker and initialize the container containing both Postgres and Metabase images
```
docker-compose up
```

6_ Setup up your database connection to Metabase through your localhost (Metabase's default port is 3000)
```
http://localhost:3000/
```

7_ Run the pipeline 
```
python gaules/main.py
```

You are all set to generate charts in Metabase using SQL queries!