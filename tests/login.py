# import requests

# session = requests.Session()
# token = session.get('http://127.0.0.1:8000/auth/').cookies['csrftoken']
# response = session.post('http://127.0.0.1:8000/auth/', {'username': 'app'}, headers={'X-CSRFToken': token})
# print(response.json())


import asyncio
import requests_async as requests

async def initialize() -> tuple[bool, str]:
    __token = None
    __session = requests.Session()

    try:
        response = await __session.get('http://127.0.0.1:8000/auth/')
    except requests.exceptions.ConnectionError:
        return (False, "couldn't connect with the server, ConnectionError")
    
    if response.status_code != 200:
        return (False, "couldn't connect with the server, ServerError")

    __token = response.cookies.get('csrftoken')
    if not __token:
        return (False, "couldn't get the token")

    print('MainModel inicializado')
    return (True, "")


print(asyncio.run(initialize()))