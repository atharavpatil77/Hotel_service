import requests
def start_search():
    base_url = "https://api.edamam.com/search"
    app_id = "07ef43a5"  # Replace with your Edamam API application ID
    app_key = "b8d83b2c01efe0d10ad772c0e81afd84		"  # Replace with your Edamam API application key

    ask = input("Enter the meal's Ingredient you are looking for ")

    params = {
        'q': ask,
        'app_id': app_id,
        'app_key': app_key,
    }
    response = requests.get(base_url, params=params)
    print(response.json())

    if response.status_code == 200:
            data = response.json()

            if data.get('hits'):
                recipe = data['hits'][0]['recipe']
                print("\nRecipe for", ask.capitalize() + ":")
                print("Ingredients:")
                for i in recipe['ingredientLines']:
                    print("  ", i)
                print("URL TO GET STEP BY STEP :", recipe['url'])
            else:
                print("No recipe found for", ask.capitalize())
    else:
            print("Error:", response.status_code)

