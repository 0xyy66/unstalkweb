#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
import requests as req
import re
from colorama import init, Fore, Back, Style
import argparse
import sys
import json
import banner

#colorama configuration
init(autoreset=True)

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url',
					nargs=1,
                    required=False,
                    action='store', 
					help="url to scrape")

parser.add_argument('-f', '--ffuf',
                    nargs=1,
                    required=False,
                    action='store',
                    help="JSON file generated by FFUF")

parser.add_argument('-v', '--verbose',
                    required=False,
                    action='store_true',
                    help='verbose ouput (only with FFUF files [-f, --ffuf])')

args = parser.parse_args()

def no_args():
    banner.print_big_banner()
    sys.exit(0)

if len(sys.argv) < 2:
    no_args()

# parses json and passes every target to scrape()
def ffuf_scrape(f):
    try:
        fopen = open(f, 'r')
    except FileNotFoundError:
        print(Fore.RED + "ERROR: File {} not found".format(f))
        sys.exit(0)
    except PermissionError:
        print(Fore.RED + "ERROR: Don't have permission to read {}".format(f))
        sys.exit(0)

    json_file = fopen.read()
    try:
        ffuf =  json.loads(json_file)
    except json.decoder.JSONDecodeError:
        print(Fore.RED + "ERROR: File format not valid, it may be corrupted")
        sys.exit(0)

    results = []
    print("[x] File: " + Style.BRIGHT + f)
    print(banner.frame, '\n')
    for target in ffuf['results']:
        result = scrape(target['url'])
        results.append(result)
    return results

# gets html, extracts text and passes it to search_email()  
def scrape(url):
    print("[x] Scraping " + Fore.RED + url)
    try:
        html = req.get(url)
    except req.exceptions.ConnectionError as e:
        print(Fore.RED + "ERROR: Can't connect to {}".format(url))
        print(e)
        sys.exit(0)
    soup = bs(html.content, 'html.parser')
    email = search_email(soup.get_text())
    print(Fore.CYAN + "{} email(s) found".format(len(email)))
    result = {'url': url, 'email': email}
    return result

# regex metch to find emails
def search_email(text):
    email =  re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return email

# single result
def print_result(result):
    print(banner.frame, '\n')
    print('[x] Url scraped: ' + Style.BRIGHT + result['url'])
    if len(result['email']) > 0:
        print('Email(s) found: ')
        for e in result['email']:
            print(Fore.GREEN + e)
    else:
        print(Fore.RED + 'No emails found')

# verbose multiple results
def verbose_print_results(results):
    print(banner.frame, '\n')
    print('[x] Verbose')
    found = 0
    for result in results:
        print('\n[x] Url scraped: ' + Style.BRIGHT + result['url'])
        if len(result['email']) > 0:
            print('Email(s) found: ')
            for e in result['email']:
                print(Fore.GREEN + e)
                found += 1
        else:
            print(Fore.RED + 'No emails found')
    #print all the emails
    print()
    if found > 0:
        print('[x] Email(s) list:')
        for r in results:
            for e in r['email']:
                print(Fore.GREEN + e)

# multiple results
def print_results(results):
    print(banner.frame, '\n')
    found = 0
    for r in results:
        if len(r['email']) > 0:
            print('Email(s) found at ' + Style.BRIGHT + r['url'])
            found += 1
    print('Email(s) found: ' + Fore.CYAN + str(found))
    for r in results:
        for e in r['email']:
            print(Fore.GREEN + e)


if __name__ == '__main__':
    banner.print_mini_banner()
    if args.url and args.ffuf:
        single_result = scrape(args.url[0])
        print_result(single_result)
        results = ffuf_scrape(args.ffuf[0])
        if args.verbose:
            verbose_print_results(results)
        else:
            print_results(results)
    elif args.url:
        result = scrape(args.url[0])
        print_result(result)
    elif args.ffuf:
        results = ffuf_scrape(args.ffuf[0])
        if args.verbose:
            verbose_print_results(results)
        else:
            print_results(results)
    else:
        no_args()