from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    # Здесь должна быть логика для аутентификации пользователя
    if username == 'user' and password == 'password':  # Пример проверки
       
    if username == 'user' and password == 'password':  # Пример проверки
        return "Успешный вход!"  # Здесь может быть перенаправление на главную страницу приложения
    else:
        return "Неверное имя пользователя или пароль", 401

if __name__ == '__main__':
    app.run(debug=True)
