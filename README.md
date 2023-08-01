# Google Scholar Crawler

In this project we will be crawling Google Scholar 
profiles by name or URL and extracting list of publications
and their details.


## Installation

```bash
pip install -r requirements.txt
```

![Alt Text](./images/google-scholar-crawler.gif)

## Usage

```bash
python main.py [-h] (-an AUTHOR_NAME | -u URL) [-o OUTPUT]
```

### Examples
```bash
python main.py -an "John Doe"

python main.py -an "John Doe" -o "output.csv"

python main.py -au "https://scholar.google.com/citations?user=8Za5gQMAAAAJ&hl=en" -o "output.csv"
```
(c) Mohammad Sina Allahkaram 
