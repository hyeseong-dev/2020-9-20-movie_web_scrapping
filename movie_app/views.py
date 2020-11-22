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
    # 검색란에서 찾고자 하는 키워드를 검색 버튼으로 누른 이후의 로직 담당
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


def moviepage(request):
# 메인 화면에서 'Watch Movie'버튼 클릭시 보여질 화면의 로직 담당
    text = request.GET.get('submit')
    r = requests.get(text)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find_all('div', class_='singcont')
    title = title[0].contents[1].text
    title = title[:-20]
    print(title)
    link = soup.find_all('iframe')
    all_link=[]
    for a in link:
        all_link.append(a['src'])

    all_dict = {'all_dict':all_link, 'title':title}
    return render(request, 'moviepage.html', all_dict)
