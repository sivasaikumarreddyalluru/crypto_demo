from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# IT will Fetch all available coins from CoinGecko in real time
@app.route('/coins', methods=['GET'])
def get_all_coins():
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            all_coin_ids = [coin['id'] for coin in data]
            return jsonify({"available_coins": all_coin_ids})
        else:
            return jsonify({"error": "Failed to fetch coin list from CoinGecko"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Wehre we will Get price of selected coin
@app.route('/crypto', methods=['GET'])
def get_crypto_price():
    coin = request.args.get('coin')
    if not coin:
        return jsonify({'error': 'Please provide a coin name.'}), 400

    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,eur,inr'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if coin in data:
            price_data = {
                "coin": coin,
                "price_in_usd": data[coin].get("usd", "N/A"),
                "price_in_eur": data[coin].get("eur", "N/A"),
                "price_in_inr": data[coin].get("inr", "N/A")
            }
            return jsonify(price_data)
        else:
            return jsonify({'error': 'Coin not found or not supported for pricing.'}), 404
    return jsonify({'error': 'Failed to fetch data from CoinGecko'}), 500

if __name__ == '__main__':
    app.run(debug=True)
