import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Header() {
  return (
    <div className="header">
      <nav className="nav-container">
        <Link to="/" className="logo-link">
          <img
            src="https://phonoteka.org/uploads/posts/2021-05/1621911833_22-phonoteka_org-p-detskie-foni-yeda-22.jpg"
            alt="Лого"
            className="logo"
          />
        </Link>
        <ul className="nav-list">
          <li>
            <Link to="/" className="nav-link">Главная</Link>
          </li>
          <li>
            <Link to="/categories" className="nav-link">Категории</Link>
          </li>
          <li>
            <Link to="/recipes" className="nav-link">Рецепты</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Header;
