from gpiozero import LED
from flask import Flask, render_template, request
app = Flask(__name__)

pins = {
    24 : {'name' : 'coffee maker', 'state': False},
    25 : {'name' : 'lamp', 'state': False}
    }

led24 = LED(24)
led25 = LED(25)
led24.off()
led25.off()

@app.route("/")
def main():
    pins[24]['state'] = led24.is_lit
    pins[25]['state'] = led25.is_lit

    templateData = {
        'pins' : pins
        }
    return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
    changePin = int(changePin)
    deviceName = pins[changePin]['name']
    if action == "on":
        if changePin == 24:
            led24.on()
            pins[24]['state'] = led24.is_lit
        if changePin == 25:
            led25.on()
            pins[25]['state'] = led25.is_lit
        message = "Turned " + deviceName + " on."

    if action == "off":
        if changePin == 24:
            led24.off()
            pins[24]['state'] = led24.is_lit
        if changePin == 25:
            led25.off()
            pins[25]['state'] = led25.is_lit
        message = "Turned " + deviceName + " off."

    if action == "toggle":
        if changePin == 24:
            led24.toggle()
            pins[24]['state'] = led24.is_lit
        if changePin == 25:
            led25.toggle()
            pins[25]['state'] = led25.is_lit
        message = "Toggled " + deviceName + "."


    templateData = {
        'message' : message,
        'pins' : pins
    }

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
