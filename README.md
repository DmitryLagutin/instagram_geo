# 📷 Instagram Geo Tracker

Python-инструмент для анализа геолокации публикаций в Instagram с использованием библиотеки `instabot`.

## 🎯 Описание проекта

Этот скрипт автоматически собирает данные о геолокациях из последних публикаций указанного Instagram-аккаунта. Полезно для:
- Геомаркетинга и анализа аудитории
- Исследования популярных локаций
- Мониторинга активности брендов
- Собраниe данных для аналитики

### Ключевые функции:

✅ Получение списка последних публикаций пользователя  
✅ Извлечение информации о геолокации каждой публикации  
✅ Вывод названия локации, широты и долготы  
✅ Обработка ошибок (публикации без геотега)  

## 🔧 Технологии

| Компонент | Версия | Описание |
|-----------|--------|----------|
| **Язык** | Python 3.x | Основной язык программирования |
| **Библиотека** | instabot | Python-клиент для автоматизации Instagram |
| **Дополнительно** | pprint, time | Для форматирования вывода и контроля скорости |

## 🚀 Установка

### Требования

- Python 3.6+
- pip (менеджер пакетов Python)
- Аккаунт Instagram (не заблокированный)

### Установка зависимостей

```bash
pip install instabot
```

## ⚙️ Конфигурация

### Параметры авторизации

В файле `main.py` укажите учетные данные:

```python
bot = Bot()
bot.login(username='ВАШ_НИКНЕЙМ', password='ВАШ_ПАРОЛЬ')
```

⚠️ **Важно:** Не храните пароли в коде! Используйте переменные окружения или config-файл.

## 📋 Использование

### Базовое использование

Запустите скрипт:

```bash
python main.py
```

Скрипт выполнит следующие действия:
1. Авторизуется в Instagram
2. Получит последние публикации указанного пользователя
3. Для каждой публикации извлечет геолокацию
4. Выведет название, широту и долготу локации

### Пример вывода:

```
1
Moscow Kremlin
55.752020
37.617499
2
Times Square
40.758896
-73.985130
Ошибка
...
```

### Настройка целевого пользователя

Измените строку в коде:

```python
twony_last_medias = bot.get_user_medias('имя_пользователя', filtration=None)
```

### Настройка лимита публикаций

По умолчанию обрабатываются ВСЕ последние публикации. Чтобы ограничить количество:

```python
max_posts = 50  # Обрабатывать не более 50 публикаций
twony_last_medias = bot.get_user_medias('имя_пользователя', filtration=None)[:max_posts]
```

### Пауза между запросами

Установите паузу для предотвращения блокировки:

```python
time.sleep(3)  # Пауза 3 секунды между запросами
```

## 🔍 Структура кода

### Основные компоненты

```
instagram_geo/
├── README.md         # Эта документация
├── main.py          # Основной скрипт анализа
└── requirements.txt # Зависимости (если создан)
```

### Функции instabot

| Функция | Описание |
|---------|----------|
| `bot.login()` | Авторизация в Instagram |
| `bot.get_user_medias()` | Получение публикаций пользователя |
| `bot.get_media_id_from_link()` | Извлечение ID публикации по ссылке |
| `bot.get_media_likers()` | Получение пользователей лайкнувших пост |
| `bot.get_media_commenters()` | Получение авторов комментариев |
| `bot.get_media_comments()` | Получение комментариев к посту |

## 📊 Возможные применения

### 1. Геомаркетинг

Анализ географического распределения аудитории:
```python
locations = {}
for post in medias:
    loc_name = post.get('location', {}).get('name', 'Unknown')
    locations[loc_name] = locations.get(loc_name, 0) + 1

for name, count in sorted(locations.items(), key=lambda x: -x[1]):
    print(f"{name}: {count} публикаций")
```

### 2. Сбор статистики

Сохранение результатов в CSV/JSON:

```python
import csv

with open('geo_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Location', 'Lat', 'Lng'])
    for post in medias:
        if 'location' in post and post['location']:
            loc = post['location']
            writer.writerow([loc.get('name'), loc.get('lat'), loc.get('lng')])
```

## ⚠️ Важные предупреждения

### Ограничения Instagram API

- Instagram имеет строгие лимиты на количество запросов
- Частые запросы могут привести к временной блокировке аккаунта
- Используйте `time.sleep()` для пауз между запросами

### Безопасность

1. **Не публикуйте свои учетные данные!**
2. Используйте двухфакторную аутентификацию (2FA)
3. Рассмотрите использование app-specific passwords
4. Регулярно меняйте пароль

### Юридическое предупреждение

Используйте этот инструмент в соответствии с:
- Условиями использования Instagram
- Законом о защите персональных данных (152-ФЗ в РФ)
- Политикой конфиденциальности

## 🐛 Решенные проблемы

### Проблема: "Login failed"

**Решение:**
1. Проверьте правильность логина и пароля
2. Если включена 2FA, используйте app password
3. Попробуйте войти через веб-интерфейс

### Проблема: "Rate limit exceeded"

**Решение:**
1. Увеличьте паузу между запросами (`time.sleep(5+)`)
2. Подождите несколько часов перед повторным запуском
3. Ограничьте количество анализируемых постов

## 💡 Расширение функциональности

### Сохранение результатов в файл

```python
from datetime import datetime

output_file = f'geo_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
# ... код сохранения ...
```

### Фильтрация по минимальному количеству публикаций

```python
min_posts = 5  # Показать только локации с 5+ публикациями
popular_locations = {k: v for k, v in locations.items() if v >= min_posts}
```

### Визуализация на карте

```python
import folium

m = folium.Map(location=[55.75, 37.61], zoom_start=10)
for post in medias_with_geo:
    loc = post['location']
    folium.Marker([loc['lat'], loc['lng']], popup=loc['name']).add_to(m)

m.save('locations_map.html')
```

## 🔗 Полезные ссылки

- [Instabot documentation](https://github.com/martijnberger/InstaBot)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/)
- [Geolocation data formats](https://en.wikipedia.org/wiki/Geographic_coordinate_system)

## 📝 License

Проект предназначен для образовательных целей. Используйте ответственно.

## 👤 Автор

Разработано [@DmitryLagutin](https://github.com/DmitryLagutin)

---

*Happy tracking! 📍*
