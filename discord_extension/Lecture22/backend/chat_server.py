import SimpleServer
import json

# classes are our friends!
class ChatServer:
    def __init__(self):
        pass

    # this is the server request callback function. You can't change its form
    def handle_request(self, request):
        print(request)
        return 'hello world'

def main():
    # make the server
    handler = ChatServer()
    # start the server to handle internet requests!
    SimpleServer.run_server(handler, 8000)

if __name__ == '__main__':
    main()