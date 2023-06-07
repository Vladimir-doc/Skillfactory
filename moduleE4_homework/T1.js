/* Задание 1. Написать, функцию, которая принимает в качестве аргумента объект 
и выводит в консоль все ключи и значения только собственных свойств. 
Данная функция не должна возвращать значение.*/

const something = {a:123, b: "word"};

function keysValues(obj) {
    for (let key in obj) {
        if (obj.hasOwnProperty(key)){
            console.log(key, obj[key]);
        }
    }
}

keysValues(something);