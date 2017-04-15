## CTFWriteupScrapper

Scrap all writeup from http://ctftime.org/ and organize which to read first.

Initialize SQLite DB:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Start : `python runserver.py`

Open from browser `127.0.0.1:31337`

Update your database with latest writeup from ctftime : `127.0.0.1:31337/feed/`

## Requirements

- Flask
- BeautifulSoup
- urllib2
- mechanize

## Todo

Empty

## Screenshot

![Screen Shoot](screenshoot.png)

## License

MIT @abdilahrf
