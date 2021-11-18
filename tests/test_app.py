import app

def test_value_gt_9(client):
    app.random.random =  lambda : 1.0
    response = client.get('/')
    assert response.status_code == 200

def test_value_lt_1(client):
    app.random.random =  lambda : .09
    response = client.get('/')
    assert response.status_code == 200

def test_value_gt_2_lt_5(client):
    app.random.random =  lambda : .3
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'

def test_value_gt_1_lt_2(client):
    app.random.random = lambda : 0.124
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'

def test_value_gt_5_lt_9(client):
    app.random.random = lambda : 0.65
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'

def test_value_eq_1(client):
    app.random.random = lambda : 0.1
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'

def test_value_eq_2(client):
    app.random.random = lambda : 0.2
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'

def test_value_eq_5(client):
    app.random.random =  lambda : 0.5
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'

def test_value_eq_9(client):
    app.random.random = lambda : 0.9
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'