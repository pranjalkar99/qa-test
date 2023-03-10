from flask import Flask,render_template,redirect, url_for,request
app = Flask(__name__)
import json
status="default"
#Setting DB initially 1
# 
# 
# .
#                       ***********************  Setting up models  ********************

import sqlite3
from flask import Flask, request, jsonify


def connect_to_database():
  connection = sqlite3.connect('checkboxes.db')
  cursor = connection.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS checkboxes (
      id INTEGER PRIMARY KEY,
      item_id INTEGER,
      is_checked INTEGER
    )
  ''')
  connection.commit()
  return connection

@app.route("/update-checkboxes", methods=["POST"])
def update_checkboxes():
    data = request.get_json()
    checkedIds = data["checkedIds"]

    # Connect to SQLite database
    conn = sqlite3.connect("checkboxes.db")
    cursor = conn.cursor()

    # Update the checkbox states in the database
    cursor.execute("DELETE FROM checkboxes")
    for checkboxId in checkedIds:
        cursor.execute("INSERT INTO checkboxes (id) VALUES (?)", (checkboxId,))
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Checkboxes updated successfully"})
@app.route('/')
def index():

  return render_template('index.html', items=items)







#                   *******************************     Views           ***********************






g=open("new_batch_letera()next_batch_5-2.json","r")
data_db2=json.loads(g.read())
g.close()

f=open("new_batch_letera_3-2.json","r")
data=json.loads(f.read())
f.close()
h=open("new_2019_next_batch_5-2.json","r")
data_2019=json.loads(h.read())

def set_database():
    g=open("new_batch_letera()next_batch_5-2.json","r")
    data_db2=json.loads(g.read())
    g.close()
    return data_db2


@app.route('/start', methods=('GET', 'POST'))
def start():
    data=set_database()
    return redirect(url_for('serve_html',data=data))
         
@app.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        user = request.form['user']
        return redirect(url_for('serve'),user=user)

    return render_template('login.html')
#Just checking
##  ***************************Testing ****************************8
# pages = [
#     "<html><body><h1>Page 1</h1></body></html>",
#     "<html><body><h1>Page 2</h1></body></html>",
#     "<html><body><h1>Page 3</h1></body></html>"
# ]
# @app.route('/')
# def index_test():
#     return "Go to /serve to get started..."

@app.route('/next_test')
def next_page(pages):
    current_page = int(request.args.get('current_page', 0))
    next_page = current_page + 1
    if next_page >= len(pages):
        next_page = 0
    return render_template('index_test.html', pages=pages, current_page=next_page)

#   
########################## end of testing ####################3333
import json
@app.route("/serve", methods=('GET', 'POST'))
def serve_html():
    
    # items = [
    # { 'id': 1, 'name': 'Item 1' },
    # { 'id': 2, 'name': 'Item 2' },
    # { 'id': 3, 'name': 'Item 3' }]
    # connection = connect_to_database()
    # cursor = connection.cursor()
    # cursor.execute('SELECT item_id, is_checked FROM checkboxes')
    # checked_items = cursor.fetchall()

    # for item in items:
    #   item['is_checked'] = False
    #   for checked_item in checked_items:
    #     if item['id'] == checked_item[0]:
    #       item['is_checked'] = True 
    if request.method=='POST':
        db=request.form.get('db')
        if db=='db2':
            return redirect(url_for("db2",db=db))
        if db=='db3':
            return redirect(url_for("db3",db=db))
        your_variable=False
        ids = {obj["iden"] for obj in data}
        identifier={}
        for each in ids:
            identifier[each]={}
            identifier[each]['link']=url_for('page',id=each)
            identifier[each]['status']=status
            for obje in data:
                if obje['iden']==each:
                    name=obje['name']
                    identifier[each]['name']=name 
        return render_template("index.html",ids=identifier,your_variable=your_variable,dboption=10)#,items=items)
    return render_template("index.html",dboption=11)#,items=items)
      #return data[0]





# @app.route('/next_test')
# def next_page(pages):
#     current_page = int(request.args.get('current_page', 0))
#     next_page = current_page + 1
#     if next_page >= len(pages):
#         next_page = 0
#     return render_template('index_test.html', pages=pages, current_page=next_page)


current_page = 0

@app.route('/serve/<id>', methods=['GET', 'POST'])
def page(id):
    obj = next((obj for obj in data if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page,)

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0)
    

## @Rajdeep write js code to update the status after button is clicked on page.html so that next time when index is loaded, status of that is updated...
# def update_status(id):
#     console.log(id)
#     print(id)
#     status="success"

print(len(data_db2))
@app.route("/db2")
def db2():
    # data_db2=set_database()
    your_variable=False
    print("db2")
    ids = {obj["iden"] for obj in data_db2}
    identifier={}
    for each in ids:
        identifier[each]={}
        identifier[each]['link']=url_for('page_db2',id=each)
        identifier[each]['status']=status
        for obje in data_db2:
            if obje['iden']==each:
                print("gotcha")
                name=obje['name']
                identifier[each]['name']=name
    print(ids)
    return render_template("index.html",ids=identifier,your_variable=your_variable,dboption=2)

@app.route('/db2/<id>', methods=['GET', 'POST'])
def page_db2(id):
    obj = next((obj for obj in data_db2 if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page,)

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0)
    
@app.route("/db3")
def db3():
    # data_db2=set_database()
    your_variable=False
    print("db2")
    ids = {obj["iden"] for obj in data_2019}
    identifier={}
    for each in ids:
        identifier[each]={}
        identifier[each]['link']=url_for('page_db3',id=each)
        identifier[each]['status']=status
        for obje in data_2019:
            if obje['iden']==each:
                name=obje['name']
                identifier[each]['name']=name
    print(ids)
    return render_template("index.html",ids=identifier,your_variable=your_variable,dboption=-1)


@app.route('/db3/<id>', methods=['GET', 'POST'])
def page_db3(id):
    obj = next((obj for obj in data_2019 if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page,id=obj['iden'])

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0,id=obj['iden'])
    