#!/bin/bash
IFS='|' read file slug w h out <<< "$1"
timeout 90 google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --virtual-time-budget=3000 --window-size=$w,$h --screenshot=/home/claude/web/shots_eu/$out.png "file:///home/claude/voxel/project/$file.dc.html" >/dev/null 2>&1
