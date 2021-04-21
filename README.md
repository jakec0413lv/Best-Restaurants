# Best-Restaurants

# Introduction
This WebApp is an interactive map that provides the top restaurants of various types based on a selected city, by utilizing the Yelp API. The restaurants are displayed using Folium within Python. Choices can be narrowed down by type, price, or both utilizing folium.LayerControl(). All geodata is acquired via the use of geopy

# Technologies

+ Python
+ HTML

# Requires

+ Yelp Api Key
+ Cuttly Api Key

#Modules Required

from geopy.geocoders import ArcGIS
import folium
import folium.plugins

from yelpapi import YelpAPI

import requests

# Credit

Usage of yelpapi by gfairchild

https://github.com/gfairchild/yelpapi


