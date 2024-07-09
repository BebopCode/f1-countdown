#!/bin/bash
python mycountdown/manage.py runserver 0.0.0.0:8000 &
python mycountdown/manage.py upcoming_race &
python mycountdown/manage.py scrap_leaderboard