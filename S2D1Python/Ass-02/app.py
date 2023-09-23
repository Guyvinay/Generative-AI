
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

store = {}

@app.route('/create', methods=['POST','GET'])
def create():
    if request.method=='POST':
        key = request.form['key']
        value = request.form['value']
        store[key] = value
        # return redirect('/read')
        return render_template('create.html')
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=store)

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        key = request.form['key']
        if key in store:
            value = request.form['value']
            store[key] = value
            return redirect('/read')
        else:
            return "Key Not Found"
    return render_template('update.html')    

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in store :
            del store[key]
            return redirect('/read')
        else :
            return "Key not found"
    return render_template('delete.html')    

if __name__== '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # In-memory dictionary to store data
# data_dict = {}

# # Route for creating a new entry
# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         key = request.form['key']
#         value = request.form['value']
#         data_dict[key] = value
#         return redirect('/read')
#     return render_template('create.html')

# # Route for reading the current state of the dictionary
# @app.route('/read')
# def read():
#     return render_template('read.html', data=data_dict)

# # Route for updating an existing entry
# @app.route('/update', methods=['GET', 'POST'])
# def update():
#     if request.method == 'POST':
#         key = request.form['key']
#         if key in data_dict:
#             value = request.form['value']
#             data_dict[key] = value
#             return redirect('/read')
#         else:
#             return "Key not found."
#     return render_template('update.html')

# # Route for deleting an existing entry
# @app.route('/delete', methods=['GET', 'POST'])
# def delete():
#     if request.method == 'POST':
#         key = request.form['key']
#         if key in data_dict:
#             del data_dict[key]
#             return redirect('/read')
#         else:
#             return "Key not found."
#     return render_template('delete.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask , render_template , request , redirect , url_for

# store = {}

# @app.route('/create',methods=['GET','POST'])
# def create():
#     if request.method == 'POST':
#         key = request.form['key']
#         value = request.form['value']
#         store[key] = value
#     return render_template('./create.html')

# @app.route('/read')
# def read():
#     return render_template('./read.html', data=store)