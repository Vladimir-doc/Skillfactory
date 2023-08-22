import React from "react";

const Main = ({ weatherData, forecastData }) => {
    // вычисляем среднюю температуру по дню
  const calculateAverageTemperature = (temperatures) => {
    const sum = temperatures.reduce((total, temp) => total + temp, 0);
    return sum / temperatures.length;
  };

  const dailyAverages = {};

  if (forecastData) {
    forecastData.list.forEach((forecast) => {
      const date = new Date(forecast.dt * 1000).toLocaleDateString();
      const temperature = forecast.main.temp;

      if (!dailyAverages[date]) {
        dailyAverages[date] = [];
      }

      dailyAverages[date].push(temperature);
    });
  }

  return (
    <div className="main">
          {weatherData && (
            <div className="currentweather">
                <h2>Сейчас в {weatherData.name}</h2>
                <p>Температура: {weatherData.main.temp} °C</p>
            </div>
      )}
      {forecastData && (
        <div className="forecastweather">
          <h2>Прогноз на 5 дней в {forecastData.city.name}</h2>
          {Object.keys(dailyAverages).map((date) => (
            <p key={date}>
              {date}: {calculateAverageTemperature(dailyAverages[date]).toFixed(2)} °C
            </p>
          ))}
        </div>
      )}
    </div>
  );
};

export default Main;
