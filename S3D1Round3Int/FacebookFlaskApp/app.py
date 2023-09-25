from flask import Flask, jsonify
app = Flask(__name__)
post = {}
@app.route('/posts')
def postCreation():
    postKye = input("Enter Your UserName:- ")
    postValue = input("Enter Caption for your Post:- ")
    post[postKye]=postValue
    print(post[postKye])
    return f"SuccessFully Created {post[postKye]} "

@app.route('/posts/delete/<username>')
def delete_creation(username):
    if username in post:
        del post[username]
        return f"{username} Deleted Successfully! "
    return f"{username} not found! "

@app.route("/getposts")
def get_app_posts():
    return jsonify(post)
    
if __name__=='__main__':
    app.run(debug=True)
