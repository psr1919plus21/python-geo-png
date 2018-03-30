import os
import time
import datetime

import folium
from selenium import webdriver

def scale_array_with_range(array, range_min, range_max):
    data_min = min(array)
    data_max = max(array)

    scaled_array = []
    for item in array:
        scaled_array.append(fit_range(item, data_min, data_max, range_min, range_max))

    return scaled_array

def fit_range(x, data_min, data_max, range_min, range_max):
    return (range_max - range_min)*((x - data_min)/(data_max - data_min)) + range_min


def create_marker(cluster, map, cluster_radius, threshold):
    """Create circle marker on the map"""
    if(int(cluster['users']) <= threshold):
        return
        
    print('create at ' + str(datetime.datetime.now().time()))
    folium.CircleMarker(
       location = [float(cluster['lat']), float(cluster['lon'])],
       popup = '',
       radius = cluster_radius,
       color = '#f44',
       fill = True,
       fill_color = 'crimson'
    ).add_to(map)


def save_as_png(htmlName):
    """Save as png"""

    tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=htmlName)
    browser = webdriver.Firefox()
    browser.get(tmpurl)
    time.sleep(1)
    browser.save_screenshot('map.png')
    browser.quit()
