from flask import Flask, render_template, request
from flask.sessions import NullSession
from helpers import get_weather, get_forecast
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/weather")
def weather():
    country = str(request.args.get("country"))
    city = str(request.args.get("city"))
    if not country or not city:
        return render_template("apology.html", error="No Country Or City Mentioned")
    if not country.isalpha() or not city.isalpha():
        return render_template("apology.html", error="Country Or City In Wrong Format")
    weather = get_weather(country, city)
    forecast = get_forecast(country, city)
    if weather == None or forecast == None:
        return render_template("apology.html", error="Wrong Country Or City entered")
    else:
        dateandtime = weather['dateAndTime']
        dateandtime = dateandtime.split()
        date = dateandtime[0]
        time = dateandtime[1]
        day_name = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')
        day = datetime.strptime(date, '%d-%m-%Y').weekday()
        Day = day_name[day]
        return render_template("weather.html", temperature=weather['temperature'], text=weather['text'], feelslike=weather['feelslike'], country=weather['country'], city=weather['city'], icon=weather['icon'], date=date, day=Day, time=time, forecast=forecast)


if __name__ == '__main__':
    app.run(debug=True)
