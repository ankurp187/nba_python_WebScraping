import requests
from bs4 import BeautifulSoup


real_names = []
players ={}

def scrap():
    global real_names
    global players
    res = requests.get('http://www.nba.com/players')
    soup = BeautifulSoup(res.text,'lxml')

    content = soup.select('#block-league-content')

    names = soup.select('#block-league-content section section a')
    real_names=[]
    for name in names:
        real_names.append(name.get('title'))

    names = soup.select('#block-league-content section section a')
    real_names=[]
    for name in names:
        real_names.append(name.get('title'))

    details = soup.select('#block-league-content section section span')

    links = soup.select('#block-league-content section section a')
    players_link=[]
    for name in names:
        players_link.append(name.get('href'))

    for i in range(len(players_link)):
        players_link[i]='http://www.nba.com'+players_link[i]

    teams1 = []
    for i in range(int(len(players_link)/2)):
        teams1.append(players_link[2*i+1])

    for i in range(len(teams1)):
        teams1[i] = teams1[i].split(" ")

    for i in range(len(teams1)):
        teams1[i][0] = teams1[i][0].split("teams/")

    for i in range(len(teams1)):
        teams1[i][0] = teams1[i][0][1]

    for i in range(len(teams1)):
        teams1[i][0] = teams1[i][0].split("/")

    for i in range(len(teams1)):
        teams1[i] = teams1[i][0][0]

    image_link = soup.select('#block-league-content section section img')

    images = []
    for i in range(len(image_link)):
        images.append(image_link[i].get('src'))

    players = {}
    for i in range(int(len(real_names)/2)):
        players[real_names[2*i]] = {'item_no.':details[3*i].getText(),'position':details[3*i+1].getText(),'physique':details[3*i+2].getText(),'profile':players_link[2*i],'team':teams1[i],'team_logo':images[2*i+1],}



if __name__ == '__main__':
    scrap()
    print("Do you want to check names(1) or search for details(2) press 0 for exit")
    a = int(input('Enter your choice'))
    while(a>0):
        if(a==1):
            print(real_names)
        elif(a==2):
            s=input('Enter the name of player ')
            print(players[s])
        a = int(input('Enter your choice again'))





