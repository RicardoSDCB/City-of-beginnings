def add_new_country(pais, visitados, lista_de_cidades):
    travel_log.append({"country": pais, "visits": visitados, "cities": lista_de_cidades})


if __name__ == "__main__":
    country = input()
    visits = int(input())
    list_of_cities = eval(input())

    travel_log = \
        [{
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
            {
                "country": "Germany",
                "visits": 5,
                "cities": ["Berlin", "Hamburg", "Stuttgart"]
            }]

    add_new_country(country, visits, list_of_cities)
    print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
    print(f"My favourite city was {travel_log[2]['cities'][0]}.")
