#!/usr/bin/env python
import os
import sys
import signal


def sighandler(signum, frame):
    print("signal {} received, quitting".format(signum))
    sys.exit(1)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjocker.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
