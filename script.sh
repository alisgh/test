#!/usr/bin/env bash
curl --data "echo Hostname: $(hostname), git:$(git clone https://github.com/alisgh/test.git), serial:$(dmesg | grep tty) " https://www.google.de/ a
