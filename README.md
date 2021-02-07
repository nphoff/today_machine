# Today Machine!

Taken from https://github.com/goldsamantha/today_machine

Instead of having a printer, I'm going to send today's report to a remarkable tablet

## Prerequisites 

###(pandoc + LaTeX)

```
sudo apt-get install pandoc
sudo apt-get install texlive texlive-base
```

### Remarkable auth

There is some setup that you have to do with your remarkable to register this API use as a "device": 
http://rmapi.subutux.be/quickstart.html#registering-the-api-client

Once you do this once, every subsequent call will grab a new token and everything should work out fine.

## Run

```
python3 -m venv env
source env/bin/activate
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

## TODOS:

- [x] Remove code for controlling printer
- [x] Write markdown file to a temp file
- [x] Figure out how to write a pdf from the markdown
  - options are mdpdf (on pypi), and some version of pandoc + latex
  - pandoc + latex is more flexible, mdpdf is easier
  - pandoc + latex is also a pretty well troden path
  - markdown -> pdf should be:
  - `pandoc manual.txt --pdf-engine=xelatex -o manual.pdf`
- [x] Figure out how to send things to remarkable
  - [x] Figure out how to use the rmapy
- [ ] Get quotes from other projects and add them to the daily thing
- [ ] Grab forecast data
- [ ] Add car search to the data
