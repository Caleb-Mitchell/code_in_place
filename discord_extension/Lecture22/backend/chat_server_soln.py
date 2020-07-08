import SimpleServer
import json

# classes are our friends!
class ChatServer:
    def __init__(self):
        """
        We need data to 'persist' between requests. What data? in this case a
        history of messages
        """
        self.history = []

    # this is the server request callback function. You can't change its header
    def handle_request(self, request):
        """
        A message has just arrived. From the internet! They need our help
        """
        cmd = request.get_command()
        params = request.get_params()
        if cmd == 'getMsgs':
            return self.get_messages(params)
        if cmd == 'newMsg':
            return self.new_message(params)
        return 'unknown command: ' + cmd

    def get_messages(self, params):
        start_index = int(params['index'])
        # slice that list!
        to_return = self.history[start_index:]
        return json.dumps(to_return)

    def new_message(self, params):
        user = params['user']
        msg = params['msg']
        self.history.append('[' + user + '] ' + msg)
        return 'success'

def main():
    # make the server
    handler = ChatServer()
    # start the server to handle internet requests!
    SimpleServer.run_server(handler, 8000)

if __name__ == '__main__':
    main()