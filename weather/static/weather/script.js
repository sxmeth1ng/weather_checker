document.getElementById("weatherForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const city = document.getElementById("cityInput").value;
    const resultDiv = document.getElementById("weatherResult");
    resultDiv.innerHTML = "<div class='loading'>Ищем погоду...</div>";

    try {
        const response = await fetch("/api/weather/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            },
            body: JSON.stringify({ city }),
        });

        const data = await response.json();
        if (!response.ok) {
            resultDiv.innerHTML = `<div class="error">${data.error}</div>`;
            return;
        }

        const current = data.current_weather;
        resultDiv.innerHTML = `
            <div class="weather-card">
                <h2>${data.city}</h2>
                <p>🌡️ ${current.temperature}°C</p>
                <p>💨 ${current.windspeed} м/с</p>
                <p>Влажность: ${data.hourly.relativehumidity_2m[0]}%</p>
            </div>
        `;
    } catch (error) {
        resultDiv.innerHTML = "<div class='error'>Ошибка сервера</div>";
    }
});