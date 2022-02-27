from distutils.log import debug
from flask import Flask, render_template, template_rendered

app = Flask(__name__)

@app.get("/")#Decorador
def inicio():
    return render_template("index.html")

@app.get("/Contactos")

def listarContactos():
    return render_template("contactos.html")

@app.get("/Contactos/<int:ContactosId>")
def editarContactos(ContactosId):
    return render_template("editarContactos.html",id = ContactosId)

#/edad/20 Nasiste en el año 2000

@app.get("/edad/<int:edadId>")
def edad(edadId):
    return render_template("edad.html", id = edadId)

app.run(debug=True)


