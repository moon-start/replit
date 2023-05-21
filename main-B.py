from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  return "Index Page123"


app.run(host="127.0.0.1", port=80)

# print(123)
###########################
# from flask import Flask

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#   return "Index Page"

# app.run(host="127.0.0.1", port=80)
#####################

# from flask import Flask
# from threading import Thread

# app = Flask(__name__)

# @app.route('/')
# def main():
#   return 'Bot is aLive!'

# def run():
#   app.run(host="127.0.0.1", port=80)

# def keep_alive():
#   server = Thread(target=run)
#   server.start()

######################

# #######################################################################
# from http.server import HTTPServer, CGIHTTPRequestHandler

# port = 80

# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print("Starting simple_httpd on port: " + str(httpd.server_port))
# httpd.serve_forever()
# ########################
