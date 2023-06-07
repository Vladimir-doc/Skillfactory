// Задание 5. Переписать консольное приложение из предыдущего юнита на классы.

class Appliances {
    constructor(name) {
        this.name = name;
    }
}

Appliances.prototype.AppliancesConnected = function () {
    let connect = false
    if (this.connected) {
        connect = true;
        } else {
        connect = false;
        }
       return (connect);
       }

class Appliance extends Appliances {
    constructor (name, power, connected, powerCheck){
    super(name);
    this.power = power;
    this.connected = connected;
    this.powerCheck = function(){
        console.log(power)
        }
    } 
}

Appliance.prototype = new Appliances();

let AllPowerConnected = function (){
    let sum = 0;
    for(let val of allAppliances){
    if (val.AppliancesConnected()){
        sum += val.power;
    } else{
        sum;
     }
    }
    return sum;
}
  
  const lamp = new Appliance(name = "lamp", power = 60, connected = true);
  const laptop = new Appliance(name = "laptop", power = 450, connected = true);
  let allAppliances = [lamp, laptop];
  
  console.log(`ноутбук подключен к сети? -> ${laptop.AppliancesConnected()}`);
  console.log(`лампа подключена к сети? -> ${lamp.AppliancesConnected()}`);
  console.log(`Общая мощность приборов подкюченных к сети составляет: ${AllPowerConnected(allAppliances)} Вт`);
  lamp.powerCheck();
  laptop.powerCheck();