from project import app, db
from flask import render_template
from models import Writeups
from bs4 import BeautifulSoup
import cookielib
import mechanize


@app.route('/feed/')
def feed():
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Chrome')]
    x = 1

    while True:
        temp = []

        try:
            # get all web writeup
            content = br.open('https://ctftime.org/writeups?page=' + str(x) + '&hidden-tags=web').read()
        except Exception, e:
            break
            # print "error: " + str(e)

        soup = BeautifulSoup(content, 'html.parser')
        datas = soup.findAll('td')

        cnt = 0
        for r in range(len(datas) / 5):

            # Jika udah ada di database skip
            id_writeup = datas[cnt+4].next['href'].split("/")[::-1][0]
            cek_writeup = Writeups.query.filter_by(idwriteup=id_writeup).first()
            if cek_writeup:
                cnt += 5
                continue
            else:

                try:
                    originalWriteup = BeautifulSoup(br.open("https://ctftime.org" + datas[cnt + 4].next['href']).read(), 'html.parser').findAll("div", {"class": "well"})[1].next['href']
                except Exception:
                    originalWriteup = "#"

                try:
                    task = datas[cnt+1].next['href'] + "|" + datas[cnt+1].next.text.encode('ascii', 'replace')
                except Exception:
                    task = "-"

                try:
                    tags = datas[cnt + 2].next.next.text
                except Exception:
                    tags = "-"

                try:
                    event = datas[cnt].next['href'] + "|" + datas[cnt].next.text.encode('ascii', 'replace')
                except Exception:
                    event = "-"

                try:
                    author = datas[cnt + 3].next['href'] + "|" + datas[cnt + 3].next.text.encode('ascii', 'replace')
                except Exception:
                    author = "-"

                try:
                    writeupUrl = datas[cnt + 4].next['href']
                except:
                    writeupUrl = "-"

                temp.append({
                    "idWriteup": id_writeup,
                    "event": event,
                    "task": task,
                    "tags": tags,
                    "author": author,
                    "writeupUrl": writeupUrl,
                    "originalWriteup": originalWriteup
                })
                cnt += 5

        idx = 0
        for data in temp:
            # Insert writeup ke database
            writeup = Writeups(data)
            db.session.add(writeup)
            db.session.commit()

        x += 1
        # if x == 1:
        #     break

    return render_template('index.html', datas=temp)

@app.route('/')
def index():
    if Writeups.query.all():
        return render_template('index.html', datas=Writeups.query.all())
    else:
        return "<h2>Something broken</h2>"