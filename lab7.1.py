import socketserver

students = {
    "Беликов": "Алексей",
    "Белов": "Алексей",
    "Бусыгин": "Георгий",
    "Грачев": "Виктор",
    "Дьякова": "Софья",
    "Ермаков": "Никита",
    "Заболотских": "Захар",
    "Какулин": "Артем",
    "Кочегаров": "Андрей",
    "Лунькина": "Арина",
    "Маматкулова": "Руслана",
    "Мамелин": "Дмитрий",
    "Мочалов": "Юрий",
    "Пономарев": "Александр",
    "Сверчков": "Артем",
    "Селуков": "Егор",
    "Сиушкин": "Кирилл",
    "Удалов": "Владислав",
    "Чумазин": "Глеб"
}


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
  
        self.data = self.rfile.readline().strip().decode('utf-8')
        if self.data in students:
            greeting = f"Привет, {students[self.data]}\n"
            self.wfile.write(greeting.encode('utf-8'))
        else:
            error_message = "Ошибка: Фамилия не найдена.\n"
            self.wfile.write(error_message.encode('utf-8'))
        
with socketserver.TCPServer(('', 7777), MyTCPHandler) as server:
    print("Сервер запущен на порту 7777...")
    server.serve_forever()
