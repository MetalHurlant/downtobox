# Downtobox
> Download a batch of Uptobox link in a row.

⚠️It is a functional draft.

**Install**

I use python 3.7, if you want to use another, you can change in `tox.py`.

Requirements:
- python
- tox

Copy `credentials.example.py` to `credentials.py` and edit it with your own credentials (I use premium ones).

Edit the parameters at the top of `app.py`

At the root of the project:
```bash
tox -r --notest
```

**Use**

Your file will be called {batch_name}.{index}.{file_name}.mkv

You will need:
- a file where every line is a link to a uptobox file page. 
    - Call this file `Data/links/{batch_name}.links.txt`.
- a file where every line is the name of the episode with the same number than the line. 
    - Call this file `Data/names/{batch_name}.names.txt`.

**Work to do**

- Tests
- Interface
    - It will allow easy way to customize credentials, download_directory, file name, ...
- Restart where download where stopped
- Temporary lost connection robust
