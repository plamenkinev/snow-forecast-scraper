#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

bg_resorts_list_url = 'http://www.snow-forecast.com/resorts/list_by_feature/7?v2'
resort_url = 'http://www.snow-forecast.com/resorts/{}/6day/mid'

result = urlopen(bg_resorts_list_url).read()

parsed_json = json.loads(result.decode("utf-8"))
resorts = parsed_json[0][1]
resorts_info = {}

for resort in resorts:
    url, name = resort
#    print('{} : {}'.format(name, resort_url.format(url)))
    resorts_info[name] = urlopen(resort_url.format(url)).read()

for resort, resort_info in resorts_info.items():
#    print("{} : {}".format(resort, resort_info))
#    print(resort_info)

    soup = BeautifulSoup(resort_info, 'lxml')
    
    days_row = soup.find_all('tr', class_ = 'day-names')[0]
    days = days_row.find_all('td', class_ = 'day-end')

    day_time_zones_row = soup.find_all('tr', class_ = 'hea2')[0]
    day_time_zones = day_time_zones_row.find_all('td', class_ = 'cell')
    
    weather_row = soup.find_all('tr', class_ = 'icons')[0]
    weather_icons = weather_row.find_all('td', class_ = 'iconcell')

    for day in days:
        print(day.string)
        for day_time_zone in range(0, 3):
            print(day_time_zones.pop(0).string)



    
    print('\n' + '=' * 30)
    
    
