#!/usr/bin/env python3
"""
Utility script to serve the generated documentation locally.
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

def serve_docs(port=8000):
    """Serve the documentation on localhost."""
    docs_dir = Path(__file__).parent
    build_dir = docs_dir / 'build' / 'html'
    
    if not build_dir.exists():
        print(f"Error: Documentation not built. Run 'make html' first.")
        sys.exit(1)
    
    os.chdir(build_dir)
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            print(f"[{self.log_date_time_string()}] {format % args}")
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            url = f"http://localhost:{port}"
            print(f"Serving documentation at {url}")
            print(f"Press Ctrl+C to stop the server")
            
            # Try to open in browser
            try:
                webbrowser.open(url)
            except:
                pass
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        print(f"Error: Could not bind to port {port}")
        print(f"Make sure the port is not in use.")
        sys.exit(1)

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Usage: {sys.argv[0]} [port]")
            sys.exit(1)
    
    serve_docs(port)
