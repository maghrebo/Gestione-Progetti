from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "e30c06fe8f5342efa8f1ac5d75a2c187"
SPOTIFY_CLIENT_SECRET = "9fa9fec219e4463db4ef5683f5ad588c"
SPOTIFY_REDIRECT_URI = "https://5000-maghrebo-gestioneproget-9kgp8ro5uvc.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui


#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)