# Esto es una prueba nada mas "

# echo "# FLASK" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/EWEARG/FLASK.git
# git push -u origin main

from flask import Flask, render_template, request, url_for, redirect 
from flask_sqlalchemy import SQLAlchemy as sal
from sqlalchemy import create_engine

import pandas as pd

#Python ODBC 
import pyodbc

# OPEN 
#establish database connection
Driver='ODBC Driver 17 for SQL Server'
Server='SURUBI037'
Database='CAPEX'
Trusted_Connection='yes'
Database_Con = f'mssql+pyodbc://@{Server}/{Database}?driver={Driver}'
xxx = "mssql+pyodbc://SURUBI037/CAPEX?driver=SQL Server?Trusted_Connection=yes"

engine = sal.create_engine(xxx)

#engine=sal.create_engine(Database_Con)
conn = engine.connect()

try:
    
    
    #pyodbc.connect('Driver={SQL Server};'
    #                  'Server=SURUBI037;'
    #                  'Database=CAPEX;'
    #                  'Trusted_Connection=yes;')
    #                  # cursor  
    #cursor = conn.cursor()
    #cursor.execute("SELECT [Oblea],[DireccionIP],[ModeloID], [Procesar] FROM xrx_impresoras")
    #records = cursor.fetchall() 
    print('EXITO - Conectado a la BD SQL SERVER') 
    data = pd.read_sql_query("""
    SELECT [ID_Indicador] ,[NOM_Indicador] ,[TIPO_Indicador] ,[SIRVE_PARA] ,[PROCESO] ,[FORMULA] ,[UNIDADES]
      ,[META] ,[TENDENCIA_ESPERADA] ,[FRECUENCIA_MEDICION] ,[FUENTE_INFORMACION] ,[RESPONSABLE] ,[ACTUALIZADO_DATE]
      ,[ACTUALIZADO_POR] ,[LOG_SQL] FROM [CAPEX].[dbo].[SGI_Indicadores]
    """, conn)    

except:
    print('Error al tratar de conectarse - Se utiliza archivo local')
    #os.chdir('C:/Users/eettlin.ENERGIAER/Downloads')
    #os.getcwd()
    #filename = 'Impresoras.csv'
    #data = pd.read_csv(filename, sep=';', header=0)
  

print('Matriz Orignal' , data.shape)
print (data.head(10))

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
        'titulo':'ENERSA - CMI',
        'encabezado':'Gestión de Indicadores',
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


