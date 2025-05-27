# Weather Checker 🌦️  

Проект для получения прогноза погоды с использованием Django REST Framework. Включает тесты на `pytest` для проверки работоспособности API, корректности вывода данных и обработки различных сценариев.  

---

## 🛠 Технологии  
- **Backend**: Django 4.2, Django REST Framework  
- **Тестирование**: pytest
- **Внешние API**: Open-Meteo (геокодинг и прогноз погоды)  

---

## ⚙️ Установка и запуск  
```bash  
# 1. Клонируйте репозиторий  
git clone https://github.com/sxmeth1ng/weather_checker.git  
cd weather_checker  

# 2. Создайте и активируйте виртуальное окружение  
python -m venv venv  

# Для Linux/macOS:  
source venv/bin/activate  

# Для Windows:  
venv\Scripts\activate  

# 3. Установите зависимости  
pip install -r requirements.txt  

# 4. Запустите сервер  
python manage.py runserver  
