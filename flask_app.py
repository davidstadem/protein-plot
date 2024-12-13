
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import markdown

app = Flask(__name__)


#@app.route('/')
def hello():
    return_string = 'Hello! Protein Plot, coming soon...'
    try:
        return_string += '\ntrying...'
        html = readme()
    except:
        return_string += '\nfailed!'
    return return_string

@app.route('/')
def readme():
    with open('README.md', 'r') as file:
        content = file.read()
        html_content = markdown.markdown(content)
    return html_content


if __name__ == '__main__':
    app.run(debug=True)

