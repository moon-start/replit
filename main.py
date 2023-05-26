# #######################################################################
# from http.server import HTTPServer, CGIHTTPRequestHandler

# port = 80

# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print("Starting simple_httpd on port: " + str(httpd.server_port))
# httpd.serve_forever()
# ########################

from flask import Flask

app = Flask('app')


@app.route('/')
def hello_world():
  return 'Hello, World!666'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
# #     if request.method == 'POST':
# #         return 'Hello ' + request.values['username']

#     if request.method == 'POST':
#         return 'Hello ' + request.values['username']

#     return


# @app.route('/<string:post_id>')
@app.route('/remote')
def remote():
  import os
  SS = os.popen("git remote -V").read()
  print(SS)
  return SS


# @app.route('/<string:post_id>')
@app.route('/exit/')
def show_post():
  # # show the post with the given id, the id is an integer
  # import os
  # # return f'Post {post_id}'
  # # return os.popen()).read()

  # # sys.exit(0)
  # os.kill(os.getppid(), 0)
  import os, sys
  try:
    sys.exit(0)
  except:
    print('die')
  finally:
    print('cleanup')

  try:
    os._exit(0)
  except:
    print('die')
    print('os.exit')  #不列印直接退出
  return "11"


app.run(host='0.0.0.0', port=80)
