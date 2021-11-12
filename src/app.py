from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
@app.route("/index")
def  home ():
    return render_template ("home.html")

@app.route ("/curiosidades")
def  curiosidades ():
    return render_template ("curiosidades.html")

@app.route ("/curriculum")
def  curriculum ():
    return render_template ("curriculum.html")


@app.route ("/projetos")
def  projetos ():
    return render_template ("projetos.html")

if __name__ == '__main__':
    app.run()