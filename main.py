from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encriptaciones")
def entrar():
    return render_template("encriptaciones.html")

@app.route("/encriptar", methods=["GET", "POST"])
def encriptarMensaje():
    mensaje = request.form.get("txtMensaje")
    
    #Definimos un diccionario de mapeo para encriptar las letras
    mapa_encriptacion = {'a': 'ϝ', 'á': 'Ϝ', 'b': 'ᶋ', 'c': 'ׁׁׁׁ۝', 'd': 'ȓ', 'e': 'ấ', 'é': 'Ӕ', 'f': 'ꬱ',
                         'g': 'ᾗ', 'h': 'סּ', 'i': '₽', 'í': 'ᴪ', 'j': 'ѩ', 'k': 'ꭊ', 'l': 'ꭌ', 'm': 'ᵾ',
                         'n': 'ᶑ', 'o': 'ά', 'ó': '£', 'p': 'µ', 'q': 'ɨ', 'r': 'ḓ', 's': 'ꜽ', 't': 'ד',
                         'u': 'ỡ', 'ú': '┼', 'v': '∩', 'w': '₷', 'x': '♫', 'y': 'ḝ', 'z': 'Ꟃ'}

    mensaje_encriptado = ''
    for letra in mensaje:
        #Remplazamos la letra con el valor de encriptación
        mensaje_encriptado += mapa_encriptacion.get(letra.lower(), letra)
    
    return mensaje_encriptado

@app.route("/desencriptar", methods=["GET", "POST"])
def desencriptarMensaje():
    mensaje = request.form.get("txtMensajeEncriptado")
    
    #Definimos un diccionario de mapeo para desencriptar las letras
    mapa_desencriptacion = {'ϝ': 'a', 'Ϝ': 'á', 'ᶋ': 'b', '۝': 'c', 'ȓ': 'd', 'ấ': 'e', 'Ӕ': 'é', 'ꬱ': 'f',
                            'ᾗ': 'g', 'סּ': 'h', '₽': 'i', 'ᴪ': 'í', 'ѩ': 'j', 'ꭊ': 'k', 'ꭌ': 'l', 'ᵾ': 'm',
                            'ᾗ': 'g', 'סּ': 'h', '₽': 'i', 'ᴪ': 'í', 'ѩ': 'j', 'ꭊ': 'k', 'ꭌ': 'l', 'ᵾ': 'm',
                            'ᶑ': 'n', 'ά': 'o', '£': 'ó','µ': 'p', 'ɨ': 'q', 'ḓ': 'r', 'ꜽ': 's', 'ד': 't',
                            'ỡ': 'u', '┼': 'ú', '∩': 'v', '₷': 'w', '♫': 'x', 'ḝ': 'y', 'Ꟃ': 'z'}

    mensaje_desencriptado = ''
    for letra in mensaje:
        # Si la letra está en el diccionario, reemplaza con el valor desencriptado, de lo contrario, deja la letra como está
        mensaje_desencriptado += mapa_desencriptacion.get(letra.lower(), letra)

    return mensaje_desencriptado

if __name__=="__main__":
    app.run(debug=True)
    