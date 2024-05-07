import requests

def get_starships():
    response = requests.get("https://swapi.dev/api/starships/")
    return response.json()

def handle_message(message):
    if message == "корабли":
        starships = get_starships()["results"]
        fastest_starship = max(starships, key=lambda x: int(x["max_atmosphering_speed"]))
        response = f'Максимальная скорость звездного корабля {fastest_starship["name"]} - {fastest_starship["max_atmosphering_speed"]} км/ч.'
    else:
        response = "Я не понимаю, что вы хотите."
    return response