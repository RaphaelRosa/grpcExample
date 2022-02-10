from concurrent import futures

import grpc

import server.proto.TaskList_pb2_grpc as handler
from server.task_list_servicer import TaskListServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    handler.add_TaskListServicer_to_server(TaskListServicer(), server)
    server.add_insecure_port('[::]:50051')
    try:
        server.start()
        print("Server started @ 0.0.0.0:50051")
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        print("Server disconnected")


serve()
