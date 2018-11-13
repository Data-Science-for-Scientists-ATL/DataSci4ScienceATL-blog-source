del /s /q output
pelican content -o output -s pelicanconf.py
ghp-import output
git push -f git@github.com:Data-Science-for-Scientists-ATL/Data-Science-for-Scientists-ATL.github.io gh-pages:master