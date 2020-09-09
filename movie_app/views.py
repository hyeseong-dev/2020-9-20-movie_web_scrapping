from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    url = 'https://www.watchmovies7.com.pk/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser') 

    main_movies = soup.find_all('div', class_='postbox')
    sub_movies = soup.find_all('div', class_='boxtitle')

    all_movies = []    
    for movie in sub_movies:
        url = movie.h2.a['href']
        name = movie.h2.a.text
        image = movie.img['src']

        all_movies.append((name, url, image))

    final_dictionary = {'final_dictionary' : all_movies}

    return render(request, 'index.html', final_dictionary)


def new_search(request):
    base_url = 'https://www.watchmovies7.com.pk/?{}{}'
    text = request.GET.get('search')
    final_url = base_url.format('s=', text)  
    r = requests.get(final_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    sub_movies = soup.find_all('div', class_='boxtitle')
    all_movies = []    
    for movie in sub_movies:
        url = movie.h2.a['href']
        name = movie.h2.a.text
        image = movie.img['src']
        all_movies.append((name, url, image))

    final2_dictionary = {'final2_dictionary' : all_movies}

    return render(request, 'new_search.html', final2_dictionary)

