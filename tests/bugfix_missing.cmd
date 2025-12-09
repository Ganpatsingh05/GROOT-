@echo off
mkdir demo_bugfix
cd demo_bugfix
gsc init
echo 1 > t1.txt
gsc add t1.txt
del t1.txt
gsc commit -m "should warn and skip"
