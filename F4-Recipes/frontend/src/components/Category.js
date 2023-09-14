// import React, { useState, useEffect } from 'react';
// import { useParams, Link } from 'react-router-dom';
// import axios from 'axios';
// import './Category.css';

// const API_BASE_URL = 'http://localhost:8000';

// function Category() {
//   const { categoryId } = useParams();
//   const [recipes, setRecipes] = useState([]);
//   const [categoryName, setCategoryName] = useState('');

//   useEffect(() => {
//     const fetchRecipesByCategory = async () => {
//       try {
//         const response = await axios.get(`${API_BASE_URL}/categories/${categoryId}/recipes/`);
//         setRecipes(response.data);
//       } catch (error) {
//         console.error('Error fetching recipes:', error);
//       }
//     };

//     const fetchCategoryName = async () => {
//       try {
//         const response = await axios.get(`${API_BASE_URL}/categories/${categoryId}/`);
//         setCategoryName(response.data.name);
//       } catch (error) {
//         console.error('Error fetching category name:', error);
//       }
//     };

//     fetchRecipesByCategory();
//     fetchCategoryName();
//   }, [categoryId]);
  

//   return (
//     <div>
//       <h2 className='text-with-shadow'>Рецепты в категории: {categoryName}</h2>
//       <ul>
//         {recipes.map(recipe => (
//         <li key={recipe.id}>
//             <Link to={`/recipes/${recipe.id}`}>{recipe.name}</Link>
//         </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default Category;


import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import './Category.css';

const API_BASE_URL = 'http://localhost:8000';

function Category() {
  const { categoryId } = useParams();
  const [category, setCategory] = useState([]);
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    const fetchRecipesByCategory = async () => {
      try {
        // Запрос для получения данных о категории
        const categoryResponse = await axios.get(`${API_BASE_URL}/categories/${categoryId}/`);
        setCategory(categoryResponse.data);

        // Запрос для получения рецептов в данной категории
        const recipesResponse = await axios.get(`${API_BASE_URL}/categories/${categoryId}/recipes/`);
        setRecipes(recipesResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
     
    };

    fetchRecipesByCategory();
  }, [categoryId]);

  return (
    <div>
      <h2 className='text-with-shadow'>Рецепты в категории: {category.name}</h2>
      <ul>
        {recipes.map(recipe => (
          <li key={recipe.id}>
            <Link to={`/recipes/${recipe.id}`}>{recipe.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Category;
