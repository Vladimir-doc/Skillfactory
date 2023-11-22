
### **Быстрый старт:**
**Для запуска проекта необходимо:**

1. Клонировать репозиторий 

    ➡️  [Github repository](https://github.com/Vladimir-doc/Skillfactory/tree/master/Diplom.git)

2. Установить виртуальное окружение
    ```bash 
    python3 -m venv venv
    ```

    ```bash 
    source ./venv/bin/activate
    ```
3. Установить `requirements.txt`
    ```bash 
    pip install -r requirements.txt
    ```
4. Переходим в директорию:
    ```bash 
    cd silant
    ```
5. Создать пользователя
    ```bash 
    python3 manage.py createsuperuser
    ```
6. Запустить сервер
    ```bash 
    python3 manage.py runserver
    ```

7. Запускаем [Силант](127.0.0.1:8888/search/) 
 
    ⚠️ порт 8888
 
### **Роли:**

Клиент: Trudnikov 

Пароль: Client2023
___

Менеджер: manager1

Пароль: manager
___

Сервисная компания: FNS

Пароль: Client2023
____



**Технические моменты**

1. Импорт данных из Exel в SQL производиться с помощью Django import/expot


2. Разметка страницы делиться на :
- ```header```
- ```main``` 
- ```footer```

все это вынесено в отдельные js файлы: 
```bash
Header.js
Main.js
Footer.js
```
также вынесен функционал в отдельные компоненты:
```bash
Category.js /*список рецептов определенной категории*/

CategoryList.js 
/*список всех категорий*/

Recipe.js /*список всех рецептов*/

RecipeSingle.js /*определенный рецепт в подробном описании*/
```
все эти компоненты импортируются и собираются в общий файл - App.js


