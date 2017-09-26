import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
import os
import threading
import logging
import subprocess
root = None
#from kivy.core.window import Window
#Window.clearcolor = (1, 1, 1, 1)
from kivy.config import Config
Config.set('graphics', 'width', '450')
#Config.set('graphics', 'height', '200')

def center_widget(widget, parent):
    widget.pos_hint['x'] -= ( (parent.width/2) + (widget.width/2) )/(parent.width*parent.width)
def callOS(path, name):
    os.chdir(os.path.expanduser(path))
    logging.info(name)
    status = subprocess.check_output(['git','status'], shell=True).decode('utf-8')
    logging.info(status)
    if 'nothing to commit' in status:
        logging.info('nothing to commit, switching branch')
        out = subprocess.check_output(['git','checkout',name], shell=True)
        logging.info(out)
    else:
        os.system('git add .')
        os.system('git stash')
        out = subprocess.check_output(['git','checkout',name], shell=True)
        logging.info(out)
    root.status('done')

class BranchButton(Button):

    def pressed(self):
        #needed to create the button, but code in here does nothing
        #deprecated, figure out how to remove

        root.status('started')
        logging.info('pressed')
        logging.info(self.text)
        t = threading.Thread(target=callOS, name='ls', args=(path,self.text))
        t.daemon = True
        t.start()

class Brancher(FloatLayout):
    cust = StringProperty()
    def on_add(self):
        name = self.ids['branch_name'].text
        logging.info (name)
        print('Path {}'.format(self.getPath().lower()))
        self.add_branch_button(name)

    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        global root
        cmds = []
        brn = False
        try:
            with open('config.txt') as f:
                cmds = [c.strip() for c in f.readlines()]
            for cmd in cmds:
                if '>branches' in cmd:
                    brn = True
                    continue
                elif '>path' in cmd:
                    brn = False
                    self._path = cmd[6:]
                    continue
                if brn:
                    self.add_branch_button(cmd)
        except:
            logging.info('no config.txt file found, carrying on without config')

        root = self


    def getPath(self):
        logging.info('wat')
        return self._path

    def add_branch_button(self, name):
        self.ids['branches'].add_widget(BranchButton(text=name))
    def status(self,status):
        self.ids['status'].text = status

class BrancherApp(App):
    def build(self):
        return Brancher()

if __name__ == "__main__":
    #pass
    BrancherApp().run()
