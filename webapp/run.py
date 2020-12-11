from web import app

HOST = '127.0.0.1'
PORT = 8090
DEBUG = True

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
