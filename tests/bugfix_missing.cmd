@echo off
mkdir demo_bugfix
cd demo_bugfix
groot init
echo 1 > t1.txt
groot add t1.txt
del t1.txt
groot commit -m "should warn and skip"
