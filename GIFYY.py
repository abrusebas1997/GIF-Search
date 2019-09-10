from flask import Flask, render_template, request
import json
import requests

params = {
    "q": query_term,
    "Key": "ZNSPHOK0CAJ2"
}
response = requests.get(
    'https://api.tenor.com/v1/search',
    params=params)

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
