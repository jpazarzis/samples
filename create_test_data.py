#!/usr/bin/python

# author: john pazarzis
# Creation Date: Tuesday, April 01 2014


import random
from numpy.random import normal
import datetime
import matplotlib.pyplot as plt
import networkx as nx

horse_names = ["Abbie", "Abby", "Ace", "Albert", "Alfie", "Alice", "Amber", "angel", "Anna", "Annie",
"Antionette", "Apache", "Apollo", "Apple", "April", "Archie", "Arthur", "Ash", "Asti", "Aston Doulton", "Austin",
"Autumn", "Avon", "Bacardi", "Badger", "Bailey", "Bandit", "Banjo", "Barfields Marco", "Barney", "Barry",
"Basil", "BAZ", "Beanie", "Beano", "Beatrice", "Beau", "Beauty", "Bedwellty Viking", "Beenda", "Bella",
"Belle", "Ben", "Benji", "Bentley", "Bertie", "Bess", "Betty", "Biggles", "Bill", "Billy",
"Billy Boy", "Biscuit", "Black Jack", "Blackie", "Blake", "Blaze", "Blossom", "Blue", "Blue Boy", "Bluebell",
"Bluey", "Bob", "Bobby", "Bonnie", "Bonny", "Boo", "Boris", "Bowe flight", "Boy", "Bracken",
"Bramble", "Brandy", "Breaking and schooling", "Breeze", "Brooke", "Brownie", "Bruce", "Bruno", 
"Bubbles", "Buddy", "Buffy", "Bumble", "Bunny", "Buster", "Buttons", "Candy", "Captain", "Caramel",
"Casino", "Casper", "Cassie", "Catalina", "Cavalier", "Chalkie", "Champ", "Chance", "Charlie", "Charm",
"Chelsea", "Cherokee", "Cherry", "Cherrytop", "Chesney", "Chester", "Chico", "Chloe", "Chucky", "Cilla",
"Cindy", "CJ", "Cleo", "Cloud", "Clover", "Clyde", "Coco", "Cody", "Coedana Eirian", "Colleen",
"Connie", "Connor", "Cookie", "Copper", "Cracker", "Crest", "Crunchie", "Daisy", "Dallas", "Dan",
"Dancer", "Dandy", "Daniel", "Danny", "Danny Boy", "Darcy", "Darkhorse Galatea", "Darkhorse Gucci", "Dee", "Del",
"Devland Snow", "Dexter", "Diamond", "Diego", "Diesel", "Dillon", "Dinky", "Diva", "Dixie", "DJ",
"Dodger", "Dollar", "Dolly", "Domino", "Dora", "Dotty", "Dougal", "Dream", "Drummer", "Dublin",
"Duchess", "Dudley", "Duffy", "Duke", "Duncan", "Dylan", "Ebony", "Echo", "Eclipse", "Eddie",
"Edward", "Ella", "Elle", "Ellie", "Elvis", "Emma", "Eric", "Ernie", "Evie", "Felix",
"Fenna", "Fern", "Fifi", "Fin", "Finley", "Finn", "Fiona", "Flame", "Flash", "Flea",
"Flicka", "Flicker", "Flo", "Flower", "Flynn", "Foxy", "Foxy Lady", "Frankie", "Fred", "Freddie",
"Freddy", "Frenchie", "Freya", "Fudge", "Gem", "Gemma", "George", "Georgie", "Ginger", "Gizmo",
"Goldie", "Grace", "Gracie", "Guiness", "Guinness", "Gypsy", "Harley", "Harry", "Harvey", "Hattie",
"Heather", "Hector", "Heidi", "Henry", "Herbie", "Hero", "Hollie", "Holly", "Honey", "Hugo",
"Indi", "Indie", "Indy", "Izzy", "Jack", "Jacko", "Jackson", "Jacob", "Jaffa", "Jake",
"Jasmine", "Jasper", "Jay", "Jazz", "Jen", "Jenny", "Jerry", "Jess", "Jessie", "Jester",
"Jet", "Jigsaw", "Jim", "Jimmy", "JJ", "Jo", "Joe", "Joey", "Johnny", "Jumbo",
"Junior", "Kai", "Katie", "Kerry", "Kilmurray Tom", "Kizzie", "Kizzy", "Lacks Ren", "Lad", "Lady",
"Lady Tara", "Lemon", "Leo", "Lexi", "Libby", "Lilly", "Lily", "Logan", "Lola", "Lottie",
"Louis", "Lucky", "Lucy", "Lulu", "Luna", "Mac", "Maddie", "Maddy", "Maggie", "Magic",
"Maisie", "Maisy", "Major", "Mallan", "Marley", "Mary", "Mattie", "Maverick", "Max", "May",
"Meg", "Megan", "Melody", "Merlin", "Mia", "Mickey", "Midnight", "Millie", "Milly", "Milo",
"Minnie", "Minstrel", "Minty", "Missy", "Misty", "Mojo", "Molly", "Monty", "Moon", "Morgan",
"Mouse", "Mr Darcy", "Murphy", "Nancy", "Nellie", "Nelly", "Nemo", "Nutmeg", "Oliver", "Ollie",
"Orion", "Oscar", "Ozzie", "Ozzy", "Paddy", "Paris", "Patch", "Patrick", "pebbles", "Peggy",
"Pen", "Penny", "Pepper", "Pepsi", "Percy", "Peter", "Phoebe", "Phoenix", "Pip", "Piper",
"Pippa", "Pixie", "Polly", "Polo", "Pop", "poppet", "Poppy", "Pride", "Prince", "Princess",
"Puzzle", "Queenie", "Ralph", "Rambo", "Red", "Reggie", "Riley", "Rio", "Robbie", "Robin",
"Rocco", "Rocky", "Rodney", "Roger", "Rolo", "Romeo", "Ronnie", "Roo", "Rooney", "Rose",
"Rosie", "Roxy", "Roy", "royal", "Ruby", "Ruby Tuesday", "Rufus", "Rupert", "Rusty", "Ryan",
"Sally", "Sam", "Sammy", "Samson", "Sandy", "Sapphire", "Sasha", "Savannah", "Scarlet", "Scooby",
"Seamus", "Selection", "Seren", "Shadow", "Shannon", "Sherry", "Sid", "sienna", "Silver", "Simba",
"Sky", "Skye", "Smartie", "Smokey", "Smudge", "Snip", "Snoopy", "Snowball", "Snowy", "Socks",
"Solly", "Solo", "sonic", "Sonny", "Sooty", "Sophie", "Sox", "Sparky", "spice", "Spike",
"spirit", "Splash", "Spot", "Spring", "Stan", "Stanley", "Star", "Stella", "Storm", "Sugar",
"Summer", "Sunny", "Suzi", "Suzie", "Syd", "Tammy", "Tango", "Tara", "Taz", "Ted",
"Teddy", "Tess", "Theo", "Thomas", "Thunder", "Tia", "Tigger", "Tilly", "Timmy", "Tinker",
"Tinkerbell", "Tiny", "Toby", "Toffee", "tom", "Tommy", "Tonto", "Topaz", "Treacle", "Troy",
"Tucker", "Twiggy", "Tyson", "Vinnie", "Warrior", "Whisper", "Will", "William", "Willow", "Winnie",
"Winston", "Wispa", "Wizard", "Wombat", "Woody", "Zara", "Ziggy", "Zizou", "Zorro"]

