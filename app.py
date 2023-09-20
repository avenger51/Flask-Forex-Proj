from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#the API won't error!
#valid_currency_codes = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]
#Can't remove the previous result!!  Refresh 'resubmits the form'
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.after_request
def disable_caching(response):
    return add_no_cache_headers(response)

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    result = ""
    if request.method == 'POST':
        # Get user input from the form
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = float(request.form['amount'])
        #float(request.form['amount'])
      
        #"USD":{"description":"United States Dollar","code":"USD"
        symbol_url = "https://api.exchangerate.host/symbols"
        response = requests.get(symbol_url)
        if response.status_code == 200:
    # do the JSON stuff
         data = response.json()

    #Set symbols and create a dict
        symbols = data.get("symbols", {})
       

       #checking if valid currency to proceed
        if from_currency not in symbols or to_currency not in symbols:
            result = "Error: Invalid currency code entered"
        else:
                api_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    data = response.json()
                    if 'result' in data:
                        converted_amount = data['result']
                        result = f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"


        return render_template('currency_converter.html', result=result)

    return render_template('currency_converter.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)


#WORKING CODE:
#
#valid_currency_codes = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]
#
#@app.route('/', methods=['GET', 'POST'])
#def currency_converter():
#    if request.method == 'POST':
#        # Get user input from the form
#        from_currency = request.form['from_currency']
#        to_currency = request.form['to_currency']
#        amount = float(request.form['amount'])
#        
#      if from_currency not in valid_currency_codes or to_currency not in valid_currency_codes:
#            result = "Error: Invalid currency code entered"
#        else:
#            try:
#                amount = float(amount)
#                api_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
#                response = requests.get(api_url)
#
#                if response.status_code == 200:
#                    data = response.json()
#                    if 'result' in data:
#                        converted_amount = data['result']
#                        result = f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
#                    else:
#                        result = "Error: Conversion data not found in the response"
#                else:
#                    result = "Error: Unable to fetch exchange rates"
#            except ValueError:
#                result = "Error: Invalid amount entered. Please enter a valid number."
#
#        return render_template('currency_converter.html', result=result)
#
#    return render_template('currency_converter.html')
#
#
#if __name__ == '__main__':
#    app.run(debug=True)
