import re

import requests

from config import get_config
from downloader import download
from helper import clean_filename, get_lines

serie = 'DBZ'
already_downloaded = 6

config = get_config(serie)

episodes_name = get_lines(config['names_file'])
links = get_lines(config['links_file'])


def get_episode_name(idx):
    filename = "{}.{}.{}".format(serie, str(idx+1).zfill(3), episodes_name[idx])
    return clean_filename(filename)


def get_dl_link(request):
    return re.findall(config['url_pattern'], str(request.content))[0]


with requests.Session() as s:
    # Login
    p = s.post(config['login_page'], data=config['payload'])

    def download_episode(link, episode_name):
        dl_page = s.get(link)
        dl_link = get_dl_link(dl_page)
        file_name = '{}/{}.mkv'.format(config['save_dir'], episode_name)
        download(dl_link, file_name, episode_name)

    if len(links) != len(episodes_name):
        raise Exception(
            "The number of names ({}) is not the same than the episodes({})"
            .format(len(links), len(episodes_name))
        )

    for i in range(already_downloaded, len(links)):
        url = links[i]
        name = get_episode_name(i)
        download_episode(url, name)
