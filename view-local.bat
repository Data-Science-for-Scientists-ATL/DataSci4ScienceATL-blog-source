del /s /q output
pelican content -o output -s pelicanconf.py
cd output
python -m http.server