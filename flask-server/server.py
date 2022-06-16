from flask import Flask
import requests

app = Flask(__name__)

# swapi api
url = 'https://swapi.dev/api/people'
response = requests.get(url)


@app.route("/results")
def results():
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
