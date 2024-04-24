var rubikRekordok = [];
rubikRekordok[2]="Mogyorósi Hunor;0,73";
rubikRekordok[3]="Slezák Gábor;5,65";
rubikRekordok[4]="Novotni Gergely;24,91";
rubikRekordok[5]="Mogyorósi Hunor;49,06";
rubikRekordok[6]="Barát Bence;1:36,67";
rubikRekordok[7]="Barát Bence;2:21,03";

function frissit(meret){
    kmeret.innerHTML=meret+' x '+meret;
    kido.innerHTML=rubikRekordok[meret].split(';')[1] + ' mp';
    knev.innerHTML=rubikRekordok[meret].split(';')[0];
    let kepfajl='rubik-'+meret+'.png';
    document.getElementById("rubik").src = kepfajl;
}
