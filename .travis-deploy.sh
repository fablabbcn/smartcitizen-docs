#!/bin/sh
set -e

# setup ssh-agent and provide the GitHub deploy key
eval "$(ssh-agent -s)"
#openssl aes-256-cbc -K $encrypted_fb17a912150b_key -iv $encrypted_fb17a912150b_iv -in ed25519.enc -out ed25519 -d
chmod 600 deploy_rsa
ssh-add deploy_rsa

# commit the assets in build/ to the gh-pages branch and push to GitHub using SSH
git remote add gh-token git@github.com:"${TRAVIS_REPO_SLUG}";
git fetch gh-token && git fetch gh-token gh-pages:gh-pages;
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then echo "Pushing to github"; PYTHONPATH=src/ mkdocs gh-deploy -v --clean --remote-name gh-token; git push gh-token gh-pages; fi;

