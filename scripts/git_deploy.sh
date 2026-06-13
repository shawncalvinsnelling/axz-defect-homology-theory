#!/usr/bin/env bash
set -euo pipefail

git init
git branch -M main
git add .
git commit -m "release: AXZ Defect Homology Theory Ultimate Release"

echo "Now add your remote:"
echo "git remote add origin https://github.com/shawncalvinsnelling/axz-defect-homology-theory.git"
echo "git push -u origin main"
echo "git tag -a ultimate -m 'AXZ Defect Homology Theory — Ultimate Release'"
echo "git push origin ultimate"
