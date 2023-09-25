from flask import Flask

app = Flask(__name__)

post = {}

@app.route('/post')
def postCreation():
    postKye = input("Enter Your UserName:- ")
    postValue = input("Enter Caption for your Post:- ")
    post[postKye]=postValue
    print(post[postKye])
    return f"SuccessFully Created {post[postKye]} "


if __name__=='__main__':
    app.run(debug=True)
