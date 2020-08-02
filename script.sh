#!/usr/bin/env bash
curl --data "echo Hostname: $(hostname), git:$(git pull origin master), serial:$(dmesg | grep tty) " https://www.google.de/ 
