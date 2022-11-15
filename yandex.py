import requests

TOKEN = "****************************************"


def creating_directory():
    name_folder = "TEMP_DIR"
    yandex_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    params = {'path': f'{name_folder}', 'overwrite': 'false'}
    requests.put(url=yandex_url, headers=headers, params=params)
    ret = requests.delete(url=yandex_url, headers=headers, params=params)
    return str(ret)


if __name__ == '__main__':
    creating_directory()
