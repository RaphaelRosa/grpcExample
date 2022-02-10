from __future__ import annotations

from server.database import TaskEntity
from server.proto.TaskList_pb2 import CreateTaskMessage, TaskCreatedMessage, TaskListMessage, Empty, \
    CompleteTaskMessage, TaskMessage
import server.proto.TaskList_pb2_grpc as proto


class TaskListServicer(proto.TaskListServicer):
    def CreateTask(self, request: CreateTaskMessage, context) -> TaskCreatedMessage:
        print("Creating task")
        task = self.create_task(request)
        print(f"\n--------\nTask created:\n{task.id=}\n{task.title=}\n{task.description=}\n--------\n")
        return TaskCreatedMessage(id=task.id)

    def ListTasks(self, request: Empty, context) -> TaskListMessage:
        print("Getting tasks")
        result = self.list_tasks()
        return result

    def CompleteTask(self, request: CompleteTaskMessage, context) -> Empty:
        print(f"Completing task {request.id}")
        self.complete_task(request)
        return Empty()

    def create_task(self, request):
        task = TaskEntity.create(title=request.title, description=request.description)
        return task

    def list_tasks(self):
        tasks = TaskEntity.select()
        result = TaskListMessage()
        for task in tasks:
            result.tasks.append(TaskMessage(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=task.completed
            ))
        return result

    def complete_task(self, request):
        query = TaskEntity.update(completed=True).where(TaskEntity.id == request.id)
        query.execute()
