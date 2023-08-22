import React, { useState } from 'react';

const GeolocationDetector = ({ onLocationDetected, API_BASE_URL, API_KEY }) => {
  const [loading, setLoading] = useState(false);

  const handleDetectLocation = () => {
    setLoading(true);
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          fetch(`${API_BASE_URL}/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${API_KEY}`)
            .then(response => response.json())
            .then(data => {
              if (window.confirm(`Ваш город ${data.name}, верно?`)) {
                onLocationDetected(data.name);
              }
            })
            .catch(error => {
              console.error("Error fetching weather data:", error);
            });
        },
        (error) => {
          console.error("Error getting current position:", error);
          alert("Невозможно определить Ваше местоположение. Пожалуйста, выберете город из списка.");
        }
      );
    } else {
      console.error("Geolocation is not available in this browser.");
      alert("Ваш браузер не поддерживает определение местоположения. Пожалуйста, выберете город из списка.");
    }
    setLoading(false);
  };

  return (
    <div className="nav">
      <button onClick={handleDetectLocation} disabled={loading}>
        {loading ? "Определение..." : "Определить Ваш город"}
      </button>
    </div>
  );
};

export default GeolocationDetector;
