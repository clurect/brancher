# Brancher

## Introduction

This project started at work when I needed to quickly switch branches in git. I felt that a lot of git UIs didn't offer what I wanted so I created a little tool to do exactly what I needed in one button.

## Configuring

The `branches.txt` file is for optional (advised) configuration. It has two commands right now:
* `>path` enter the absolute path to your project on the same line as the command
* `>branches` will read every line in the file after this command as a branch

## Installing the app

### Setup virtualenv

Info on [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

After cloning:
`cd brancher`
`pip inistall virtualenv`
`virtualenv brancher-env`
`source brancher-env/Scripts/activate`
`python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew`

### Running

`python Brancher.py`
