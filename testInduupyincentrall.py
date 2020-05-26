import boto3
rekognition = boto3.client("rekognition")

def handler(event, context):
    try:
        data = rekognition.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': "indunil.trigger",
                    'Name': "obama.jpg"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed induu"}
