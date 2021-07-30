import requests
import json
import os
# from time import sleep
from pathlib import Path

api_name = []
api_desc = []
auth_type = []
https_type = []
cors_type = []
api_links = []
categories = []

fnames = []
fdesc = []
fauth = []
fhttps = []
fcors = []
flinks = []

def nl():
    print('\n')

def header(chosen):
    chosen = str(chosen)
    chosen = chosen.upper()
    print(f"""
    ===============================
    ==      Public API Search    ==
    ===============================
              {chosen}          
    -------------------------------
    """)

def categ_choice():
    print(f'''
    ============================================================================
    ==                             Public API Search                          ==
    ==                                 CATEGORIES                             ==
    ============================================================================
    Animals                     Anime               Anti-Malware
    Art & Design                Authentication      Books
    Business                    Calendar            Cloud Storage & File Sharing
    Continuous Integration      Cryptocurrency      Currency Exchange
    Data Validation             Development         Dictionaries
    Documents & Productivity    Environment         Events
    Finance                     Food & Drink        Games & Comics
    Geocoding                   Government          Health
    Jobs                        Machine Learning    Music
    News                        Open Data           Open Source Projects
    Patent                      Personality         Phone
    Photography                 Science & Math      Security
    Shopping                    Social              Sports & Fitness
    Test Data                   Text Analysis       Tracking
    Transportation              URL Shorteners      Vehicle
    Video                       Weather
    -----------------------------------------------------------------------------
    ''')

def clrscrn():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls') 

def search_api(apiext, categ):
    url = f'https://api.publicapis.org/{apiext}?category={categ}'
    res = requests.get(url)
    data = json.dumps(res.json())
    data = json.loads(data)
    count = data['count']
    entries = data['entries']
    for entry in entries:
        name = entry['API']
        desc = entry['Description']
        auth = entry['Auth']
        https = entry['HTTPS']
        cors = entry['Cors']
        link = entry['Link']
        print(f'API: {name}')
        print(f'Description: \"{desc}\"')
        print(f'Auth: [{auth}] HTTPS: [{https}] Cors: [{cors}]')
        print(f'Link: {link} \n')
    print(f'Results Found: {count}')

def update_api_list():
    url = f'https://api.publicapis.org/entries'
    response = requests.get(url)

    data = json.dumps(response.json())
    data = json.loads(data)
    entries = data['entries']
    count = data['count']
    print(f'\nResults Found: {count} \n')

    for entry in entries:
        name = entry['API']
        desc = entry['Description']
        auth = entry['Auth']
        https = entry['HTTPS']
        cors = entry['Cors']
        link = entry['Link']
        api_name.append(name)
        api_desc.append(desc)
        auth_type.append(auth)
        https_type.append(https)
        cors_type.append(cors)
        api_links.append(link)
    print("\nDIRECTORY UPDATED!\n")
    # print(api_name)
    # print(api_desc)
    # print(auth_type)
    # print(https_type)
    # print(cors_type)
    # print(api_links)    
    print(f'Length: {len(api_name)}, {len(api_desc)}, {len(auth_type)}, {len(https_type)}, {len(cors_type)}, {len(api_links)}')

# path = 'E:/Programming/Python_Projects/python_test_codes/apis/res/'
path = Path().absolute()
path = str(path)
path = path + '/res/'
def fileWrite():
    
    f = open(path + 'api_name.txt', 'w', encoding='utf-8')
    for i in api_name:
        f.write(i)
        f.write('\n')
    f.close()

    f = open(path + 'api_desc.txt', 'w', encoding='utf-8')
    for i in api_desc:
        f.write(i)
        f.write('\n')
    f.close()
    
    f = open(path + 'auth_type.txt', 'w', encoding='utf-8')
    for i in auth_type:
        f.write(i)
        f.write('\n')
    f.close()

    f = open(path + 'https_type.txt', 'w', encoding='utf-8')
    for i in https_type:
        types_1 = str(i)
        f.write(types_1)
        f.write('\n')
    f.close()

    f = open(path + 'cors_type.txt', 'w', encoding='utf-8')
    for i in cors_type:
        f.write(i)
        f.write('\n')
    f.close()

    f = open(path + 'api_links.txt', 'w')
    for i in api_links:
        f.write(i)
        f.write('\n')
    f.close()

    f = open(path + 'categories.txt', 'w')
    for i in categories:
        f.write(i)
        f.write('\n')
    f.close()

