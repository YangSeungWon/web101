from flask import Flask, render_template, redirect
from markupsafe import escape
import jinja2
app = Flask(__name__)

@app.route('/')
def index():
    navigation = [
        {
            'slide': 3,
            'href': '/basic_html',
            'caption': '기본적인 HTML',
        },
    ]
    return render_template('index.html', navigation=navigation)

@app.route('/<filename>')
def static_server(filename):
    try:
        return render_template(f'{escape(filename)}.html')
    except jinja2.exceptions.TemplateNotFound:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)