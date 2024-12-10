import grpc
from concurrent import futures
import election_pb2
import election_pb2_grpc


class ElectionService(election_pb2_grpc.ElectionService):

    def GetElectionData(self, request, context):
        election = election_pb2.ElectionData(
            regionID="123",
            electionRegion="Sample Region",

        )

        party = election_pb2.Party(
            partyID=2,
            partyName="OEVP",
            votes=1000
        )

        party2 = election_pb2.Party(
            partyID=3,
            partyName="NEOS",
            votes=100
        )

        election.countingData.extend([party])
        election.countingData.extend([party2])

        return election_pb2.MessageResponse(responseData=election)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    election_pb2_grpc.add_ElectionServiceServicer_to_server(election_pb2_grpc.ElectionService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print('Server is running')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()