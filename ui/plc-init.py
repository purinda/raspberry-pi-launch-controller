#!/usr/bin/env python

from onoffthread import OnOffThread
from guithread import UIThread

if __name__ == '__main__':
    myThread = OnOffThread()
    myThread.start()

    app = UIThread()
    app.start()

