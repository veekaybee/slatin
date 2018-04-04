'''
Transliterates Latin to Cyrillic
'''


from flask import Flask, request, render_template, url_for
from transliterate import translit


app = Flask(__name__, static_url_path = "/static", static_folder = "/static")


@app.route('/')
@app.route('/index')
def my_form():
    return render_template('index.html')



@app.route('/response', methods=['GET', 'POST'])

def my_form_post():
    if request.method == 'POST':
        text = request.form['text']
        text = translit(text, "ru")
        return render_template("response.html", responses = text)


if __name__ == "__main__":
    app.run()