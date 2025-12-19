@echo off
REM demo for init + add
cd %~dp0
mkdir demo_init_add_test
cd demo_init_add_test
groot init
echo "Demo file" > demo.txt
groot add demo.txt
groot status
