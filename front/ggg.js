// Обработчик формы
document.getElementById('login-form').addEventListener('submit', async(e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;

    // Отправляем на ТВОЙ контроллер
    const response = await fetch('http://127.0.0.1:8005/auth/user', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username })
    });

    const user = await response.json();

    if (user) {
        alert(`Привет, ${user.username}!`);
        // Тут можно сохранить user.id для дальнейших запросов
    }
});