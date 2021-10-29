from rest_framework.test import APIRequestFactory, APIClient

client = APIClient()
client.login(username='admin', password='admin')

response = client.get('/api')
assert response.status_code == 200

# Obtain a CSRF token.
response = client.get('/api/')
assert response.status_code == 200
csrftoken = response.cookies['csrftoken']

response = client.post('/api/posts/create', json={
    "content": "test"
    }, headers={'X-CSRFToken': csrftoken})
assert response.status_code == 200

response = client.get('/api/test/')
assert response.status_code == 200

response = client.post('/api/test/like')
assert response.status_code == 200

client.logout()