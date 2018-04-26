from goose3 import Goose
import os
import subprocess
import feedparser
# Edit the following according to your preferences.
MAX_RETRIES = 10  # Amount of Network-Error based request retries
WD = os.path.dirname(os.path.realpath(__file__))  # Current working Directory
HTML_DIR = "HTML_Out"  # Storage location for the extracted HTML source
TEMP_FILE = 'temp.txt'  # A temporary storage file for downloaded text
FEED_URL = 'http://www.aaronsw.com/2002/feeds/pgessays.rss'  # The Feed URL - Change this to your desired source
EBOOK_NAME = 'Paul_Graham_Essays.epub'
# Create HTML storage dir
if not os.path.exists(HTML_DIR):
    os.mkdir(HTML_DIR)
d = feedparser.parse(FEED_URL)
# Enumerate through our feed, store the 'clean' article text in our temporary file, before exporting it to HTML
for c, e in enumerate(d.entries):
    url = e.link
    print('Processing - {}'.format(url))
    g = Goose()
    retries = MAX_RETRIES
    while retries > 0:
        try:
            article = g.extract(url=url)
            g.close()
            break
        except Exception as e:
            print('Error establishing connection. Retrying...')
            retries -= 1
    if retries <= 0:
        print('Failed to retreive article ({}). Moving on to next feed item.'.format(url))
        retries = MAX_RETRIES
    with open('temp.txt', 'w') as file:
        file.write(article.cleaned_text)
    of = HTML_DIR + '/s{}-{}.html'.format('{0:05d}'.format(c+1), url.split("/")[-1].split(".")[0])
    subprocess.Popen('pandoc -i temp.txt -t html5 -o {}'.format(of), cwd=WD, shell=True).wait()

    with open(of, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('<h1>{}</h1>'.format(article.title).rstrip('\r\n') + '\n' + content)
# Feed title and Link are required as per the RSS2 spec ... we don't check if there's actually a value
with open(HTML_DIR + '/s00000.html', 'w') as file:
    file.write('<!DOCTYPE html><html><head><meta name="author" content="{}" />'
               '<title>{}</title></head></html>'.format(d.feed.link, d.feed.title))
# Convert the directory of (Ordered HTML file's into a single EPub)
subprocess.Popen('pandoc -s -i {}/*.html -t epub -o {} --toc'.format(HTML_DIR, EBOOK_NAME), cwd=WD, shell=True).wait()
# Cleanup
os.remove('temp.txt')
