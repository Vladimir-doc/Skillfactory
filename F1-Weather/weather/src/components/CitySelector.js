import React from 'react';

const CitySelector = ({ selectedCity, handleCityChange, cityList }) => {
  return (
    <div className="nav">
      {/* <button onClick={handleAutoDetectCity}>Определить Ваш город</button> */}
      <select value={selectedCity} onChange={handleCityChange}>
        <option value="">Выбрать город</option>
        {cityList.map((city) => (
          <option key={city} value={city}>
            {city}
          </option>
        ))}
      </select>
    </div>
  );
}

export default CitySelector;
