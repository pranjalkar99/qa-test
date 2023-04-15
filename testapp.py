from flask import Flask, render_template, request

app = Flask(__name__)
import json
with open('test.json', 'r') as f:
    data = f.read()
dict = json.loads(data)
lst = dict.keys()

# Sample list of dictionaries containing HTML files
html_list = []
for file in lst:
    data = dict[file]
    html_list.append(data)

@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    html_slice = html_list[start:end]
    num_pages = len(html_list) // per_page + (len(html_list) % per_page > 0)
    return render_template('index.html', html_list=html_slice, page=page, num_pages=num_pages)

@app.route('/view-file', methods=['POST'])
def view_file():
    file_index = int(request.form['file_index'])
    file_dict = html_list[file_index]
    file_content = file_dict['text']
    return render_template('file.html', file_content=file_content)


if __name__ == '__main__':
    app.run(debug=True)
