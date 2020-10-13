
import numpy as np
import pandas as pd
import  random
import re





Movies = pd.read_csv("./wiki_movie_plots.csv")
Movies = Movies.dropna()
horror = Movies[Movies['Genre'] == 'horror']
drama = Movies[Movies['Genre'] == 'drama']
action = Movies[Movies['Genre'] == 'action']
comedy = Movies[Movies['Genre'] == 'comedy']
adv = Movies[Movies['Genre'] == 'adventure']

#---function btrg3 esm el movie----
def MovieName(list_of_words):
    if((len(list_of_words))>1):
        word = ' '.join(list_of_words)
        return word
    else:
        word = list_of_words[0]
        return word
print("Search here : ")
message = input()


#--------patterns----------

allpat = 'all (.*)'
horrorpat = 'horror (.*)'
dramapat = 'drama (.*)'
actionpat = 'action (.*)'
comedypat = 'comedy (.*)'
advpat = 'adventure (.*)'

cap = r"[A-Z]\w+"
descpat = 'what is the story (.*)'
castpat = 'actors|cast (.*)'
dicpat = 'director (.*)'
kindtpat = 'origin (.*)'
yeartpat = 'year|release (.*)'
#--matches-----


descmatch = re.search(descpat, message)
castmatch = re.search(castpat, message)
dictmatch = re.search(dicpat, message)
kindmatch = re.search(kindtpat, message)
yearmatch = re.search(yeartpat, message)
match = re.search(allpat, message)
match1 = re.search(horrorpat, message)
match2 = re.search(dramapat, message)
match3 = re.search(actionpat, message)
match4 = re.search(comedypat, message)
match5 = re.search(advpat, message)


if match1:
    print("here is all the horror movies that we recommend to you")
    for lab, row in horror.iterrows():
        print("The Title : " + row['Title'])
        print("The wiki page : " + row['Wiki Page'])

elif match2:
    print("here is all the drama movies that we recommend to you")
    for lab, row in drama.iterrows():
        print("The Title : " + row['Title'])
        print("The wiki page : " + row['Wiki Page'])

elif match3:
    print("here is all the action movies that we recommend to you")
    for lab, row in action.iterrows():
        print("The Title : " + row['Title'])
        print("The wiki page : " + row['Wiki Page'])

elif match4:
    print("here is all the comedy movies that we recommend to you")
    for lab, row in comedy.iterrows():
        print("The Title : " + row['Title'])
        print("The wiki page : " + row['Wiki Page'])

elif match5:
    print("here is all the adventure movies that we recommend to you")
    for lab, row in adv.iterrows():
        print("The Title : " + row['Title'])
        print("The wiki page : " + row['Wiki Page'])

elif descmatch:
    Mname = re.findall(cap, message)
    fname = MovieName(Mname)
    desc = Movies[Movies['Title'] == fname]
    print("The " + fname + " Story : " + desc['Plot'])

elif castmatch:
    Mname = re.findall(cap, message)
    fname = MovieName(Mname)
    desc = Movies[Movies['Title'] == fname]
    print("The " + fname + " Cast : " + desc['Cast'])
    print("and for more information you can check the wikipage : " + desc['Wiki Page'])

elif dictmatch:
    Mname = re.findall(cap, message)
    fname = MovieName(Mname)
    desc = Movies[Movies['Title'] == fname]
    print("The " + fname + " Director is : " + desc['Director'])
    print("and for more information you can check the wikipage : " + desc['Wiki Page'])

elif kindmatch:
    Mname = re.findall(cap, message)
    fname = MovieName(Mname)
    desc = Movies[Movies['Title'] == fname]
    print(fname + " is " + desc['Origin/Ethnicity'])
    print("and for more information you can check the wikipage : " + desc['Wiki Page'])

elif yearmatch:
    Mname = re.findall(cap, message)
    fname = MovieName(Mname)
    desc = Movies[Movies['Title'] == fname]
    print(fname + " released on  " + desc['Release Year'])
    print("and for more information you can check the wikipage : " + desc['Wiki Page'])

elif match:
    print("There's our available movies:D : ")
    print(Movies['Title'])
else :
    print("not found")
    print("but these is our recommendation : Movies['Title']")

















