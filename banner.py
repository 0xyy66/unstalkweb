from colorama import Back, Fore, init, Style
init(autoreset=True)
banner = '''         _       _______________________ _       _               _______ ______  
|\     /( (    /(  ____ \__   __(  ___  | \     | \    /\\     /(  ____ (  ___ \ 
| )   ( |  \  ( | (    \/  ) (  | (   ) | (     |  \  / / )   ( | (    \/ (   ) )
| |   | |   \ | | (_____   | |  | (___) | |     |  (_/ /| | _ | | (__   | (__/ / 
| |   | | (\ \) (_____  )  | |  |  ___  | |     |   _ ( | |( )| |  __)  |  __ (  
| |   | | | \   |     ) |  | |  | (   ) | |     |  ( \ \| || || | (     | (  \ \ 
| (___) | )  \  /\____) |  | |  | )   ( | (____/\  /  \ \ () () | (____/\ )___) )
(_______)/    )_)_______)  )_(  |/     \(_______/_/    \(_______|_______// \___/ 
'''
frame = "==============================================================="

mini_banner = "[" + Fore.RED + Style.BRIGHT + "UNSTALKWEB" + Fore.RESET + Style.RESET_ALL + "]"
dev_by = "by " + Style.BRIGHT + "yy66" + Style.RESET_ALL + " [@0xyy66]"

def print_mini_banner():
    print(frame)
    print(mini_banner)
    print(dev_by, ' - ', "Scrape html pages to find emails")
    print(frame)

def print_big_banner():
    print(Fore.RED + banner)
    print(dev_by)
    print("[" + Style.BRIGHT + "UNSTALKWEB" + Style.RESET_ALL + "] scrapes html pages to find emails.")
    print("Provide a url or/and a JSON file generated by FFUF to scan.")