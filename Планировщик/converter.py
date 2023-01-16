import requests

def getLink(place):
    response = requests.get(
        f'https://geocode-maps.yandex.ru/1.x/?apikey=34e30fd1-24b4-4592-81ae-e8cbcfc425bf&geocode={place}&format=json&results=1&ll=39.200269,51.660786')
    if response.status_code == 200:
        coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude = float(coords[0:coords.find(' ')])
        latitude = float(coords[coords.find(' ') + 1:len(coords)])
        return f'https://yandex.ru/maps/?pt={longitude},{latitude}&z=19&l=map'
    else:
        return place
