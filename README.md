# Sensitive

## Description
In a mission to stop online harassment we present Sensitive. Sensitive uses Google's Youtube Data 3 API to get comments made on users accounts and automatically delete ones that score high in negative sentiment.

## Install

* Clone the repo -> https://github.com/sgp715/sensitive.git
* install sqlite
```
$ sudo apt-get install sqlite3 libsqlite3-dev
```
* install from requirements.txt
```
$ sudo pip install -r requirements.txt
```


## Usage

* To start running the webapp (binds to port 80)
```
$ sudo python server.py -p
```
* To start running the comment analyzer
```
$ python decomment.py
```
