from geopy.geocoders import ArcGIS
import folium
import folium.plugins

from yelpapi import YelpAPI
yelp_api = YelpAPI("Yelp-Api-Key")

import requests
api_key = "Cuttly-Api-Key"

#Main Feature Group Addition Function

def geoDataRetrieval(addresses, restLat, restLon, restNames, restURLS, restImg, restPrice, fg, fg1, fg2, fg3, fg4, col):
    i = 0
    for add in addresses:
        location = nom.geocode(add)
        restLat.append(location.latitude)
        restLon.append(location.longitude)
    for lt, ln, n, add, lnk, pic, p in zip(restLat, restLon, restNames, addresses, restURLS, restImg, restPrice):
        iframe = folium.IFrame(html=html %  (n, add, lnk, lnk, pic), width=200, height=200)
        if p == "$":
            fg1.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=col)))
        elif p =="$$":
            fg2.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=col)))
        elif p =="$$$":
            fg3.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=col)))
        elif p =="$$$$":
            fg4.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=col)))

    map.add_child(fg)
    map.add_child(fg1)
    map.add_child(fg2)
    map.add_child(fg3)
    map.add_child(fg4)

#Cuttly API Call to Shorten URL for more aesthetic tooltip information
def shortenUrl(url):
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        shortened_url = data["shortLink"]
    else:
        print("[!] Error Shortening URL:", data)
    return shortened_url

#Parse Yelp API json information, first checking for valid key's to avoid errors [ie missing "price" data]
def parseYelpJSON(restaurants, names, addresses, urls, imgs,prices):
    for restaurant in restaurants:
        if "name" in restaurant.keys():
            names.append(restaurant["name"])
        else:
            names.append("")
        if "url" in restaurant.keys():
            addresses.append(restaurant["location"]["address1"] + ", " + restaurant["location"]["city"] + ", " + restaurant["location"]["state"] + " " + restaurant["location"]["zip_code"])
        else:
            addresses.append("")
        if "url" in restaurant.keys():
            url = (restaurant["url"])
            shortened_url = shortenUrl(url)
            urls.append(shortened_url)
        else:
            urls.append("")
        if "image_url" in restaurant.keys():
            imgs.append(restaurant["image_url"])
        else:
            imgs.append("")
        if "price" in restaurant.keys():
            prices.append(restaurant["price"])
        else:
            prices.append("")


nom = ArcGIS()

#Choice of City
city = "Austin"
state = "TX"

#Map Seed Data Acquisition With Geocode
location = nom.geocode(city + "," + state)
mapSeedLat = location.latitude
mapSeedLon = location.longitude

## Map Initialization ##
map = folium.Map(location=[mapSeedLat, mapSeedLon], tiles = "Stamen Terrain")

#Html Element
html = """
<strong>Name:</strong> <em>%s </em> <br>
<strong>Address:</strong> <em>%s <br>
<strong>Link:</strong><a href= %s target="_blank"> %s</a> <br>
<img src= %s width="100" height="100" display="block" margin-left="auto" margin-right="auto">
"""


#### Sushi ####

sushi_results = yelp_api.search_query(term='sushi', location=city + ", " + state, sort_by='rating', limit=20)
sushiRestaurants = sushi_results["businesses"]

sushiAddresses = []
sushiNames = []
sushiURL = []
sushiLat = []
sushiLon = []
sushiImg = []
sushiPrices = []

parseYelpJSON(sushiRestaurants, sushiNames, sushiAddresses, sushiURL, sushiImg, sushiPrices)

fgs = folium.FeatureGroup(name="Sushi")   
fgs_1 = folium.plugins.FeatureGroupSubGroup(group=fgs, name="Sushi -- $") 
fgs_2 = folium.plugins.FeatureGroupSubGroup(group=fgs, name="Sushi -- $$") 
fgs_3 = folium.plugins.FeatureGroupSubGroup(group=fgs, name="Sushi -- $$$") 
fgs_4 = folium.plugins.FeatureGroupSubGroup(group=fgs, name="Sushi -- $$$$") 

