import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib.request
import urllib.error


def has_digit(string):
    for char in string:
        if char.isdigit():
            return True
    return False


counter = 0
team_urls = [
    'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1',
    'https://www.transfermarkt.com/primera-division/startseite/wettbewerb/ES1',
    'https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1',
    'https://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1',
    'https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1',
]


def check_internet():
    try:
        header = {"pragma": "no-cache"}
        req = urllib.request.Request("http://www.google.ro", headers=header)
        urllib.request.urlopen(req, timeout=2)
        return True
    except urllib.error.URLError:
        return False


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
}

player_data_list = []
count = 0
isrunning = True
while True:
    conn = check_internet()
    if conn:
        try:
            for t in team_urls:
                r = requests.get(t, headers=header)
                soup = BeautifulSoup(r.content, "html.parser")
                team_elements = soup.find_all("td", class_="hauptlink no-border-links")
                for team_element in team_elements:
                    anchor_tag = team_element.find("a")
                    if anchor_tag:
                        team_link = anchor_tag['href']
                        team_url = f"https://www.transfermarkt.com{team_link}"
                        team_page = requests.get(team_url, headers=header)
                        team_soup = BeautifulSoup(team_page.content, "html.parser")

                        player_elements = team_soup.find_all("span", class_="show-for-small")
                        for player_element in player_elements:
                            anchor_tag = player_element.find("a")
                            if anchor_tag:
                                player_link = anchor_tag['href']
                                player_url = f"https://www.transfermarkt.com{player_link}"
                                player_page = requests.get(player_url, headers=header)
                                player_soup = BeautifulSoup(player_page.content, "html.parser")

                                con = player_soup.select_one(
                                    'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(3)')
                                if con:
                                    con = con.text.strip()
                                else:
                                    con = 'Null'
                                if con == 'Date of birth:':
                                    player_name = anchor_tag['href'].split('/')[1].replace('-', ' ').title()
                                    team_e = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(20) a')
                                    if team_e:
                                        try:
                                            club_id = 'c-' + team_e['href'].split('/')[4]
                                        except:
                                            club_id = ''
                                    player_id = 'p-' + anchor_tag['href'].split('/')[4]
                                    birth = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(4)')
                                    if birth:
                                        birth_date = birth.text.strip()
                                    age__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(8)')
                                    if age__:
                                        try:
                                            age = int(age__.text.strip())
                                        except:
                                            age = player_soup.select_one(
                                                'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(6)')

                                    height__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(10)')
                                    if height__:
                                        height = height__.text.strip()
                                        height = height.split('\xa0')[0]
                                        height = height.replace(',', '')
                                        try:
                                            height = int(height)
                                        except:
                                            height = height
                                    joined__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(22)')
                                    if joined__:
                                        joined = joined__.text.strip()

                                    expires__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(24)')
                                    if expires__:
                                        expires = expires__.text.strip()

                                    position__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(14)')
                                    if position__:
                                        position = position__.text.strip()

                                    foot__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(16)')
                                    if foot__:
                                        foot = foot__.text.strip()

                                    agent__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(18)')
                                    if agent__:
                                        agent = agent__.text.strip()

                                    value = player_soup.select_one(
                                        '#main > main > header > div.data-header__box--small > a')
                                    if value:
                                        value = value.text.split(' ')[0].split('€')[1]
                                        if 'm' in value:
                                            value = value.split('m')[0]
                                            value = float(value) * 1000000
                                            value = int(value)
                                        elif 'k' in value:
                                            value = value.split('k')[0]
                                            value = float(value) * 1000
                                            value = int(value)

                                    n_id = player_soup.select_one(
                                        '#main > main > header > div.data-header__info-box > div > ul:nth-child(3) > li:nth-child(1) > span a')
                                    if n_id:
                                        dig = n_id.text.split()
                                        if has_digit(dig):
                                            national_id = ''
                                        else:
                                            national_id = 'n-' + n_id['href'].split('/')[4]

                                    player_data = {
                                        "Player ID": player_id,
                                        "Player Name": player_name,
                                        "Team ID": club_id,
                                        "Player Birth Date": birth_date,
                                        "Player Age": age,
                                        "Player Height": height,
                                        "Player Joined": joined,
                                        "Player Expires": expires,
                                        "Player Position": position,
                                        "Player Foot": foot,
                                        "Player Agent": agent,
                                        "Player Value": value,
                                        "Player National ID": national_id
                                    }
                                    player_data_list.append(player_data)
                                    count = count + 1
                                    if count == 2500:
                                        break

                                elif con == 'Null':
                                    continue
                                elif con == 'Place of birth:':
                                    player_name = anchor_tag['href'].split('/')[1].replace('-', ' ').title()
                                    team_e = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(20) a')
                                    if team_e:
                                        try:
                                            club_id = 'c-' + team_e['href'].split('/')[4]
                                        except:
                                            club_id = ''
                                    player_id = 'p-' + anchor_tag['href'].split('/')[4]
                                    birth = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(2)')
                                    if birth:
                                        birth_date = birth.text.strip()
                                    age__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(6)')
                                    if age__:
                                        age = int(age__.text.strip())

                                    height__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(10)')
                                    if height__:
                                        height = height__.text.strip()
                                        height = height.split('\xa0')[0]
                                        height = height.replace(',', '')
                                        try:
                                            height = int(height)
                                        except:
                                            height = height

                                    joined__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(20)')
                                    if joined__:
                                        joined = joined__.text.strip()

                                    expires__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(22)')
                                    if expires__:
                                        expires = expires__.text.strip()

                                    position__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(12)')
                                    if position__:
                                        position = position__.text.strip()

                                    foot__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(14)')
                                    if foot__:
                                        foot = foot__.text.strip()

                                    agent__ = player_soup.select_one(
                                        'div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten span:nth-child(16)')
                                    if agent__:
                                        agent = agent__.text.strip()

                                    value = player_soup.select_one(
                                        '#main > main > header > div.data-header__box--small > a')
                                    if value:
                                        value = value.text.split(' ')[0].split('€')[1]
                                        if 'm' in value:
                                            value = value.split('m')[0]
                                            value = float(value) * 1000000
                                            value = int(value)
                                        elif 'k' in value:
                                            value = value.split('k')[0]
                                            value = float(value) * 1000
                                            value = int(value)

                                    n_id = player_soup.select_one(
                                        '#main > main > header > div.data-header__info-box > div > ul:nth-child(3) > li:nth-child(1) > span a')
                                    if n_id:
                                        dig = n_id.text.split()
                                        if has_digit(dig):
                                            national_id = ''
                                        else:
                                            national_id = 'n-' + n_id['href'].split('/')[4]

                                    player_data = {
                                        "Team ID": club_id,
                                        "Player ID": player_id,
                                        "Player Name": player_name,
                                        "Player Birth Date": birth_date,
                                        "Player Age": age,
                                        "Player Height": height,
                                        "Player Joined": joined,
                                        "Player Expires": expires,
                                        "Player Position": position,
                                        "Player Foot": foot,
                                        "Player Agent": agent,
                                        "Player Value": value,
                                        "Player National ID": national_id
                                    }
                                    player_data_list.append(player_data)
                                    count = count + 1
                                    if count == 2500:
                                        break

        except Exception as e:
            # Handle the exception or error
            print("An error occurred:", str(e))
            # Optionally, you can log the error or perform other actions

    else:
        # Code to execute when internet is not available
        time.sleep(30)
        break

df = pd.DataFrame(player_data_list)
df.to_csv('Players.csv',encoding='utf-8-sig',index=False)