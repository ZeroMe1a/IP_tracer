import requests

print('\nInput 127.0.0.1 to geolocate yourself!')
ip = input('\nIP to geolocate: ')

if ip == '127.0.0.1':
    ip = 'http://geolocation-db.com/json/'
    geoloc = requests.get(ip).json()

else:
    ip = 'http://geolocation-db.com/json/' + ip
    geoloc = requests.get(ip).json()

print(f"""\nCountry: {geoloc["country_name"]} ({geoloc["country_code"]})
State: {geoloc["state"]}
City: {geoloc["city"]}
Postal: {geoloc["postal"]}
Latitude: {geoloc["latitude"]}
Longitude: {geoloc["longitude"]}""")
    