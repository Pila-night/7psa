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


class MyUDPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
  
        self.data = self.rfile.readline().strip().decode('utf-8')
        if self.data in students:
            greeting = f"Привет, {students[self.data]}\n"
            self.wfile.write(greeting.encode('utf-8'))
        else:
            error_message = "Ошибка: Фамилия не найдена.\n"
            self.wfile.write(error_message.encode('utf-8'))

port = int(input("Введите порт для запуска сервера: "))        
with socketserver.UDPServer(('',port), MyUDPHandler) as server:
    print(f"Сервер запущен на порту {port}")
    server.serve_forever()
