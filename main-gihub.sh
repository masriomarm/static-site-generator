#! /usr/bin/bash
python3 src/main.py "/masriomarm.github.io/"
cd public && python3 -m http.server 8888
