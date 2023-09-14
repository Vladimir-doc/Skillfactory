import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import axios from 'axios';
import Main from './components/Main';
import CategoryList from './components/CategoryList';
import Category from './components/Category';
import Recipe from './components/Recipe';
import Header from './components/Header';
import Footer from './components/Footer';
import RecipeSingle from './components/RecipeSingle';
import './App.css';


function App() {
  return (
    <div>
      <Router>
        <div>
          <Header />
          <Routes>
            <Route path="/categories" element={<CategoryList />} />
            <Route path="/categories/:categoryId" element={<Category />} />
            <Route path="/recipes" element={<Recipe />} />
            <Route path="/recipes/:recipeId" element={<RecipeSingle />} />
            <Route path="" element={<Main />} />
          </Routes>
        </div>
        <Footer />
      </Router>
    </div>
  );
}

export default App;