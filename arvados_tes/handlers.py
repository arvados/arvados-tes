import json
import urllib.parse
import arvados
import arvados.commands.keepdocker

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
    print(json.dumps(body, indent=2))

    mounts = {}

    for inp in body["inputs"]:
        u = urllib.parse.urlparse(inp["url"])
        print(u)

        mounts[inp["path"]] = {
            "kind": "collection",
            "uuid": u.netloc,
            "path": u.path
        }

    # "url": "s3://ce8i5-4zz18-nrm9u73cqjdz4rq/whale.txt",
    #   "path": "/var/lib/cwl/stgb7fd4415-e640-4bc5-9f53-e0e32e8502a3/whale.txt",
    #   "type": "FILE",
    #   "name": "input",
    #   "description": "cwl_input:input"

    mounts[body["executors"][0]["workdir"]] = {
        "kind": "tmp",
        "capacity": int(body["resources"]["disk_gb"] * 1024*1024*1024)
    }

    image_name, image_tag = body["executors"][0]["image"].split(":")

    api = arvados.api()

    images = arvados.commands.keepdocker.list_images_in_arv(api, 3,
                                                            image_name=image_name,
                                                            image_tag=image_tag)

    container_request = {
        "state": "Committed",
        "mounts": mounts,
        "runtime_constraints": {
            "vcpus": body["resources"]["cpu_cores"],
            "ram": int(body["resources"]["ram_gb"] * 1024*1024*1024)
        },
        "container_image": api.collections().get(uuid=images[0][0]).execute()["portable_data_hash"],
        "command": body["executors"][0]["command"],
        "output_path": body["executors"][0]["workdir"],
        "priority": 500
    }

    print(json.dumps(container_request, indent=2))

    cr = api.container_requests().create(body={"container_request": container_request}).execute()

    return {"id": cr["uuid"]}

def GetTask(id):
    api = arvados.api()
    cr = api.container_requests().get(uuid=id).execute()
    con = api.containers().get(uuid=cr["container_uuid"]).execute()

    state = ""

    if con["state"] == "Queued":
        state = "QUEUED"

    if con["state"] == "Locked":
        state = "INITIALIZING"

    if con["state"] == "Running":
        state = "RUNNING"

    if cr["state"] == "Final":
        if con["state"] == "Complete":
            state = "COMPLETE"
        else:
            state = "EXECUTOR_ERROR"

    return {"id": id, "state": state}

def CancelTask(id):
    print("canceling", id)
    return {"id": id}
