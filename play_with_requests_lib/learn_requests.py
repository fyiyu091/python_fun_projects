import requests
import json
from json import JSONDecodeError
from requests import HTTPError

def main():
    get_url = 'https://httpbin.org/get'
    post_url = 'https://httpbin.org/post'
    put_url = 'https://httpbin.org/put'
    delete_url = 'https://httpbin.org/delete'
    # status_err_url = 'https://httpbin.org/status/404'
    try:
        #Get method
        get_data = requests.get(get_url)
        get_data.raise_for_status()
        # print(get_data.json()['args'])
        #Post method
        post_data = requests.post(post_url, data={'sports': ['basketball', 'football']})
        post_data.raise_for_status()
        print('---post_data---')
        print(post_data.json())
        #Put method
        put_data = requests.put(put_url, data={'sports': ['basketball', 'football', 'ping-pang']})
        put_data.raise_for_status()
        print('---put_data---')
        print(put_data.json())
        #Delete method
        delete_data = requests.delete(delete_url)
        delete_data.raise_for_status()
        print('---delete_data---')
        print(delete_data.json())

    except JSONDecodeError as err:
        print(f'json decode error {err}')

    except HTTPError as err:
        print(f'http error {err}')
    

if __name__ == "__main__":
    main()