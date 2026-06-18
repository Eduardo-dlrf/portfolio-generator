#!/bin/bash

echo "=================="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace

python3 /urs/bin/portfolio.py

git add -A && git commit -m "Update Portfolio"
git push --set-upstream origin main

echo "=================="