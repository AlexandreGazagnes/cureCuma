# !/usr/bin/env python3
# coding: utf-8

import sys
import time

from src import create_app
from params import GeneralParams as Params


app = create_app()


def main():
    """main funct"""

    app = create_app()
    app.run(port=Params.port, host="0.0.0.0")


if __name__ == "__main__":
    main()
