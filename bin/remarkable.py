import locale
import os
import sys


locale.textdomain('remarkable')

REMARKABLE_ROOT = os.getenv('REMARKABLE_ROOT', os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src')))
sys.path.insert(0, REMARKABLE_ROOT)

os.putenv('XDG_DATA_DIRS', '%s:%s' % ((REMARKABLE_ROOT + '/share'), os.getenv('XDG_DATA_DIRS', '/usr/local/share:/usr/share')))

import Application
Application.run()
