// api.js
export const API_KEY = 'a9bdbf8cfc956a8eb8ee096e8c5cb05b'; // Вставьте свой ключ
export const API_BASE_URL = 'https://api.openweathermap.org/data/2.5';

export const fetchWeatherData = async (city) => {
  const response = await fetch(`${API_BASE_URL}/weather?q=${city}&units=metric&appid=${API_KEY}`);
  const data = await response.json();
  return data;
};

export const fetchForecastData = async (city) => {
  const response = await fetch(`${API_BASE_URL}/forecast?q=${city}&units=metric&appid=${API_KEY}`);
  const data = await response.json();
  return data;
};
