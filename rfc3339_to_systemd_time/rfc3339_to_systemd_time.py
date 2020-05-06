#!/usr/bin/env python3

# Copyright (c) 2020, AT&T Intellectual Property.
# SPDX-License-Identifier: LGPL-2.1-only

import argparse
import iso8601
import itertools
import os
import pytz
from typing import List, Tuple


def rfc3339_to_systemd_time(rfc3339_time: str) -> str:
    """Convert a rfc3339 timstamp into systemd.time timstamp"""
    _date_obj = iso8601.parse_date(rfc3339_time)
    _date_utc = _date_obj.astimezone(pytz.utc)
    _date_utc_zformat = _date_utc.strftime('%Y-%m-%d %H:%M:%S.%f UTC')
    return _date_utc_zformat


def arg_to_system_time_arg(arg: Tuple[str, str]) -> List[str]:
    arg_name, arg_value = arg
    return ["--" + arg_name, rfc3339_to_systemd_time(arg_value)]


def main():
    """
    A wrapper around journalctl that allows rfc3339 timestamps to be passed
    to the --since and --until options. All other options are passed unmodifed.

    Redundant when https://github.com/systemd/systemd/issues/5194 is fixed
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--since', default=argparse.SUPPRESS)
    parser.add_argument('--until', default=argparse.SUPPRESS)
    args, unknown = parser.parse_known_args()

    # print(unknown)
    # print(vars(args))

    rfc3339_args: List[str] = list(itertools.chain.from_iterable(
        map(arg_to_system_time_arg, vars(args).items())))

    # print(['/usr/bin/journalctl'] + unknown + rfc3339_args)

    os.execv('/usr/bin/journalctl',
             ['/usr/bin/journalctl'] + rfc3339_args + unknown)


if __name__ == "__main__":
    main()
