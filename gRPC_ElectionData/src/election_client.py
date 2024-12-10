import grpc
import election_pb2
import election_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = election_pb2_grpc.ElectionServiceStub(channel)

    request = election_pb2.MessageRequest(regionID="123")

    # sending the request to the server
    response = stub.GetElectionResults(request)

    # printing the response
    print("Client received: " + "\n" + response.responseData)


if __name__ == '__main__':
    run()