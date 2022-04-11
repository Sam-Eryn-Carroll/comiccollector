from django.shortcuts import render
from django.http import HttpResponse

class Comic:
    def __init__(self, title, series, issuenumber, summary, releasedate, publisher):
        self.title = title
        self.series = series
        self.issuenumber = issuenumber
        self.summary = summary
        self.releasedate = releasedate
        self.publisher = publisher

comics = [
    Comic('The Flash', '1st Series', 123,
     'Barry Allen appears at the Community Center in Central City to perform for kids, and during one of his amazing tricks, is mysteriously transported to Keystone City, a place that he recalls that the original Flash once lived; The two meet and Barry surmises that Jay lives on a parallel Earth, one that evidently Earth-1 writer Gardner Fox tuned in on when he wrote the adventures of the Flash in the 1940''s; Jay tells Barry that a crime wave has hit Keystone City and asks Barry for his help.',
     'Sep 1961', 'DC'),
    Comic('Blackest Night', 'N/A', 8,
    'Earth has become the final battleground for life versus death, but how will our heroes fight back against the darkness of sentient space itself? And what does the future hold for Green Lantern, The Flash and the rest of the world''s greatest heroes and villains?',
     'May 2010', 'DC'),
    Comic('Daredevil', '2nd Series', 15,
    'N/A', 'Mar 2001', 'Marvel')
]

def home(request):
    return HttpResponse('<h1>Hello</H1>')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    return render(request, 'comics/index.html', { 'comics': comics})