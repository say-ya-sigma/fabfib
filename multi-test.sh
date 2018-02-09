#!/bin/bash

python3 game.py 10 | grep time >> result
python3 game.py 100 | grep time >> result
python3 game.py 1000 | grep time >> result
python3 game.py 10000 | grep time >> result
python3 game-multi.py 10 | grep time >> result
python3 game-multi.py 100 | grep time >> result
python3 game-multi.py 1000 | grep time >> result
python3 game-multi.py 10000 | grep time >> result
