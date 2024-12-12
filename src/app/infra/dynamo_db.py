import boto3

from helper import constants


class DynamoDB():
    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.table_name = constants.dynamo_db_name
    
    def put_item(self, item):
        response = self.client.put_item(
            TableName=self.table_name,
            Item=item
        )

    def get_item(self, pk : str):
        return self.client.get_item(
            Key=pk,
            AttributesToGet=[
                'heaviest_file_name',
                'heaviest_file_size',
                'lightest_file_name',
                'lightest_file_size'                
            ]
        )
