import requests

base_url = "http://127.0.0.1:5000"

print("Fetching All Available Coins from CoinGecko...\n")

# API Link will fetch all coin names
coins_api_url = "https://api.coingecko.com/api/v3/coins/list"

response = requests.get(coins_api_url)

if response.status_code == 200:
    coins_data = response.json()
    available_coins = [coin['id'] for coin in coins_data]

    print(f"Total Available Coins: {len(available_coins)}")

    print("\nHere are Coins for reference:\n")
    for coin in available_coins:
        print("-", coin)
else:
    print("Failed to fetch coins from CoinGecko.")
    exit()

print("\n")

# It will Ask user for input until correct coin name is given
while True:
    user_coin = input("Enter any coin name from all available coins: ").lower()

    if user_coin in available_coins:
        price_response = requests.get(f"{base_url}/crypto?coin={user_coin}")

        if price_response.status_code == 200:
            print("\nPrice Details:\n")
            print(price_response.json())
        else:
            print("Error fetching price from your Flask API.")
        break
    else:
        print("Invalid Coin Name! Please enter again.\n")

print("\nThank you! Demo Completed Successfully ")
