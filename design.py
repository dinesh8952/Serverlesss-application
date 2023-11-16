from flask import Flask, render_template, request, jsonify
import requests
import json
design = Flask(__name__)
lambda_function_endpoint = "https://jtvbg9d59f.execute-api.ap-south-1.amazonaws.com/default/samee"
@design.route('/add')
def index():
    return render_template('add.html')


@design.route('/get')
def get():
    return render_template('get.html')

@design.route('/delete')
def delete():
    return render_template('delete.html')


@design.route('/get_data', methods=['POST'] )
def submit_post():
    # Get data from the form
    user_name = request.form.get('user_name')
    # email = request.form.get('email')
    # print(user_name)
    # print(email)

    # Create data object
    data = {
	"user_name":user_name
    }

    data1=json.dumps(data)

    

    # Simulate the Lambda function endpoint
    # # Replace this with your actual Lambda function endpoint
    # lambda_function_endpoint = 'https://g5h3ff4t34.execute-api.ap-northeast-1.amazonaws.com/default/all-methods-function'

    headers = {
    "Content-Type": "application/json"
    }
    
    # body= json.stringify(data)
    # print(body)

    # Make a POST request to the Lambda function
    response = requests.get(lambda_function_endpoint, data=data1 ,headers=headers )
    

    # Process the response
    if response.status_code == 200:
        return jsonify(response.text)
    else:
        return jsonify(response.text)





@design.route('/add_data', methods=['POST'])
def submit_add():
    # Get data from the form
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    # print(user_name)
    # print(email)

    # Create data object
    data = {
	"user_name":user_name,
	"email": email
    }

    data1=json.dumps(data)

    

    # Simulate the Lambda function endpoint
    # Replace this with your actual Lambda function endpoint
    # lambda_function_endpoint = 'https://g5h3ff4t34.execute-api.ap-northeast-1.amazonaws.com/default/all-methods-function'

    headers = {
    "Content-Type": "application/json"
    }
    
    # body= json.stringify(data)
    # print(body)

    # Make a POST request to the Lambda function
    response = requests.post(lambda_function_endpoint, data=data1 ,headers=headers )
    

    # Process the response
    if response.status_code == 200:
        return jsonify({'status': 'success', 'message': 'User registered successfully!'})
    else:
        return jsonify({'status': 'error', 'message': 'Error occurred while registering the user.'})





@design.route('/delete_data', methods=['POST'])
def submit_delete():
    # Get data from the form
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    # print(user_name)
    # print(email)

    # Create data object
    data = {
	"user_name":user_name,
	"email": email
    }

    data1=json.dumps(data)

    

    # Simulate the Lambda function endpoint
    # Replace this with your actual Lambda function endpoint
    # lambda_function_endpoint = 'https://g5h3ff4t34.execute-api.ap-northeast-1.amazonaws.com/default/all-methods-function'

    headers = {
    "Content-Type": "application/json"
    }
    
    # body= json.stringify(data)
    # print(body)

    # Make a POST request to the Lambda function
    response = requests.delete(lambda_function_endpoint, data=data1 ,headers=headers )
    

    # Process the response
    if response.status_code == 200:
        return jsonify({'status': 'success', 'message': 'User deleted successfully!'})
    else:
        return jsonify({'status': 'error', 'message': 'Error occurred while deleting the user.'})



if __name__ == '__main__':
    design.run(debug=True)