BEST_TIMING = 68.0
WORST_TIMING = 73.0
MIN_STDEV = 1.0
MAX_STDEV = 2.5
MIN_TRACK_VARIANT = 1.0
MAX_TRACK_VARIANT = 5.0


class Horse:
    def __init__(self, name):
        self.name = name
        self.mean = random.uniform(BEST_TIMING, WORST_TIMING)
        self.stdev = random.uniform(MIN_STDEV, MAX_STDEV)
        self.final_time = 0.0

    def run(self,track_variant):
        self.final_time = normal(self.mean,self.stdev) + track_variant

    def __str__(self):
        return '{0},{1:2.2f}'.format(self.name, self.final_time)

def run_a_race(division, track_variant, field_size = 2):
    horses = random.sample(division, field_size)
    map( lambda h: h.run(track_variant) ,horses)
    horses.sort(key = lambda h: h.final_time)
    return horses
    

def make_devisions():
    random.shuffle(horse_names)
    horses = [Horse(name) for name in horse_names]
    horses.sort(key = lambda h : h.mean)
    divisions = [horses[x:x+60] for x in xrange(0, len(horses), 60)]
    del divisions[-1]
    return divisions
 
            
def simulate_meeting(divisions, date, number_of_days=1000):
    starters = {}
    days = []    
    for i in range(number_of_days): 
        date += datetime.timedelta(days=1)
        track_variant = random.uniform(MIN_TRACK_VARIANT, MAX_TRACK_VARIANT)
        for division in divisions:
            for horse in run_a_race(division,track_variant):
                if horse.name not in starters:
                    starters[horse.name] = []
                day = date.strftime("%Y-%m-%d")
                starters[horse.name].append( (day, horse.final_time) )
                if day not in days:
                    days.append(day)
    return starters,days


if __name__ == "__main__":
    divisions = make_devisions()
    starters,days = simulate_meeting(divisions, datetime.datetime(2010,1,1),30)

    graph = nx.Graph()
    day_map = {}
    for i, d in enumerate(days):
        index = i + 1
        graph.add_node(index,date = d)    
        day_map[d] = index
        
    edges = {}
    for s in starters:
        previous_day, previous_time = None, None
        for day, final_time in starters[s]:
            if previous_day is not None:
                edge_key = (day_map[previous_day], day_map[day])
                if edge_key not in edges:
                    edges [edge_key] = []
                edges [edge_key].append(previous_time - final_time)    
            previous_day, previous_time = day, final_time

    for edge in edges:
        weight =  sum(edges[edge])/ len(edges[edge])
        graph.add_edge(edge[0],edge[1], weight = weight)
                
    G = graph        

    elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
    esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

    pos=nx.spring_layout(G) # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=700)

    # edges
    nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=1)

    nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=1,alpha=0.5,edge_color='b',style='dashed')

    # labels
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

    plt.axis('off')
    plt.savefig("variant.png") # save as png
    plt.show() # display

