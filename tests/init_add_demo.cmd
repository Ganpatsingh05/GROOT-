@echo off
REM demo for init + add
cd %~dp0
mkdir demo_init_add_test
cd demo_init_add_test
gsc init
echo "Demo file" > demo.txt
gsc add demo.txt
gsc status
