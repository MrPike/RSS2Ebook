# RSS2Ebook
A Python script that converts articles linked to in a RSS feed, extracts the article content and generates a single ebook (ePub, PDF, docx...)

## Installation and Running

1. Virualenv setup 

2. Install required packages
```bash
pip install -r /path/to/requirements.txt
```

3. Set the appropriate variables. The script is setup

```python
# The URL of the RSS feed you would like to parse
FEED_URL = 'http://www.aaronsw.com/2002/feeds/pgessays.rss'
# The name of the resulting ebook. Note - the extension is important,
# and will dictate teh format of the output.
EBOOK_NAME = 'Paul_Graham_Essays.epub'
```
 
4. Run the script:
```bash
python RSS2Ebook.py
```