geoDataRetrieval(sushiAddresses, sushiLat, sushiLon, sushiNames, sushiURL, sushiImg, sushiPrices, fgs, fgs_1, fgs_2,fgs_3, fgs_4, "lightblue")

#### Italian ####

fgi = folium.FeatureGroup(name="Italian")   
fgi_1 = folium.plugins.FeatureGroupSubGroup(group=fgi, name="Italian -- $") 
fgi_2 = folium.plugins.FeatureGroupSubGroup(group=fgi, name="Italian -- $$") 
fgi_3 = folium.plugins.FeatureGroupSubGroup(group=fgi, name="Italian -- $$$") 
fgi_4 = folium.plugins.FeatureGroupSubGroup(group=fgi, name="Italian -- $$$$") 

italian_results = yelp_api.search_query(term='italian', location=city + ", " + state, sort_by='rating', limit=20)
italianRestaurants = italian_results["businesses"]

italianAddresses = []
italianNames = []
italianURL = []
italianLat = []
italianLon = []
italianImg = []
italianPrices = []

parseYelpJSON(italianRestaurants, italianNames, italianAddresses, italianURL, italianImg, italianPrices)

geoDataRetrieval(italianAddresses, italianLat, italianLon, italianNames, italianURL, italianImg, italianPrices, fgi, fgi_1, fgi_2,fgi_3, fgi_4, "red")

#### Mexican ####

fgm = folium.FeatureGroup(name="Mexican")   
fgm_1 = folium.plugins.FeatureGroupSubGroup(group=fgm, name="Mexican -- $") 
fgm_2 = folium.plugins.FeatureGroupSubGroup(group=fgm, name="Mexican -- $$") 
fgm_3 = folium.plugins.FeatureGroupSubGroup(group=fgm, name="Mexican -- $$$") 
fgm_4 = folium.plugins.FeatureGroupSubGroup(group=fgm, name="Mexican -- $$$$") 

mexican_results = yelp_api.search_query(term='mexican', location=city + ", " + state, sort_by='rating', limit=20)
mexicanRestaurants = mexican_results["businesses"]

mexicanAddresses = []
mexicanNames = []
mexicanURL = []
mexicanLat = []
mexicanLon = []
mexicanImg = []
mexicanPrices = []

parseYelpJSON(mexicanRestaurants, mexicanNames, mexicanAddresses, mexicanURL, mexicanImg, mexicanPrices)

geoDataRetrieval(mexicanAddresses, mexicanLat, mexicanLon, mexicanNames, mexicanURL, mexicanImg, mexicanPrices, fgm, fgm_1, fgm_2,fgm_3, fgm_4, "green")

fga = folium.FeatureGroup(name="American")   
fga_1 = folium.plugins.FeatureGroupSubGroup(group=fga, name="American -- $") 
fga_2 = folium.plugins.FeatureGroupSubGroup(group=fga, name="American -- $$") 
fga_3 = folium.plugins.FeatureGroupSubGroup(group=fga, name="American -- $$$") 
fga_4 = folium.plugins.FeatureGroupSubGroup(group=fga, name="American -- $$$$") 

american_results = yelp_api.search_query(term='american', location=city + ", " + state, sort_by='rating', limit=20)
americanRestaurants = american_results["businesses"]

americanAddresses = []
americanNames = []
americanURL = []
americanLat = []
americanLon = []
americanImg = []
americanPrices = []

parseYelpJSON(americanRestaurants, americanNames, americanAddresses, americanURL, americanImg, americanPrices)

geoDataRetrieval(americanAddresses, americanLat, americanLon, americanNames, americanURL, americanImg, americanPrices, fga, fga_1, fga_2,fga_3, fga_4, "orange")

map.add_child(folium.LayerControl())
map.save("TopRestaurants.html")


