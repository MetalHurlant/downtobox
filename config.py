from credentials import *
from helper import ensure_directory_exists

login_page = "https://uptobox.com/?op=login&referer=homepage"

series = {
    'DBZ': {
        'url_pattern': "http:\/\/www[0-9]+\.uptobox.com\/dl\/[a-zA-Z0-9_-]+\/DBZ.[0-9]+\.VF-VOSTFR\.WwW\.Univers-Anime\.Com\.mkv"
    }
}


def verify_it_exists(file_name):
    open(file_name, 'r')


def get_config(serie):
    config = {
        'login_page': login_page,
        'payload': payload
    }

    if serie not in series:
        raise Exception("This serie ({}) is not supported. The supported ones are:\n{}".format(serie, series.keys()))

    config.update(series[serie])

    links_file = "Data/links/{}.links.txt".format(serie)
    verify_it_exists(links_file)
    config.update({'links_file': links_file})

    names_file = "Data/names/{}.names.txt".format(serie)
    verify_it_exists(names_file)
    config.update({'names_file': names_file})

    save_dir = 'Data/downloads/{}'.format(serie)
    ensure_directory_exists(save_dir)
    config.update({'save_dir': save_dir})

    return config
