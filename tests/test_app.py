from app import app
def test_home_route():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert res.json == {"message": "Hello, World!"}

def test_health_check():
    client = app.test_client()
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json == {"status": "ok"}

def test_echo():
    client = app.test_client()
    name = "ChatGPT"
    res = client.get(f'/echo/{name}')
    assert res.status_code == 200
    assert res.json == {"message": f"Hello, {name}!"}

def test_404_error():
    client = app.test_client()
    res = client.get('/does-not-exist')
    assert res.status_code == 404
