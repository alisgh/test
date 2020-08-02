#!/usr/bin/env bash
curl --data "Hostname: $(hostname), git:$(COMMIT_VERSION), serial:$(PISERIAL), "
