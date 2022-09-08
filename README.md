# [UNSTALKWEB]

Scrape html pages to find emails.

## Single page scrape

``` bash
./unstalkweb.py -u https://sitetopwn.com/contacts
```

## More pages from FFUF scan

The script works well with JSON output files obatained from a [FFUF](https://github.com/ffuf/ffuf) scan.

### Generate a JSON with FFUF

``` bash
ffuf -w wordlist.txt -u https://sitetopwn.com/FUZZ -o ffuf.json
```

Ouput

``` text
===============================================================
[UNSTALKWEB]
by yy66 [@0xyy66]  -  Scrape html pages to find emails
===============================================================
[x] Scraping http://sitetopwn.com/contacts
2 email(s) found
=============================================================== 

Url scraped: http://sitetopwn.com/contacts
Emails found: 2

goldie@sitetopwn.com
bob@sitetopwn.com
```

By default the output format is JSON, if not add -of json to the command.

### Scrape all the pages found with FUFF

```
./unstalkweb.py -f ffuf.json
```

Output

``` text
===============================================================
[UNSTALKWEB]
by yy66 [@0xyy66]  -  Scrape html pages to find emails
===============================================================
[x] File: ffuf.json
===============================================================

[x] Scraping http://sitetopwn.com/about
0 email(s) found
[x] Scraping http://sitetopwn.com/contacts
2 email(s) found
[x] Scraping http://sitetopwn.com/home
1 email(s) found
[x] Scraping http://sitetopwn.com/tour
0 email(s) found
===============================================================

Email(s) found at http://sitetopwn.com/about
Email(s) found at http://sitetopwn.com/contacts
Email(s) found: 3

info@sitetopwn.com
goldie@sitetopwn.com
bob@sitetopwn.com
```