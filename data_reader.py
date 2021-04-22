from pymongo import MongoClient

def read_data(uri:str, database:str):
    client = MongoClient(uri)
    result = client[database]['dynamicRisk'].aggregate([
        {
            '$lookup': {
                'from': 'patientContext', 
                'localField': 'patientContextId', 
                'foreignField': '_id', 
                'as': 'context'
            }
        }, {
            '$lookup': {
                'from': 'patientHistory', 
                'localField': 'context.patientId', 
                'foreignField': '_id', 
                'as': 'history'
            }
        }
    ])
    
    return result
