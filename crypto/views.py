from django.shortcuts import render

# free api key
api_key = 'fcbcd6c636020c3e0654c3853fb39dd85c3c83c1194bf757ee55d76e882cf0a4'

# Create your views here.
def home(request):
    import requests
    import json

    # grab crypto prices
    price_request = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BNB,XRP,DOGE,MATIC,ADA,BUSD,CHZ,LTC&tsyms=USD&api_key={api_key}')
    price = json.loads(price_request.content)

    # grab the cyrpto news from api
    news_request = requests.get(f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}')
    news = json.loads(news_request.content)

    return render(request, 'home.html', {"news": news, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json

        # grab the quote from the base.html
        quote = request.POST['quote']

        # grabs the specified crypto from api
        crypto_request = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD&api_key={api_key}')
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, 'prices.html', {'notfound': notfound})


def top_crypto(request):
    import requests
    import json

    # grab top 10
    coin_request = requests.get(f'https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10&tsym=USD&api_key={api_key}')
    top_coin = json.loads(coin_request.content)

    return render(request, 'top_crypto.html', {'top_coin': top_coin, 'range': range(10)})