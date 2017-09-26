# Brancher Tool

## Introduction

This project started at work when I needed to quickly switch branches in git. I felt that a lot of git UIs didn't offer what I wanted so I created a little tool to do exactly what I needed in one button.

## Configuring

The `branches.txt` file is for configuration. It has two commands right now
* `>path` enter the absolute path to your project on the same line as the command
* `>branches` will read every line in the file after this command as a branch

## Installing the app

### Setup virtual-env

It's a bit easier to make a python app when using virtual-env.

### Running

`python Brancher.py`
