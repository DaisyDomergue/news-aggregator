# news-aggregator
A simple fast api rest app that either fetch latest news or search news from two sources (reddit and newsapi)

assumes python and make or cmake are install in ubuntu/mac

dependecies 
    fastapi
    pandas

    uvicorn

To install dependencies

```bash
make install-dependencies
```

To start the server

```bash
make start
```

To run unittest

```bash
make test
```

Get the latest News using cURL

```bash
curl --location --request GET '127.0.0.1:8000/'
```
Search a topic in the news

```bash
curl --location --request GET '127.0.0.1:8000/search/topic'
```
Replace topic with and subject you want to search

Blackbox Test 
Can also be done by importing the news-aggregator.postman_collection.json