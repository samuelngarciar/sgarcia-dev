#!/usr/bin/env python3
"""
Simple HTTP server to serve the Cloud Native consulting website
Serves static files and handles basic routing
"""

import os
import http.server
import socketserver
import mimetypes
from urllib.parse import urlparse

class CloudNativeHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for the Cloud Native consulting website"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def do_GET(self):
        """Handle GET requests with custom routing"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Remove leading slash for file system operations
        if path.startswith('/'):
            path = path[1:]
        
        # Default to index.html for root path and directories
        if path == '' or path.endswith('/'):
            path = 'index.html'
        
        # Handle SPA routing - serve index.html for non-file paths
        if not os.path.exists(path) and '.' not in os.path.basename(path):
            path = 'index.html'
        
        # Check if file exists
        if os.path.exists(path) and os.path.isfile(path):
            self.serve_file(path)
        else:
            self.send_error(404, "File not found")
    
    def serve_file(self, filepath):
        """Serve a static file with appropriate headers"""
        try:
            # Get file size
            file_size = os.path.getsize(filepath)
            
            # Determine content type
            content_type, _ = mimetypes.guess_type(filepath)
            if content_type is None:
                content_type = 'application/octet-stream'
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(file_size))
            
            # Add caching headers for static assets
            if filepath.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg')):
                self.send_header('Cache-Control', 'public, max-age=31536000')  # 1 year
            else:
                self.send_header('Cache-Control', 'public, max-age=3600')  # 1 hour
            
            # Security headers
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('X-Frame-Options', 'DENY')
            self.send_header('X-XSS-Protection', '1; mode=block')
            
            self.end_headers()
            
            # Send file content
            with open(filepath, 'rb') as f:
                self.copyfile(f, self.wfile)
                
        except Exception as e:
            print(f"Error serving file {filepath}: {e}")
            self.send_error(500, "Internal server error")
    
    def log_message(self, format, *args):
        """Custom logging format"""
        print(f"[{self.address_string()}] {format % args}")

def run_server(port=5000, host='0.0.0.0'):
    """Run the HTTP server"""
    
    # Ensure we're in the correct directory
    if not os.path.exists('index.html'):
        print("Error: index.html not found in current directory")
        print("Make sure you're running the server from the project root")
        return
    
    try:
        with socketserver.TCPServer((host, port), CloudNativeHandler) as httpd:
            print(f"Cloud Native Consulting Website")
            print(f"Server running at http://{host}:{port}/")
            print(f"Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Serve forever
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Error: Port {port} is already in use")
            print("Try using a different port or stop the existing process")
        else:
            print(f"Error starting server: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    import sys
    
    # Default values
    port = 5000
    host = '0.0.0.0'
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5000")
    
    if len(sys.argv) > 2:
        host = sys.argv[2]
    
    # Validate port range
    if not (1 <= port <= 65535):
        print("Port must be between 1 and 65535. Using default port 5000")
        port = 5000
    
    # Start the server
    run_server(port, host)
