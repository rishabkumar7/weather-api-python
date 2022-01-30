from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json

# import os to handle env variables
import os

# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name kingston
        city = 'Kingston'

    # your API key will come here
    api = os.environ.get("API_KEY")

    # source contain json data from api
    source = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api).read()

    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "cityname": str(list_of_data['name']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
        + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
