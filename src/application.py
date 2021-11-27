from flask import app, Flask, render_template
minha_app = Flask(__name__)

@minha_app.route("/")
@minha_app.route("/index")
def  home ():
    return render_template ("home.html")

@minha_app.route ("/curiosidades")
def  curiosidades ():
    return render_template ("curiosidades.html")

@minha_app.route ("/curriculum")
def  curriculum ():
    return render_template ("curriculum.html")


@minha_app.route ("/projetos")
def  projetos ():
    return render_template ("projetos.html")

if __name__ == '__main__':
    minha_app.run('0.0.0.0')