def fileRead():
    f = open(path + 'api_name.txt', 'r')
    fnames = [line.strip() for line in f]
    print(fnames)
    nl()
    f = open(path + 'api_desc.txt', 'r')
    fdesc = [line.strip() for line in f]
    print(fdesc)
    nl()
    f = open(path + 'auth_type.txt', 'r')
    fauth = [line.strip() for line in f]
    print(fauth)
    nl()
    f = open(path + 'https_type.txt', 'r')
    fhttps = [line.strip() for line in f]
    print(fhttps)
    nl()
    f = open(path + 'cors_type.txt', 'r')
    fcors = [line.strip() for line in f]
    print(fcors)
    nl()
    f = open(path + 'api_links.txt', 'r')
    flinks = [line.strip() for line in f]
    print(flinks)

def load_dir():
    f = open(path + 'api_name.txt', 'r')
    fnames = [line.strip() for line in f]

    f = open(path + 'api_desc.txt', 'r')
    fdesc = [line.strip() for line in f]

    f = open(path + 'auth_type.txt', 'r')
    fauth = [line.strip() for line in f]

    f = open(path + 'https_type.txt', 'r')
    fhttps = [line.strip() for line in f]

    f = open(path + 'cors_type.txt', 'r')
    fcors = [line.strip() for line in f]

    f = open(path + 'api_links.txt', 'r')
    flinks = [line.strip() for line in f]

    return fnames, fdesc, fauth, fhttps, fcors, flinks

def entriesapi(apiext):
    url = f'https://api.publicapis.org/{apiext}'
    response = requests.get(url)

    data = json.dumps(response.json())
    data = json.loads(data)
    entries = data['entries']
    count = data['count']
    print(f'\nResults Found: {count} \n')

    for entry in entries:
        name = entry['API']
        desc = entry['Description']
        auth = entry['Auth']
        https = entry['HTTPS']
        cors = entry['Cors']
        link = entry['Link']
        print(f'API: {name}')
        print(f'Description: \"{desc}\"')
        print(f'Auth: [{auth}] HTTPS: [{https}] Cors: [{cors}]')
        print(f'Link: {link} \n')
    print(f'\nResults Found: {count} \n')

def categ_api(apiext):
    url = f'https://api.publicapis.org/{apiext}'
    response = requests.get(url)

    data = json.dumps(response.json())
    data = json.loads(data)
    for i in data:
        categories.append(i)
        print(i)

def health_api(apiext):
    url = f'https://api.publicapis.org/{apiext}'
    response = requests.get(url)

    data = json.dumps(response.json())
    data = json.loads(data)
    stat = data['alive']
    print(f'Status: {stat}')

again = 'y'

while again == 'y':
    clrscrn()
    print(f'''
    ===============================
    ==      Public API Search    ==
    ===============================
    -    1. All API               -
    -    2. Random                -
    -    3. Categories            -
    -    4. Health                -
    -    5. Update API Dir        -
    -    6. Search by Category    -
    -    7. Check Dir             -
    -------------------------------
    ''')

    choice = input("Choose one: ")
    choice = int(choice)
    print('\n')

    if choice == 1:
        clrscrn()
        header('ALL API')
        entriesapi('entries')
        again = input('Main Menu[y/n]: ')
        again = again.lower()

    elif choice == 2:
        clrscrn()
        header('Random API')
        entriesapi('random')
        again = input('Main Menu[y/n]: ')
        again = again.lower()

    elif choice == 3:
        clrscrn()
        categ_choice()
        again = input('Main Menu[y/n]: ')
        again = again.lower()

    elif choice == 4:
        clrscrn()
        header('API STATUS')
        health_api('health')
        again = input('Main Menu[y/n]: ')
        again = again.lower()

    elif choice == 5:
        clrscrn()
        header('UPDATE API')
        update_api_list()
        fileWrite()
        again = input('Main Menu[y/n]: ')
        again = again.lower()

    elif choice == 6:
        clrscrn()
        header('Search by category')
        search = input("Enter Category:")
        search = str(search)
        search_api('entries', search)
        again = input('Main Menu[y/n]: ')
        again = again.lower()


    elif choice == 7:
        clrscrn()
        header('Check Dir Contents')
        fileRead()
        again = input('Main Menu[y/n]: ')
        again = again.lower()

    else:
        print('Invalid Input')
        again = input('Main Menu[y/n]: ')
        again = again.lower()
