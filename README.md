<body>
    <h1>Задачи chatbots</h1>
    <h2>Описание</h2>
    <p>Данный проект был разработан в рамках получения компетенций на сайте <a href="https://students.forus.ru/">Октагон</a>. Разработано с использованием языка программирования python.</p>
      <h2>Технологии и Инструменты</h2>
    <ul>
        <li><strong>Python:</strong> Проект создан с использованием языка программирования python.</li>
        <li><strong>Библиотека python-telegram-bot:</strong> Используется для разработки телеграм бота</li>
    </ul>
      <h2>Инструкция</h2>
    <ul>
        <li>Установите Python, если он еще не установлен. Можно скачать с <a href="https://www.python.org/downloads/">официального сайта Python</a>.(для проекта был использован python 3.11)</li>
        <li>Склонируйте репозиторий проекта на свой компьютер.</li>
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
        <li>Создайте файл с названием ".env" в корневой директории проекта и добавьте в него свой токен Telegram Bot API в формате 
            <pre><code>TOKEN=токен_бота</code></pre></li>
        На windows можно использовать команду echo
            <pre><code>echo TOKEN=6518777001:AAGyeaQyHYXMw6VdcAeuj599qels7JyfYjq > .env</code></pre></li>
        Вставьте свой токен бота вместо указанного в примере.
        <li>Бот готов к использованию.</li>
        <pre><code>python main.py</code></pre></li>
    </ul>
    <h2>Контакты</h2>
    <li>Автор: <a href="https://github.com/Ashurumaru/">ashuramaru</a></li>
</body>
