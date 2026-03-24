import requests
from urllib.parse import urljoin
api_base = "http://10.161.186.197:8000"

def post_login_api(email: str, password: str) -> str:
    resp = requests.post(
        urljoin(api_base, "login"),
    json = {"email": email, "password": password},
    )
    resp.raise_for_status()

    return resp.json()["token"]

def get_seed_list_names_api(token: str) -> list[str]:
    resp = requests.get(
        urljoin(api_base, "seed_list_names"),
        headers={"Authorization": f"Bearer {token}"},
    )
    resp.raise_for_status()
    return resp.json()["data"]

if  __name__== "__main__":
    token = post_login_api(email="catsonmars@hotmail.com", password="spacexlaunchfailure")
    print(token)
    print(get_seed_list_names_api(token))