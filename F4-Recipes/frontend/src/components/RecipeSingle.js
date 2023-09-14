import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';



const API_BASE_URL = 'http://localhost:8000';

function RecipeSingle() {

  const { recipeId } = useParams();
  const [recipe, setRecipe] = useState(null);
  const [categoryName, setCategoryName] = useState('');

  useEffect(() => {
    const fetchRecipe = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/recipes/${recipeId}/`);
        setRecipe(response.data);
        const categoryResponse = await axios.get(`${API_BASE_URL}/categories/${response.data.category}/`);
        setCategoryName(categoryResponse.data.name);
      } catch (error) {
        console.error(error);
      }
    };

    fetchRecipe();
  }, [recipeId]);

  if (!recipe) {
    return <div>Упс!Что-то пошло не так...</div>;
  }

  return (
    <div>
      <h2 className='text-with-shadow'>Название: {recipe.title}</h2>
      <h3 className='text-with-shadow'>Категория:    
      <Link to={`/categories/${recipe.category}`}> {categoryName}</Link></h3>
     <h3 className='text-with-shadow'>Ингридиенты:</h3> <p>{recipe.ingredients}</p>
     <h3 className='text-with-shadow'>Инструкция:</h3><p>{recipe.manual}</p>
    </div>
  );
}

export default RecipeSingle;
