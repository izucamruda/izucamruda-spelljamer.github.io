import http.server
import socketserver

PORT = 8000

class SpelljammerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # Читаем HTML из отдельного файла
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        self.wfile.write(html_content.encode('utf-8'))

def run_server():
    with socketserver.TCPServer(("", PORT), SpelljammerHandler) as httpd:
        print(f"Сервер запущен на http://localhost:{PORT}")
        print("Остановка: Ctrl+C")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()