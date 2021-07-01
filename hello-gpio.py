from flask import Flask, render_template
import datetime
from gpiozero import Button
app = Flask(__name__)

button1 = Button(24)
button2 = Button(25)
button3 = Button(26)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'HELLO!',
        'time': timeString
        }
    return render_template('main.html', **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):
    try:
        if pin == '23':
            if button1.is_pressed:
                response = "Pin number 23 is high!"
            else:
                response = "Pin number 23 is low!"
        elif pin == '24':
            if button2.is_pressed:
                response = "Pin number 24 is high!"
            else:
                response = "Pin number 24 is low!"
        elif pin == '25':
            if button3.is_pressed:
                response = "Pin number 25 is high!"
            else:
                response = "Pin number 25 is low!"
    except:
        response = "There was an error reading pin " + pin + "."

    templateData = {
        'title' : 'Status of Pin' + pin,
        'response' : response
        }

    return render_template('pin.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)