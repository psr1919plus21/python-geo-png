# import the library
import os
import time
import json
import datetime

from selenium import webdriver

import folium
import pandas as pd

# Make an empty map
m = folium.Map(location=[20,0], tiles="Mapbox Bright", zoom_start=2)

def create_marker(cluster):
    print('create at ' + str(datetime.datetime.now().time()))
    cluster_radius = int(cluster['users'])
    if (cluster_radius > 20):
        cluster_radius = 20

    folium.CircleMarker(
       location = [float(cluster['lat']), float(cluster['lon'])],
       popup = '',
       radius = cluster_radius,
       color = '#f44',
       fill = True,
       fill_color = 'crimson'
    ).add_to(m)


def save_as_png(htmlName):
    """Save as png"""

    tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=htmlName)
    browser = webdriver.Firefox()
    browser.get(tmpurl)
    time.sleep(2)
    browser.save_screenshot('map.png')
    browser.quit()

start_time = str(datetime.datetime.now().time())

users_geo = json.load(open('users-geo.json'))
for user_cluster in users_geo:
    create_marker(user_cluster)

finish_time = str(datetime.datetime.now().time())
print('started at: ' + start_time)
print('finished at: ' + finish_time)






# Save it as html
m.save('mymap.html')
save_as_png('mymap.html');
