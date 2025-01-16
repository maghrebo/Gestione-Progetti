from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

NASA_API_KEY = "NYYgwAYWHsnwCHsk1UxqlkuCWnjA8aRFUrYEu8sW" #api key personale del sito della nasa





# Rourte /nasa per immagine NASA
@app.route('/nasa')
def nasa_home():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    # richiedo i dati
    data = response.json() #converte da json a dict python
    return render_template('nasa.html', title=data.get("title"), description=data.get("explanation"), image_url=data.get("url"))

if __name__ == '__main__':
    app.run(debug=True)