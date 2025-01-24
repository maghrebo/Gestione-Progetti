import requests

def persone_nello_spazio():
    """Chiama l'API e restituisce un elenco di persone nello spazio e i loro veicoli."""
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('people', [])
    else:
        return []