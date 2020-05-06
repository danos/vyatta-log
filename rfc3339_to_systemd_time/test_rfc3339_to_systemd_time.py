#!/usr/bin/env python3

# Copyright (c) 2020, AT&T Intellectual Property.
# SPDX-License-Identifier: LGPL-2.1-only

from .rfc3339_to_systemd_time import rfc3339_to_systemd_time


def test_rfc3339_to_systemd_time():
    assert rfc3339_to_systemd_time(
        "2019-12-25T04:57:58.050-07:00") == "2019-12-25 11:57:58.050000 UTC"


def test_z_tz():
    assert rfc3339_to_systemd_time(
        "2019-12-25T04:57:58Z") == "2019-12-25 04:57:58.000000 UTC"
