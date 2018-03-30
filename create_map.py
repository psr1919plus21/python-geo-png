import json
import datetime

import folium
import pandas as pd
from helpers import save_as_png
from helpers import create_marker
from helpers import scale_array_with_range


start_time = str(datetime.datetime.now().time())
map = folium.Map(location=[20,0], tiles="Mapbox Bright", zoom_start=2)

users_geo = json.load(open('users-geo.json'))

cluster_radiuses = []
for user_cluster in users_geo:
    cluster_radiuses.append(int(user_cluster['users']))

scaled_radiuses = scale_array_with_range(cluster_radiuses, 0.2, 30)

i = 0
for user_cluster in users_geo:
    create_marker(user_cluster, map, scaled_radiuses[i], 100)
    i = i + 1

finish_time = str(datetime.datetime.now().time())
print('started at: ' + start_time)
print('finished at: ' + finish_time)

map.save('mymap.html')
save_as_png('mymap.html');
