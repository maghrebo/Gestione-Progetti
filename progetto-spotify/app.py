from flask import Flask, redirect, request, url_for, render_template,session, Blueprint
import spotipy
from blueprints.auth import auth_bp
from blueprints.home import home_bp

app = Flask(__name__)
app.secret_key = 'ElMaghrebo' #ci serve per identificare la sessione

#collego i blueprint all'app per poter accedere alle loro route
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
