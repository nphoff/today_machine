# Today Machine!

Taken from https://github.com/goldsamantha/today_machine

Instead of having a printer, I'm going to send today's report to a remarkable tablet


## Run
```
python3 -m venv env
python3 -m pip install requests
python3 -m pip install todoist-python 
python3 -m pip install pytz

```

## Add your own API token
First copy over the example file to the correct location
```
$ cp lib/example_secrets.py lib/secrets.py
```
Then go ahead and add your own token to the file lib/secrets.py
N.B. This file is automatically .gitignored so it shouldn't get added,
however be extra careful to never share your token in git!

# TODOS:
[ ] Remove code for controlling printer
[ ] Figure out how to send things to remarkable
