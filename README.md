# Shortlink
#### Приложение, позволяющее сокращать ссылки

##### Функционал:
- принимает url адрес;
- сокращает путь до 5 символов;
- считает кол-во кликов по сокращенной ссылке;
- хранит историю:
   1. оригинальную ссылку;
   2. сокращенную ссылку;
   3. дату добавления ссылки;
   4. количество кликов по сокращенной ссылке.
- очищает историю.

Нажатие на сокращенную ссылку приводит к перенаправлению 
на оригинальную ссылку.

Url_hash генерируется с помощью алгоритма
хеширования MD5 для поля full_url
и использует только первые 5 символов, 
которые возвращает метод save() модели, 
выполняемый каждый раз, когда Django сохраняет 
запись в базе данных. Кроме того, прописана функция(redirect_clicks), 
которая, на основе функции clicked в модели, отслеживает, сколько раз была использована ссылка. 


##### Написан с использованием:
- [Django](https://www.djangoproject.com/);
- [Bootstrap](https://getbootstrap.com/).

##### Чтобы запустить проект локально:
- сделать импорты файла [requirements.txt](./requirements.txt);
- выполнить __python manage.py runserver__.

##### Использование:
- Приложение размещено на Heroku (https://linkshrtapp.herokuapp.com/);
- Доступ в админку: логин - _admin_, пароль - _admin_.

##### Нюансы:
- Время добавления ссылки по Гринвичу (заказчик из UK).

##### Контакты:
- Vk (https://vk.com/lanfor)
- Ссылка на проект (https://github.com/Nik-Verlan/linkshrt)