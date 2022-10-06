from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!, my name is Aakarshit Agarwal</p>"

@app.route('/products')
def products():
    return 'This is the page to build products'

@app.route('/helloworld')
def hello_world2():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)