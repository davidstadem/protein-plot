from flask import Flask
import markdown

app = Flask(__name__)


@app.route('/')
def readme():
    with open('README.md', 'r') as file:
        content = file.read()
        html_content = markdown.markdown(content)
    return html_content


if __name__ == '__main__':
    app.run(debug=True)

