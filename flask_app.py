from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def inicio():
    paquetes = [
{"nombre": "Cartagena", "descripcion": "Playas y cultura caribeña"},
{"nombre": "Medellín", "descripcion": "Montañas y tecnología"}
]
    return render_template("index.html", paquetes=paquetes)
