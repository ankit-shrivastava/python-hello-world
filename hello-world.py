#!/usr/bin/python
import subprocess,os
from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 80

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

  #Handler for the GET requests
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    # Send the html message
    self.wfile.write(b"*** Python - Hello World ! ***\n")
    self.wfile.write(b"Hostname is : " + subprocess.check_output("uname -n", shell=True))
    self.wfile.write(b"Process ID  : " + str(os.getpid()).encode('utf-8'))
    return

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print ('Started httpserver on port ' , PORT_NUMBER)

  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print ('^C received, shutting down the web server')
  server.socket.close()
