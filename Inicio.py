# Esto es una prueba nada mas "

# echo "# FLASK" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/EWEARG/FLASK.git
# git push -u origin main

from flask import Flask
app = Flask ( _name_ )
@app.route ( "/" )
def test ( ):
return "This is a test"
