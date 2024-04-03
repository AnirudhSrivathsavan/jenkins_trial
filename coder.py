import http.server
import os
import socketserver
from urllib.parse import parse_qs, urlparse
import sys

arg1 = sys.argv[1]


PORT = 8000
web_dir = "." 
Handler = http.server.SimpleHTTPRequestHandler

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Check if 'textfield' parameter exists in the query
            # Get the value of 'textfield'
            
            # Fill the content in the div
        output_content = f"<p>Paramenter: {arg1}</p>"
        
        # Serve the modified index.html with the filled content
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(os.path.join(web_dir, "index.html"), "rb") as f:
            content = f.read().decode("utf-8")
            # Inject the output content into the div with id 'output'
            content_with_output = content.replace('<div id="output"></div>', f'<div id="output">{output_content}</div>')
            self.wfile.write(content_with_output.encode("utf-8"))
        

# Change directory to the location of your index.html file
os.chdir(web_dir)

# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()