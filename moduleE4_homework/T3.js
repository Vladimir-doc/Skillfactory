// Задание 3. Написать функцию, которая создает пустой объект, но без прототипа.

function someObject(){
    return Object.create(null);
   }
   console.log (someObject());