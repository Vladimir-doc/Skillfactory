/*Задание 2. Написать функцию, которая принимает в качестве аргументов строку и объект,
 а затем проверяет есть ли у переданного объекта свойство с данным именем. 
 Функция должна возвращать true или false. */


 let user = {
    name: 'Alex',
    city: 'Moscow',
   };

let answer = sometest('name', user)

function sometest(str, obj) {
	if (obj.hasOwnProperty(str)) {
        return true;
    }   
    return false;
}

console.log(answer);