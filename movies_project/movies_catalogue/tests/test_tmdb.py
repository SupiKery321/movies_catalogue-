import tmdb_client, pytest
from unittest.mock import Mock
from app import app


def test_get_poster_url_uses_default_size():
       # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def test_get_movies_list(monkeypatch):
       # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
  mock_single_movie = ["Movie 1"]
  requests_mock = Mock()
  response = requests_mock.return_value
  response.json.return_value = mock_single_movie
  monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

  single_movie = tmdb_client.get_single_movie(movie_id = 1)
  assert single_movie == mock_single_movie
 
def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = "https://api.themoviedb.org/3/movie/1/credits"
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json()["cast"] = response.json.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie_cast = tmdb_client.get_single_movie_cast(movie_id = 1)
    assert movie_cast == mock_single_movie_cast

def test_get_poster_url(monkeypatch):
    mock_poster_url = "https://image.tmdb.org/t/p/w342/https://image.tmdb.org/t/p/w780//bZnOioDq1ldaxKfUoj3DenHU7mp.jpg"
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_poster_url
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    get_poster_url = tmdb_client.get_poster_url(poster_api_path = "https://image.tmdb.org/t/p/w780//bZnOioDq1ldaxKfUoj3DenHU7mp.jpg", size="w342")
    assert get_poster_url == mock_poster_url





@pytest.mark.parametrize('list_type',[
    ('popular'), 
    ('now_playing'),
    ('upcoming'), 
    ('top_rated')])
def test_homepage(list_type):
   api_mock = Mock(return_value={'list_type': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')
       
   