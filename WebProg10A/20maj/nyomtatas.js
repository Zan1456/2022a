function kalkulal(){
    //Űrlapadatok
    const szelesseg=297;
    const magassag=420;
    const papir=document.getElementById('papirtipus').value;
    //Számítások
    let terulet=Math.round((szelesseg*magassag)/10000);    
    let koltseg=terulet*papir;
    //Megjelenítés
    document.getElementById('terulet').textContent = terulet;
    document.getElementById('papir').textContent = papir;
    document.getElementById('koltseg').textContent = koltseg;
    document.getElementById('valasz').style.visibility = "visible";
}