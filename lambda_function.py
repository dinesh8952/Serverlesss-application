import json
import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table_name = 'UserRegistrationTable'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        if event['httpMethod'] == 'POST':
            # Parse registration data from the Lambda event
            body = json.loads(event['body'])
            user_name = body['user_name']
            email = body['email']

            # Store data in DynamoDB
            table.put_item(
                Item={
                    'user_name': user_name,
                    'email': email
                }
            )

            # Return a successful response
            response = {
                'statusCode': 200,
                'body': json.dumps('User registered successfully!')
            }

        elif event['httpMethod'] == 'GET':
            try:
                # if event['httpMethod'] == 'POST':
                    
                    data = json.loads(event['body'])
                    user_name = data.get('user_name')
                    # email = data.get('email')

                    
                    if user_name : #and email
                        
                        response = table.query(
                            KeyConditionExpression=Key('user_name').eq(user_name)  
                        )

                        
                        items = response.get('Items', [])

                        if items:
                            return {
                                'statusCode': 200,
                                'body': json.dumps(items)
                            }
                        else:
                            return {
                                'statusCode': 404,
                                'body': json.dumps({'error': 'Items not found'})
                            }
                    else:
                        return {
                            'statusCode': 400,
                            'body': json.dumps({'error': 'Both user_name and email are required in the request body.'})
                        }

            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps({'error': f'Error: {str(e)}'})
                }

        elif event['httpMethod'] == 'DELETE':
            # Assuming you want to delete an item based on user_name and email
            body = json.loads(event['body'])
            user_name = body['user_name']
            email = body['email']

            if user_name:
                # User exists, proceed with deletion
                table.delete_item(
                    Key={
                        'user_name': user_name ,
                        'email':email
                    }
                )

                # Return a successful response
                return {
                    'statusCode': 200,
                    'body': json.dumps('User deleted successfully!')
                }
            else:
                # User not found, return an appropriate response
                return {
                    'statusCode': 404,
                    'body': json.dumps('User not found!')
                }
            

        else:
            response = {
                'statusCode': 400,
                'body': json.dumps('Invalid HTTP method')
            }

    except Exception as e:
        # Return an error response if something goes wrong
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

    return response