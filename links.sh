#!/usr/bin/bash
mkdocs-linkcheck docs -r --exclude assets -v -l> tests/out.log 2>tests/err.log
