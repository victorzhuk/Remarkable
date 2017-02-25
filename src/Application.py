import optparse
from locale import gettext as _

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from remarkable import get_version, set_up_logging, main


def parse_options():
    parser = optparse.OptionParser(version="%%prog %s" % '1.0')
    parser = optparse.OptionParser(version="%%prog %s" % get_version())
    parser.add_option(
        "-v", "--verbose", action="count", dest="verbose",
        help=_("Show debug messages (-vv debugs remarkable_lib also)"))
    (options, args) = parser.parse_args()
    set_up_logging(options)


def run():
    main()
