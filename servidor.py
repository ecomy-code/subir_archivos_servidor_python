from flask import Flask, request,render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import pathlib
import time

def cargando ():
    print (".")
    time.sleep(.4)
    print ("..")
    time.sleep(1)
    print ("...")
    time.sleep(.4)

miruta = str(pathlib.Path().absolute())
miruta = miruta + '\imagen'

carpeta_guardar = miruta
extenciones_aceptadas = set(["png", "jpg", "jpge","py", "css", "html"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = carpeta_guardar


def allowed_file(filename):

    return "." in filename and filename.rsplit(".", 1)[1].lower() in extenciones_aceptadas


@app.route("/subir", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if not "file" in request.files:
            return "No file part in the form."


        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            cargando()
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))#guardamos foto y redireccionamos 
            #return redirect(url_for("get_file", filename=filename))      abrir archivo despues de guardado
            return "  <h1>Archivo guardado con exito</h1>"
        return "File not allowed."

    return render_template("subir.html")

@app.route("/subir/<filename>")
def get_file(filename):

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(port = 3244,debug=True)

