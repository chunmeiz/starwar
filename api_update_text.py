import requests
from pprint import pprint

#base = 'https://swapi.dev/api/'
base = 'https://swapi.py4e.com/api/'

def json_from_request(base, endpoint, path='', query=''):
    url = f'{base}{endpoint}{path}{query}'
    response = requests.get(url)
    data = response.json().get('results')
    # pprint(data) # in reality it is a string formatted in specific way
    return data


def json_from_url(url):
    response = requests.get(url)
    data = response.json()
    return data




film_title = []
films = []
def get_all_films():
    endpoint = 'films/'

    url = f'{base}{endpoint}'
    films = json_from_url(url).get('results')
    for film in films:
        film_title.append(film.get('title'))
    for i in range(1, len(film_title) + 1):
        print(f'{i}: {film_title[i - 1]}')

charNameList = []
charLinks = []
characters =[]
def get_all_characters(nums):
    endpoint = 'films/'
    url = f'{base}{endpoint}'
    films = json_from_url(url).get('results')
    charLinks = films[nums - 1].get('characters')
    for link in charLinks :
        character = json_from_url(link)
        charNameList.append(character.get('name'))
        characters.append(character)
    for i in range(1, len(charNameList) + 1):
        print(f'{i}: {charNameList[i - 1]}')
    return characters,charNameList

def get_character_properties(choice, characters):
     char = characters[choice-1]

     print('Your height is: ')
     height = char.get('height')
     print(f'{height} cm')

     print('Your mass is: ')
     mass = char.get('mass')
     print(f'{mass} kg')

     print('Your birth_year is: ')
     birth_year = char.get('birth_year')
     print(f'{birth_year}')

     print('Your homeworld is: ')
     homeworld_url = char.get('homeworld')
     homeworld = json_from_url(homeworld_url)
     homeworld_name = homeworld.get('name')
     print(f'{homeworld_name}')

     print('Your species is: ')
     species_url = char.get('species')
     species = json_from_url(species_url[0])
     species_name = species.get('name')
     print(f'{species_name}')
     print('Your language is: ')
     species_language = species.get('language')
     print(f'{species_language}')

starshipNameList =[]
starships =[]
def get_all_starship(choice, characters):
    char = characters[choice-1]
    starship_urls = char.get('starships')
    for link in starship_urls :
        starship = json_from_url(link)
        starshipNameList.append(starship.get('name'))
        starships.append(starship)

    if len(starshipNameList) == 0:
        print ('Sorry, you have no starship.You can start your galaxy trip with a pilot.')
    else:
        print(f'You have {len(starshipNameList)} starships.')
        for i in range(1, len(starshipNameList) + 1):
          print(f'{i}: {starshipNameList[i - 1]}')
        shipNum = int(input('Which starship would you like to take?(Choose from the above numbers) :'))
        print(f'You can drive the {starshipNameList[shipNum-1]} to start your first galaxy trip...')

def get_all_starships():
    endpoint = 'starships/'
    ship_info = json_from_request(base, endpoint)
    print('All the ships with a hyperdrive rating above 3 are: ')
    for ship in ship_info:
        hyperdrive_rating = float(ship.get('hyperdrive_rating'))

        if hyperdrive_rating > 3:
            print(ship.get('name'))
    print('')
    print('All the ships with cargo capacity above 300000 are: ')

    for ship in ship_info:
        cargo_capacity = float(ship.get('cargo_capacity'))
        if cargo_capacity > 300000:
            print(ship.get('name'))
    print('')
    print('All ships with consumables above 5 months are: ')

    for ship in ship_info:
        duration_consumables = ship.get('consumables').split()
        # print(duration_consumables[1])
        if duration_consumables[1] == 'months':
            int_duration = int(duration_consumables[0])
        if duration_consumables[1] == 'year':
            int_duration = int(duration_consumables[0]) * 12
        # print(int_duration)
        if int_duration > 5:
            print(ship.get('name'))
    print('')
    print('All ships with passengers 0 are: ')
    for ship in ship_info:
        passengers = ship.get('passengers')
        if passengers == str(0):
            print(ship.get('name'))
    print('')







print('Welcome to the Star Wars virtual environment.We have the following films:')
get_all_films()
nums = int(input('Which movie would you like to be a part of? (Choose from the above numbers): '))
title = film_title[nums - 1]

print(title)
print('')
print('All characters: ')
characters,charNameList = get_all_characters(nums)
choice = int(input('Which character would you like to be? (Choose from the above numbers) '))

print(f'Hello {charNameList[choice-1]}.')
ans = input('Do you want to get your basic information?(Y/N)')
if ans == 'Y' or ans == 'y':
   get_character_properties(choice, characters)

ans = input('Do you want to know all starship?(Y/N)')
if ans == 'Y' or ans == 'y':
   get_all_starships()
ans = input('Do you want to know how many starship do you have?(Y/N)')
if ans == 'Y' or ans == 'y':
   get_all_starship(choice, characters)
  
