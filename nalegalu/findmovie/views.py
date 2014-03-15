from django.shortcuts import render
import httplib2
import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
from findmovie.models import MovieEntry
http = httplib2.Http()


# Create your views here.
from django.http import HttpResponse


def populate(request):
    very_links = []
    for i in range(1, 2):
        url = "http://www.ipla.tv/Film/wszystkie/" + str(i)

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())

        divResults = soup.findAll('div', {'class': "universal_page_items_list"})

        lis = divResults[0].findAll('li')

        for li in lis:
            a = li.findAll('a')
            p = li.findAll('p')
            if len(a) > 0 and len(p) > 0:
                very_links.append((u"http://www.ipla.tv" + a[0]['href'],
                                   p[0].find('a').text))

    for t in very_links:
        newMovie = MovieEntry(full_title=t[1], ipla=t[0])

        newMovie.save()

    very_links = []

    for i in range(1, 3):
        url = "http://www.iplex.pl/filmy-iplex-plus/?page=" + str(i)

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())

        divResults = soup.findAll('div', {'class': "movie-details"})

        for li in divResults:
            a = li.findAll('a')
            if len(a) > 0:
                very_links.append((a[0]['href'], a[0].text))

    for t in very_links:
        newMovie = MovieEntry(full_title=t[1], iplex=t[0])

        newMovie.save()

    very_links = []

    for i in range(1, 2):
        url = "http://vod.tvp.pl/filmy-fabularne?sort=title"

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())

        divResults = soup.findAll('strong', {'class': "fullTitle"})

        for li in divResults:
            a = li.findAll('a')
            if len(a) > 0:
                very_links.append((a[0]['href'], a[0].text))

    for t in very_links:
        newMovie = MovieEntry(full_title=t[1],
                              tvp=u"http://vod.tvp.pl/" + t[0])

        newMovie.save()

    very_links = []

    return HttpResponse("Zrobiwszy!")
