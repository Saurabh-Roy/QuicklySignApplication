from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index():
    return render_template('./display _cv.html')

@app.route('/return_cv')
def return_pdf():
    pass

if __name__ == '__main__':
    app.run(debug=True)