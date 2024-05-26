from flask import Flask, render_template, request
from dotenv import load_dotenv
from converter import CurrencyConverter
import os

class BiddingApp:
    def __init__(self, bid_offer, api_key):
        self.bid_offer = bid_offer
        self.converter = CurrencyConverter(api_key)
        self.kes_rate = self.converter.convert_usd_to_kes(1)

    @property
    def money_earned(self):
        return int(self.bid_offer) * 0.94

    @property
    def money_kes(self):
        return self.money_earned * self.kes_rate

    def get_results(self):
        return {
            'money_earned': f"{self.money_earned:.2f}",
            'money_kes': f"{self.money_kes:.2f}"
        }

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == 'POST':
        bid_offer = request.form['bid_offer']
        api_key = os.getenv('API_KEY') 
        bidding_app = BiddingApp(bid_offer, api_key)
        results = bidding_app.get_results()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
