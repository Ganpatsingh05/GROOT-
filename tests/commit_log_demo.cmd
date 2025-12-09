@echo off
mkdir demo_commit_log
cd demo_commit_log
gsc init
echo a > a.txt
echo b > b.txt
gsc add a.txt
gsc add b.txt
gsc commit -m "two files commit"
gsc log
