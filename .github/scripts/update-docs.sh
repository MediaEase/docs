#!/bin/bash
# Script to update documentation from a repository
# Usage: ./update-docs.sh

# Copy necessary files to docs folder
rm -rf docs/{api,harmonyui,mediaease,scripts}
mkdir -p docs/{api,harmonyui,mediaease,scripts}
cp -r MediaEase/docs/* docs/mediaease
cp -r MediaEase/README.md docs/mediaease
cp -r MediaEase/frontend/docs/* docs/harmonyui
cp -r MediaEase/frontend/README.md docs/harmonyui
cp -r MediaEase/scripts/docs* docs/scripts
cp -r MediaEase/scripts/README.md docs/scripts
python .github/scripts/openapi.py
python .github/scripts/mkdocs.py
