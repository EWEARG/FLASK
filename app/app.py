# Esto es una prueba nada mas "

# echo "# FLASK" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/EWEARG/FLASK.git
# git push -u origin main

from flask import Flask, render_template, request, url_for, redirect 

app = Flask ( __name__ )

@app.before_request  
def before_request():
    print("Antes de la Petición...")

@app.after_request
def after_request(response):
    print("Después de la petición...")
    return response

@app.route ( "/" )
def index( ):
    # return "Esta es mi Primera Prueba"
    cursos =["PHP", "SQL", "Power-BI", "Python", "Java", "FLASK"]
    data={
        'titulo':'ENERSA - Legales',
        'encabezado':'Gestión Sector Legales',
        'bienvenida':'¡Saludos !',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)

@app.route ('/contacto/<nombre>/<edad>')
def contacto(nombre, edad):
    data= {
        'titulo':'Contacto',
        'nombre':nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "OK"

def pagina_no_encontrada(error):
    #return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)

