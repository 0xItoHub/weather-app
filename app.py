from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                api_key = os.getenv("OPENWEATHER_API_KEY")
                if not api_key:
                    error = "APIキーが設定されていません。"
                    return render_template(
                        "index.html", weather_data=weather_data, error=error
                    )

                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja"
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:
                    weather_data = {
                        "city": data["name"],
                        "temperature": round(data["main"]["temp"]),
                        "description": data["weather"][0]["description"],
                        "humidity": data["main"]["humidity"],
                        "wind_speed": data["wind"]["speed"],
                    }
                else:
                    error = "都市が見つかりませんでした。"
            except Exception as e:
                error = f"エラーが発生しました: {str(e)}"

    return render_template("index.html", weather_data=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
