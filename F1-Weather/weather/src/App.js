import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header';
import CitySelector from './components/CitySelector';
import CurrentWeather from './components/CurrentWeather';
import Forecast from './components/Forecast';
import Footer from './components/Footer';
import { fetchWeatherData, fetchForecastData, API_BASE_URL, API_KEY } from './api';
import GeolocationDetector from './components/GeolocationDetector';

const cityList = [
  'Москва', 'Санкт-Петербург', 'Петрозаводск', 'Омск', 'Воронеж',
  'Симферополь', 'Краснодар', 'Тверь', 'Калининград'
];

function App() {
  const [selectedCity, setSelectedCity] = useState('');
  const [weatherData, setWeatherData] = useState(null);
  const [forecastData, setForecastData] = useState(null);

  useEffect(() => {
    if (selectedCity) {
      fetchWeatherData(selectedCity).then(data => setWeatherData(data));
      fetchForecastData(selectedCity).then(data => setForecastData(data));
    }
  }, [selectedCity]);

  const handleCityChange = (event) => {
    setSelectedCity(event.target.value);
  };

  const handleGeolocationDetected = (detectedCity) => {
    setSelectedCity(detectedCity);
  };

  return (
    <div className="App">
      <Header />
      <div className="nav">
        <CitySelector 
          selectedCity={selectedCity}
          handleCityChange={handleCityChange}
          cityList={cityList}
        />
        <GeolocationDetector 
          onLocationDetected={handleGeolocationDetected}
          API_BASE_URL={API_BASE_URL}
          API_KEY={API_KEY}
        />
      </div>
      <div className="main">
        <CurrentWeather weatherData={weatherData} />
        <Forecast forecastData={forecastData} />
      </div>
      <Footer />
    </div>
  );
}

export default App;
