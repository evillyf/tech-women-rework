from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#executar somente o arquivo principal
#debug true para fazer alteração automáticamente na página web
if __name__ == '__main__':
    app.run(debug=True)  

