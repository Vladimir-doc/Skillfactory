import React from 'react';

const Forecast = ({ forecastData }) => {
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
    <div className="forecastweather">
      {forecastData && forecastData.city && (
        <>
          <h2>Прогноз на 5 дней в {forecastData.city.name}</h2>
          {Object.keys(dailyAverages).map((date) => (
            <p key={date}>
              {date}: {calculateAverageTemperature(dailyAverages[date]).toFixed(2)} °C
            </p>
          ))}
        </>
      )}
    </div>
  );
};

export default Forecast;

