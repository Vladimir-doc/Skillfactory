import React from 'react';

const CurrentWeather = ({ weatherData }) => {
  return (
    <div className="currentweather">
      {weatherData && weatherData.name && (
        <>
          <h2>Сейчас в {weatherData.name}</h2>
          <p>Температура: {weatherData.main.temp} °C</p>
        </>
      )}
    </div>
  );
};

export default CurrentWeather;
