import sys
import gettext
from textwrap import dedent
import os

from . import AncapBot, settings
from .db import updatedb

gettext.translation(
    "ancap_bot",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "locale")),
    languages=[settings.LOCALE],
).install()


def main_cli():  # TODO: use argparse and add error handling
    if len(sys.argv) <= 1:
        print(_("type --help for the options"))
    else:
        arg = sys.argv[1]
        if arg == "--help" or arg == "-h":
            print(
                dedent(
                    _(
                        """\
                ancap-bot CLI Options:
                run:
                    run the bot
                updatedb:
                    populate de database with tables
                """
                    )
                )
            )
        elif arg == "run":
            AncapBot()
        elif arg == "updatedb":
            updatedb()
        else:
            print(_("type --help for the options"))


if __name__ == "__main__":
    main_cli()