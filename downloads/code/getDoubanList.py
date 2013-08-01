#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# auther: jeswang
# finished time: 2012.2.4

import os 
import stat
import urllib2
import urllib
import time,datetime 
import threading
import string
from time import sleep
from BeautifulSoup import *


BOOK_HEAD = '''---
layout: page
title: "Book"
comments: true
sharing: true
footer: false
---

'''

MOVIE_HEAD = '''---
layout: page
title: "Moive"
comments: true
sharing: true
footer: false
---

'''

def getList(base_url, list_kind):
    c=urllib2.urlopen(base_url+list_kind+'?sort=time&start=0&filter=all&mode=grid&tags_sort=count')
    soup = BeautifulSoup(c.read())
    c.close()
    totalNumber =soup.find('span', { "class" : "subject-num"}).contents[0]
    separator = "/"
#    print totalNumber
    totalNumber = totalNumber[totalNumber.find(separator) + 7:]
    totalNumber = string.atoi(totalNumber)
#    print totalNumber

    bookList = soup.findAll('a', { "class" : "nbg"})
#    print bookList
    
    beginNumber = 15
    while totalNumber-15 > 0:
        c = urllib2.urlopen(base_url+list_kind+'?sort=time&start='+str(beginNumber)+'&filter=all&mode=grid&tags_sort=count')
        soup = BeautifulSoup(c.read())
        c.close()
        bookList = bookList + soup.findAll('a', { "class" : "nbg"})
        totalNumber = totalNumber - 15
        beginNumber += 15
    return bookList

        


if __name__ == "__main__":

    book_file = file('../octopress/source/book/index.markdown', 'w')
    book_file.write(BOOK_HEAD)
    print "获取正在读的书籍列表"
    base_url = 'http://book.douban.com/people/dowang/'
    book_file.write('''## 在读的书
''')
    
    for book in getList(base_url, 'do'):
        book_file.write(str(book).replace('spic','mpic')+' ')

    print "读过的书籍列表"
    base_url = 'http://book.douban.com/people/dowang/'
    book_file.write('''
## 读过的书
''')
    
    for book in getList(base_url, 'collect'):
        book_file.write(str(book).replace('spic','mpic')+' ')

    print "想要的书籍列表"
    base_url = 'http://book.douban.com/people/dowang/'
    book_file.write('''
## 想要读的书
''')
    
    for book in getList(base_url, 'wish'):
        book_file.write(str(book).replace('spic','mpic')+' ')

    movie_file = file('../octopress/source/movie/index.markdown', 'w')
    movie_file.write(MOVIE_HEAD)
    
    print "获取正在看的电影列表"
    base_url = 'http://movie.douban.com/people/dowang/'
    movie_file.write('''## 在看的电影
''')
    
    for book in getList(base_url, 'do'):
        movie_file.write(str(book).replace('spic','mpic')+' ')

    print "看过的电影列表"
    movie_file.write('''
## 看过的电影
''')
    
    for book in getList(base_url, 'collect'):
        movie_file.write(str(book).replace('spic','mpic')+' ')

    print "想要的电影列表"
    movie_file.write('''
## 想要看的电影
''')
    
    for book in getList(base_url, 'wish'):
        movie_file.write(str(book).replace('spic','mpic')+' ')

    print "Finish!"
