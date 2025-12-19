@echo off
mkdir demo_commit_log
cd demo_commit_log
groot init
echo a > a.txt
echo b > b.txt
groot add a.txt
groot add b.txt
groot commit -m "two files commit"
groot log
