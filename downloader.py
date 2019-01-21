import sys

import requests


def progress_bar(done, nb_block):
    block_size = 100 / nb_block
    done_bar = "=" * round(done/block_size)
    not_done_bar = " " * (nb_block - len(done_bar))
    return f"\r[{done_bar}{not_done_bar}] - {done:.2f}%"


def download(link, file_name, display_name=None):
    if display_name is None:
        display_name = file_name
    with open(file_name, "wb") as f:
        print("Downloading {}".format(display_name))
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=65536):
                dl += len(data)
                f.write(data)
                done = dl / total_length * 100

                sys.stdout.write(progress_bar(done, 20))
                sys.stdout.flush()
            sys.stdout.write("\n")
