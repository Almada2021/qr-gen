#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
echo "installing requiremnts"
pip3 install -r requirements.txt

echo "ready"
# Convert static asset files
python3 manage.py collectstatic --no-input

echo "migrations"
# Apply any outstanding database migrations
python3 manage.py migrate