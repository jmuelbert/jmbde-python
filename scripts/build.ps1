Remove-Item -Recurse -Force ../dist/*
git submodule init
git submodule update --remote

pyinstaller --clean --distpath ../dist/files -y main.spec

Set-Location ../dist
