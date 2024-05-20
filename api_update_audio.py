import requests
from pprint import pprint
import pyttsx3

def text_to_speech(text):
    # Initialize the Text-to-Speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)   # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()

#base = 'https://swapi.dev/api/'
base = 'https://swapi.py4e.com/api/'


def json_from_request(base, endpoint, path='', query=''):
    request = f'{base}{endpoint}{path}{query}'
    #print(request)
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

def json_from_request_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

film_titles = []

def get_all_films():
    endpoint = 'films/'
    films = json_from_request(base, endpoint).get('results')

    for film in films:
        film_titles.append(film.get('title'))
    for i in range(1, len(film_titles) + 1):
        print(f'{i}: {film_titles[i - 1]}')
        text_to_speech(f'{i}: {film_titles[i - 1]}')

char_list = []
def get_all_characters_from_onefilm():
    endpoint = 'films/'
    path = film_num
    char_urls = json_from_request(base, endpoint,path).get('characters')
    
    i=1
    for char_url in char_urls:
        char_name = json_from_request_url(char_url).get('name')
       # char_list.append(char_name)
       # print(f'{i}: {char_list[i - 1]}')
        print(f'{i}: {char_name}')
        text_to_speech(f'{i}: {char_name}')
        i+=1
    return char_urls

def get_char_info(url):
    char = json_from_request_url(url)
    print(f'Your name is {char.get('name')}.')
    print(f'Your height is {char.get('height')} meters.')
    print(f'Your mass is {char.get('mass')} kilograms.')
    print(f'Your skin color is {char.get('skin_color')}.')
    text_to_speech(f'Your name is {char.get('name')}.')
    text_to_speech(f'Your height is {char.get('height')} meters.')
    text_to_speech(f'Your mass is {char.get('mass')} kilograms.')
    text_to_speech(f'Your skin color is {char.get('skin_color')}.')

print('Welcome to the Star Wars virtual environment. Which movie would you like to be a part of?')
text_to_speech('Welcome to the Star Wars virtual environment     Which movie would you like to be a part of?')
get_all_films()
film_num = int(input('Which movie would you like to be a part of? (Choose from the above numbers) '))
film = film_titles[film_num - 1]
print(f'Let us come into "{film}" .Here is the list of characters.Which character would you like to be?')
text_to_speech(f'Let us come into "{film}".Here is the list of characters.Which character would you like to be?')
char_urls = get_all_characters_from_onefilm()
char_num = int(input('Which character would you like to be? (Choose from the above numbers) '))
get_char_info(char_urls[char_num-1])