# Let's import Flask
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# To stop caching static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'

    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form.get('content', '')
        words = content.split()
        characters = len(content)
        word_count = len(words)
        sentence_count = sum(content.count(p) for p in '.!?')
        paragraph_count = len([p for p in content.split('\n') if p.strip()])
        average_word_length = round(sum(len(word) for word in words) / len(words), 2) if words else 0

        results = {
            'characters': characters,
            'words': word_count,
            'sentences': sentence_count,
            'paragraphs': paragraph_count,
            'average_word_length': average_word_length
        }

        return render_template('result.html', results=results, content=content, title='Analysis Results')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)