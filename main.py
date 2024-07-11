from flask import Flask, request

app = Flask(__name__)

from user_input import user_input

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/find_courses', methods=['GET', 'POST'])
def find_courses():
    if request.method == 'POST':
        user_question = request.form['user_question']
        db_index = request.form['db_index']
        if not user_question or not db_index:
            return  """Please provide user_question and db_index in the request body.
                        db_index should be one of the following: laborBenefit_index, faiss_index
                    """
        
        response = user_input(user_question, db_index)

        return response

    return "Find course function is now working!"

if __name__ == '__main__':
    app.run(debug=True)