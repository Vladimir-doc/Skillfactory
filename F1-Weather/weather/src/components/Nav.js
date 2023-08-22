import React from "react";


const Nav = ({ handleDetectLocation, selectedCity, handleCityChange, cityList }) => {
    return (
        <div className="nav">
             <button onClick={handleDetectLocation} disabled={loading}>
                {loading ? "Определение..." : "Определить Ваш город"}
            </button>
            <select value={selectedCity} onChange={handleCityChange}>
            <option value="">Выбрать город</option>
                {cityList.map((city) => (
                <option key={city} value={city}>
                {city}
                </option>
                ))}
            </select>
        </div>
    )
}

export default Nav;