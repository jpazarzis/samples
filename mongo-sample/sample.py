#!/usr/bin/python
# author: john pazarzis
# Creation Date: Tuesday, July 01 2014

from sentenses import sentenses
from names import names
from random import choice
from pymongo import ASCENDING, DESCENDING

def create_test_data(db):
    new_posts = []
    for name in names:
        post = {"author": name,
                "text": choice(sentenses),
                "tags": choice(sentenses)
                }
        new_posts.append(post)

    posts = db.posts.insert(new_posts)
        
def test_find(posts):
    name = choice(names)
    for post in posts.find({ 'author':  name}):
        p = type("Post", (object,), post)

def show_posts(posts):
    for i, post in enumerate(posts.find()):
        p = type("Post", (object,), post)
        a = p.author
        t = p.text
    print i

def create_index(posts):
    posts.create_index([("author", ASCENDING)])


class Posts(object):
    def __init__(self, collection):
        self.collection = collection

    def find(self, matcher):
        print matcher.to_json()
        name = choice(names)
        for post in self.collection.find({ 'author':  name}):
            p = type("Post", (object,), post)
            yield p

class Matcher(object):

    def to_json(self):
        d = {}
        for key, value in self.__dict__.iteritems():
            d[key] = value
        return d
        
        

if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')


    #for i in range(50):
    #    create_test_data(client.mydb)
    #    print i
    #show_posts(client.mydb.posts)
    #create_index(client.mydb.posts)
    #for i in range(1000):
    #    test_find(client.mydb.posts)

    posts = Posts(client.mydb.posts)

    matcher = Matcher()
    matcher.author = choice(names)

    for post in posts.find(matcher):
        #print post.author
        pass

