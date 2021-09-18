# Web Scraping Top 250 `IMDb` Movies Project

## Author: Dr Mike Lakoju

> ### The goal of this project is to build a crawl spider to scrape the top 250 movies as rated by IMDb Users.

**IMDb** is an online database of information related to films, television programs, home videos, video games, and streaming content online – including cast, production crew and personal biographies, plot summaries, trivia, ratings, and fan and critical reviews. _Source: Wikipedia_

web Link :  `https://www.imdb.com/chart/top/?ref_=nv_mv_250`

List of items crawled:

* Movie Title
* Year of Movie
* Duration of Movie
* Genre
* Rating
* Movie URL

### ***** To RUN *****
Note: the name of the spider is "best_movies"

* To run and see output on Terminal/command line :  `scrapy crawl best_movies`

* To run and save output as a json file: `scrapy crawl best_movies -o dataset.json`

* To run and save output as a csv file: `scrapy crawl best_movies -o dataset.csv`

