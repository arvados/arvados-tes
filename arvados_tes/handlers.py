def GetServiceInfo():
    return {
        "id": "",
        "name": "",
        "type": "",
        "description": "",
        "organization": {
        },
        "contactUrl": "",
        "documentationUrl": "",
        "createdAt": "",
        "updatedAt": "",
        "environment": "",
        "version": "",
        "storage": [],
        "tesResources_backend_parameters": []
    }

def ListTasks():
    return {"tasks": []}

def CreateTask(body):
    print(body)
    pass

def GetTask(id):
    print("getting", id)
    return {"id": id}

def CancelTask(id):
    print("canceling", id)
    return {"id": id}
