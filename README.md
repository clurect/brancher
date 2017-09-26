# Brancher

This project started at work when I needed to quickly switch branches in git. I felt that a lot of git UIs didn't offer what I wanted so I created a little tool to do exactly what I needed in one button.

## Configuring

The `config.txt` file is for configuration. It has two commands right now:
* `>path` (required) enter the absolute path to your project on the same line as the command
* `>branches` (optional) will read every line in the file after this command as a branch

## Installing the app

### Setup environment

Info on [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* `pip install virtualenv` (if you don't have it already)

#### Windows setup (using terminal emulator)
After cloning:
* `cd brancher`
* `virtualenv env-bt`
* `source env-bt/Scripts/activate` "(env-bt)" will now be showing above or to the left of you terminal prompt
* `python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew`
* `python -m pip install kivy`

#### Exiting virtualenv

In terminal instance that is in the "env-bt" virtualenv
`deactivate`


More about installing [Kivy](https://kivy.org/docs/installation/installation-windows.html) on Windows

### Running

`python Brancher.py`

The Branch input form is for names of branches e.g. "master", "development". You are able to add buttons to the app using this.

Clicking a button will stash all your current changes in your local repo and switch to the branch matching the name on the button.
