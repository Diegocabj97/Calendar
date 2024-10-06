import http.server
import socketserver
import json
import calendar
from urllib.parse import parse_qs

PORT = 8000

def create_calendar_matrix(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return {
        "month_name": month_name,
        "year": year,
        "calendar": cal
    }

class CalendarHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/get_calendar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            
            year = int(params['year'][0])
            month = int(params['month'][0])
            
            calendar_data = create_calendar_matrix(year, month)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(calendar_data).encode())
        else:
            super().do_POST()

with socketserver.TCPServer(("", PORT), CalendarHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()