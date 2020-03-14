# IMDB Scraper

![](https://img.shields.io/github/license/dojutsu-user/IMDB-Scraper.svg?style=for-the-badge)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg?style=for-the-badge)](https://GitHub.com/dojutsu-user/IMDB-Scraper/graphs/contributors/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/dojutsu-user/IMDB-Scraper/pulls)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Overview

This is a [Scrapy](https://github.com/scrapy/scrapy) project which can be used to crawl [IMDB](https://www.imdb.com/) website to scrape movies' information and then store the data in `json` format. 

## Crawling

1. Clone the repo and navigate into `IMDB-Scraper` folder.
```
$ git clone https://github.com/dojutsu-user/IMDB-Scraper.git
$ cd IMDB-Scraper/
```
2. Create and activate a virtual environment.
```
(IMDB-Scraper) $ pipenv shell
```
3. Install all dependencies.
```
(IMDB-Scraper) $ pipenv install
```
4. Navigate into `imdb_scraper` folder.
```
(IMDB-Scraper) $ cd imdb_scraper/
```
5. You can change the starting page of the crawler in the file `imdb_scraper/spiders/movie.py` by changing the `SEARCH_QUERY` variable. You can get your own query from here: [imdb.com/search/title](https://www.imdb.com/search/title). Copy the generated URL and paste it in place of default url. By default:
```python3
SEARCH_QUERY = (
    'https://www.imdb.com/search/title?'
    'title_type=feature&'
    'user_rating=1.0,10.0&'
    'countries=us&'
    'languages=en&'
    'count=250&'
    'view=simple'
)
```
7. Start the crawler.
```
(IMDB-Scraper) $ scrapy crawl movie
```
8. Data will be stored in `json` file named `movie.json` located at `IMDB-Scraper/imdb-scraper/data/movie.json`.


The final data will be in the form:

```
[
    ...
    {
        ...
    },
    {
        "title": "12 Strong",
        "rating": "R",
        "year": "2018",
        "users_rating": "6.6",
        "votes": "42,919",
        "metascore": "54",
        "img_url": "https://m.media-amazon.com/images/M/MV5BNTEzMjk3NzkxMV5BMl5BanBnXkFtZTgwNjY2NDczNDM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
        "countries": [
            "USA"
        ],
        "languages": [
            "English",
            "Dari",
            "Russian",
            "Spanish",
            "Uzbek"
        ],
        "actors": [
            "Chris Hemsworth",
            "Michael Shannon",
            "Michael Peña",
            "Navid Negahban",
            "Trevante Rhodes",
            "Geoff Stults",
            "Thad Luckinbill",
            "Austin Hébert",
            "Austin Stowell",
            "Ben O'Toole",
            "Kenneth Miller",
            "Kenny Sheard",
            "Jack Kesy",
            "Rob Riggle",
            "William Fichtner"
        ],
        "genre": [
            "Action",
            "Drama",
            "History",
            "War"
        ],
        "tagline": "The Declassified True Story of the Horse Soldiers",
        "description": "12 Strong tells the story of the first Special Forces team deployed to Afghanistan after 9/11; under the leadership of a new captain, the team must work with an Afghan warlord to take down the Taliban.",
        "directors": [
            "Nicolai Fuglsig"
        ],
        "runtime": "130 min",
        "imdb_url": "https://www.imdb.com/title/tt1413492/"
    },
    {
        ...
    }
    ...
]
```


## Stats

These are the **FINAL** stats when the default `SEARCH_QUERY` is used.

```python3
{
    "downloader/exception_count": 32,
    "downloader/exception_type_count/twisted.internet.error.ConnectError": 8,
    "downloader/exception_type_count/twisted.internet.error.TimeoutError": 24,
    "downloader/request_bytes": 46219942,
    "downloader/request_count": 58931,
    "downloader/request_method_count/GET": 58931,
    "downloader/response_bytes": 2522617013,
    "downloader/response_count": 58899,
    "downloader/response_status_count/200": 58899,
    "dupefilter/filtered": 9829,
    "finish_reason": "finished",
    "finish_time": datetime.datetime(2018, 12, 28, 12, 37, 8, 676592),
    "item_scraped_count": 58623,
    "log_count/DEBUG": 117556,
    "log_count/INFO": 299,
    "memusage/max": 639164416,
    "memusage/startup": 52166656,
    "request_depth_max": 235,
    "response_received_count": 58899,
    "retry/count": 32,
    "retry/reason_count/twisted.internet.error.ConnectError": 8,
    "retry/reason_count/twisted.internet.error.TimeoutError": 24,
    "scheduler/dequeued": 58930,
    "scheduler/dequeued/memory": 58930,
    "scheduler/enqueued": 58930,
    "scheduler/enqueued/memory": 58930,
    "start_time": datetime.datetime(2018, 12, 28, 7, 46, 8, 317470)
}

 ```
 ## IMDB Movie Dataset (58,623 Movies)
 
 The dataset obtained from the above crawler is uploaded in the Google Drive and can be downloaded from this link: https://drive.google.com/open?id=13OE6CyqqDqJRpP-8JR15l9Tjb2fSWa6r
 
 
## Disclaimer

The project and the obtained dataset is intended only for educational purpose. It is completely open source and has no value intentions to commercialise complete or any part of the same. The developer is on no part the owner of any resources used and does not claim to hold the permissions to use the project.
