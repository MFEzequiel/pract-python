const d = s => console.log(s);

let ar = 0.7
let ap = 1.6
let ac = 3

function condi(n, t) {

    if (n >= 0.6 && n < 1) {
         
        d(`${t} Chocolate $0.6`);
        d(`${t} Cambio ${n - 0.4}`);

    }else if (n >= 1 && n < 1.7) {

        d(`${t} Vainilla $1 o de Dlce d lche $1.6`);
        d(`${t} Cambio ${n - 0.6}`);

    }else if (n >= 2) {

        d(`${t} Frutilla $2`);
        d(`${t} Cambio ${n - 2}`);
    
    } else if (n < 0.6) {
        d(`${t} No tienes dinero suficiente`)
    }
};


condi(ar, "ar")
condi(ap, "ap")
condi(ac, "ac")