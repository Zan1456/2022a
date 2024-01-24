function osszegzes(lista) {
    var s = 0;
    for(let i = 0; i < lista.length; i++){
        s += lista[i];
    }
    return s;
}

console.log(osszegzes([1, 2, 3, 4, 5]));

function osszeszorzas(lista) {
    var s = lista[0];
    for(let i = 1; i < lista.length; i++){
        s *= lista[i];
    }
    return s;
}

console.log(osszeszorzas([1, 2, 3, 4, 5]));

function megszamlalas(l) {
    let count = 0;

    for (let i = 0; i < l.length; i++) {
        if (l[i] === 0) {
            count++;
        }
    }
     
    return count;
}

console.log(megszamlalas([1, 2, 0, 4, 5]));

function maxkiv(l){
    let max = l[0], index = 0;
    for(let i = 1; i < l.length; i++){
        if(max < l[i]){
            max = l[i];
            index = i;
            }
        }
    return [index, max];
}