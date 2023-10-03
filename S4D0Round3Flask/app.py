
# Problem Statement: Building a Basic Social Media Web Application Backend using Flask and TDD

# Objective:

# Your objective is to create the backend for a simple social media web application, similar to Instagram, using Flask and following Test-Driven Development (TDD) principles. This application will not involve database integration or user authentication; instead, it will manage data using Flask and in-memory data structures.

# Requirements:

# 1. Post Creation:
#    - Create an API endpoint for users to create new posts, each including a username and a caption.
#    - Define a data structure within your Flask application to represent a "post," including fields for username and caption.

# 2. Post Viewing:
#    - Implement an API endpoint to display all posts in the system.

# 3. Post Deletion:
#    - Develop a feature allowing users to delete a post using its unique ID.
#    - Gracefully handle scenarios where a user tries to delete a non-existent post.

# Resources:
# Flask Official Documentation

# Advanced Tasks (Bonus):

# 1. Like Feature:
#    - Integrate a "like" mechanism enabling users to like posts.
#    - Each post should maintain a count of the total number of likes it has received.
#    - Create an API endpoint to increment the like count for a post.

# 2. Comment Feature:
#    - Enhance the application with a "comment" functionality, allowing users to add comments to posts.
#    - Implement a data structure to store comments for each post.
#    - Develop an API endpoint to add comments to a post.

# Focus:

# This task focuses on backend development using Flask. There is no requirement for frontend design. Your performance will be evaluated based on your proficiency in backend development within the Flask environment and your ability to apply TDD principles effectively.

# Submission:

# Submit your code along with comprehensive test cases that demonstrate your implementation meets the stated requirements and bonus tasks (if attempted). Ensure your submission is well-documented, maintainable, and adheres to best practices in Flask development and TDD.

from flask import Flask, jsonify,request

app = Flask(__name__)

postDict = {}


@app.route('/post',methods=['POST'])
def postRoute():
    data = request.get_json
    name = data.get('username')
    caption = data.get('caption')
    postDict[name]=caption
    return "Post created Successfuly"
@app.route('/posts/<name>')
def postRoutes(name):
    if name in postDict:
        return jsonify({
            "name":f"{name}",
            "caption":f"{postDict[name]}"
        })
    
    return "Post created Successfuly"

if __name__ == "__main__":
    app.run(debug=True)