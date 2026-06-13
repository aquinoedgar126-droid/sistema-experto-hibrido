from flask import Flask, render_template, request

app = Flask(__name__)

def diagnosticar(sintomas):
    if "no_enciende" in sintomas or "no_hay_luces" in sintomas or "no_giran_ventiladores" in sintomas:
        resultado = {
            "categoria": "Sin energía",
            "causa": "Fuente de poder, cable de corriente, regulador o tarjeta madre.",
            "recomendacion": "Verificar cable, contacto eléctrico, regulador, fuente ATX y conexiones internas."
        }

    elif "pantalla_negra" in sintomas or "no_da_video" in sintomas or "sin_senal_monitor" in sintomas:
        resultado = {
            "categoria": "Falla de video",
            "causa": "Monitor, cable de video, memoria RAM o tarjeta gráfica.",
            "recomendacion": "Revisar cable HDMI/VGA, probar otro monitor y limpiar la memoria RAM."
        }

    elif "pitidos" in sintomas or "reinicios_aleatorios" in sintomas or "pantalla_azul" in sintomas:
        resultado = {
            "categoria": "Problema de RAM",
            "causa": "Memoria RAM mal colocada, dañada o incompatible.",
            "recomendacion": "Retirar la RAM, limpiar contactos, cambiar de ranura o probar otro módulo."
        }

    elif "no_detecta_disco" in sintomas or "arranque_lento" in sintomas or "sistema_no_encontrado" in sintomas:
        resultado = {
            "categoria": "Problema de almacenamiento",
            "causa": "Disco duro/SSD, cable SATA, alimentación o configuración BIOS.",
            "recomendacion": "Revisar cables, entrar al BIOS y probar el disco en otro equipo."
        }

    elif "sobrecalentamiento" in sintomas or "se_apaga_sola" in sintomas or "ventilador_ruidoso" in sintomas:
        resultado = {
            "categoria": "Sobrecalentamiento",
            "causa": "Ventilador sucio, pasta térmica seca o acumulación de polvo.",
            "recomendacion": "Limpiar ventiladores, cambiar pasta térmica y revisar flujo de aire."
        }

    else:
        resultado = {
            "categoria": "Desconocida",
            "causa": "No identificada",
            "recomendacion": "Selecciona más síntomas para mejorar el diagnóstico."
        }

    return resultado


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        sintomas = request.form.getlist("sintomas")
        resultado = diagnosticar(sintomas)
        resultado["sintomas"] = sintomas

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)