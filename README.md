# RSS2Ebook
A Python script that converts articles from an  RSS feed into a single Ebook (ePub, PDF, docx - pandoc powered). 
The original motivation for this project was to create an ePub containing 
[Paul Graham's Essays](http://paulgraham.com/articles.html).
This approach was then generalised to include any RSS source (but the default configuration still targets Paul Graham's 
work).

The script is (highly) dependant on some excellent Python libraries, including 
[FeedParser](https://github.com/kurtmckee/feedparser), [Goose3](https://github.com/goose3/goose3) 
and [Pandoc](https://pandoc.org/).
*FeedParser* does the heavy lifting with the RSS side of things, providing an easy to use interface for extracting the
URL and Title of the linked articles.
The URL is then fed into *Goose*, which extracts the primary article content of the linked page and returns 'clean' text.


## Installation and Running

1. Optional, but recommended - Virualenv setup:
```bash
pip install virtualenv
cd RSS2Ebook
virtualenv --python=/usr/bin/python3.6 --no-site-packages RSS2Ebook
source RSS2Ebook/bin/activate
``` 

2. Install required packages
```bash
pip install -r /path/to/requirements.txt
```
Also, your system needs to have [Pandoc](https://pandoc.org/) installed. If you're on a Mac, use the following 
instructions:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install pandoc
pandoc --version
```

If you are on another platform, or have issues with installing pandoc, please follow the official [installation 
instructions](https://pandoc.org/installing.html) provided by this excellent project

3. Set the appropriate variables in the python script, specifically:

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

5. Check your ebook. It will be generated in the location specfied by 
the `EBOOK_NAME` variable, in the python script.
