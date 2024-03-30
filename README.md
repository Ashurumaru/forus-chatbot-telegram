<body>
    <h1>Задачи chatbots</h1>
    <h2>Описание</h2>
    <p>Данный проект был разработан в рамках получения компетенций на сайте <a href="https://students.forus.ru/">Октагон</a>. Разработано с использованием языка программирования python.</p>
      <h2>Технологии и Инструменты</h2>
    <ul>
        <li><strong>Python:</strong> Проект создан с использованием языка программирования python.</li>
        <li><strong>Библиотека python-telegram-bot:</strong> Используется для разработки телеграм бота</li>
        <li><strong>Библиотека aiomysql:</strong> Используется для асинхронного взаимодействия с базой данных MySQL в Python.</li>
    </ul>
      <h2>Инструкция</h2>
    <ul>
        <li>Установите Python, если он еще не установлен. Можно скачать с <a href="https://www.python.org/downloads/">официального сайта Python</a>.(для проекта был использован python 3.11)</li>
        <li>Склонируйте репозиторий проекта на свой компьютер.</li>
            <pre><code>git clone https://github.com/Ashurumaru/forus-chatbot-telegram.git</code></pre>
        <li>Перейдите в корневую директорию проекта.</li>
        <li>Создайте виртуальное окружение для проекта, чтобы изолировать зависимости. Это можно сделать с помощью команды:
    <pre><code>python -m venv venv</code></pre>
</li>
<li>Активируйте виртуальное окружение. Для Windows используйте команду:
    <pre><code>venv\Scripts\activate</code></pre>
    Для macOS и Linux:
    <pre><code>source venv/bin/activate</code></pre>
</li>
        <li>Установите зависимости, запустив команду:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Создайте файл с названием ".env" в корневой директории проекта и добавьте в него свои данные в формате 
            <pre><code>TOKEN=токен бота
DB_HOST=хост
DB_USER=имя пользователя
DB_PASSWORD=пароль 
DB_NAME=имя бд
</code></pre></li>
        На windows можно использовать команду echo
            <pre><code>echo "TOKEN=6518777001:AAGyeaQyHYXMw6VdcAeuj599qels7JyfYjq" "DB_HOST=localhost" "DB_USER=user" "DB_PASSWORD=BIN!KBK7WVdr/)-t" "DB_NAME=chatbottests" > .env</code></pre></li>
        <p>Вставьте свои данные вместо указанного в примере.</p>
        <p>Либо же можно создать и заполнить файл .env через VS Code.</p>
        <li>Бот готов к использованию.</li>
        <pre><code>python main.py</code></pre>
    </ul>
    <h2>Возможные ошибки</h2>
    <p>Ошибка при запуске проекта:</p>
    <pre>File "frozen codecs", line 322, in decode UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte</pre>
    <p>Исправление: Открыть файл .env с помощью VS Code в нижнем правом углу нажать на кодировку, затем выбрать Save with Encoding и выбрать кодировку UTF-8</p>
    <h2>Контакты</h2>
    <li>Автор: <a href="https://github.com/Ashurumaru/">ashuramaru</a></li>
</body>
