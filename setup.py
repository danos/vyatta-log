from setuptools import setup

setup(
    name='rfc3339-to-systemd-time',
    version='0.1',
    description='Convert rfc3339 timestamps to a form journalctl understands',
    author='Vyatta Package Maintainers',
    author_email='DL-vyatta-help@att.com',
    packages=['rfc3339_to_systemd_time'],
    entry_points={
        "console_scripts": [
            'vyatta-journalctl-wrapper-rfc3339-to-systemd-time=rfc3339_to_systemd_time.rfc3339_to_systemd_time:main',
        ],
    },
    install_requires=['iso8601', 'pytz'],
)
