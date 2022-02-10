import grpc
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from starlette import status

import client_python.proto.TaskList_pb2_grpc
from client_python.proto.TaskList_pb2 import CreateTaskMessage, TaskCreatedMessage, TaskListMessage, Empty, \
    CompleteTaskMessage

app = FastAPI()

channel = grpc.insecure_channel("0.0.0.0:50051")
stub = client_python.proto.TaskList_pb2_grpc.TaskListStub(channel)


class CreateTaskInterface(BaseModel):
    title: str
    description: str


@app.post("/createTask")
async def create_task(payload: CreateTaskInterface):
    response: TaskCreatedMessage = stub.CreateTask(
        CreateTaskMessage(title=payload.title, description=payload.description))
    return ORJSONResponse(status_code=status.HTTP_201_CREATED, content={"id": response.id})


@app.get("/listTasks")
async def list_task():
    response: TaskListMessage = stub.ListTasks(Empty())
    result = {"tasks": []}
    for task in response.tasks:
        result["tasks"].append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed
        })
    return ORJSONResponse(status_code=status.HTTP_200_OK, content=result)


@app.put("/complete/{id}")
async def complete_task(id: int):
    stub.CompleteTask(CompleteTaskMessage(id=id))
    return ORJSONResponse(status_code=status.HTTP_200_OK)
