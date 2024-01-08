#!/bin/bash
# Script to update documentation from a repository
# Usage: ./update-docs.sh <repo-name> <version>

# Parameters
REPO_NAME=$1
VERSION=$2  # 'current' or 'next'

# Execute mkdocs.py script
python .github/scripts/mkdocs.py

# Copy necessary files to docs folder
TARGET_DIR="../docs/$REPO_NAME"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"
cp -pR docs/* "$TARGET_DIR/"
cp -pR README.md "$TARGET_DIR/"

# Check if REPO_NAME is "harmonyui" and execute openapi.py
if [ "$REPO_NAME" == "HarmonyUI" ]; then
    python .github/scripts/openapi.py
fi

# Print updated documentation message
printf "Documentation from %s (%s version) updated.\n" "$REPO_NAME" "$VERSION"
