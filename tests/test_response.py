import json


def test_response(app, db, client, prepare_es):
    # response = client.post('/records/', data=json.dumps({"title": "necooo"}), content_type='application/json')
    # print(response)
    # assert response.status_code == 201

    url = "https://localhost:5000/records/jej"
    response = client.get(url)
    print(response.data)
    assert response.status_code == 200
    #
    # url = "https://localhost:5000/records/blah1"
    # response = client.get(url)
    # assert response.status_code == 404

    # url = "https://localhost:5000/records/1/blah"
    # response = client.get(url)
    # assert response.status_code == 401
