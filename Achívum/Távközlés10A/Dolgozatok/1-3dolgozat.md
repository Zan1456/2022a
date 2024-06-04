# 1 - 3. fejezet: Alapszintű hálózati kapcsolat és kommunikáció vizsga

> Frissítve 2024.01.05. 0:55

## A kérdések eltérőek lehetnek az enyéimtől. A források oldalon további 42 kérdés található meg. (Fájl alján találod)

## Kérdések

1. Melyik kifejezés írja le azt a modellt, ahol a kiszolgáló szoftver dedikált számítógépeken fut?
- internet
- **kliens/szerver**
- intranet
- extranet

2. Tanulmányozzuk az ábrát! A ServerB kapcsolódni próbál a HostA-hoz. Melyik két állítás írja le helyesen azt a címzést, amelyet a ServerB nevű
eszköz hajt végre? (Két jó válasz van.)
- **A csomag cel IP-cime a HostA lesz.**
- A csomag cel IP-cime a RouterA lesz.
- **A keret cel MAC-cime a RouterB lesz.**
- A csomag cel IP-cime a RouterB lesz.
- A keret cel MAC-cime a SwitchB lesz.
- A keret cel MAC-cime a RouterA lesz.

3. Melyik három alkalmazási rétegbeli protokoll tartozik a TCP/IP-protokollkészlethez? (Három jó válasz van.)
- PPP
- NAT
- ARP
- **DNS**
- **FTP**
- **DHCP**

4. Melyik két OSI-modell réteg rendelkezik összességében azokkal a funkciókkal, mint a TCP/IP-modell egyetlen rétege?(Két jó válasz van.)
- adatkapcsolati
- hálózati
- szállítási
- viszony
- **fizikai**

5. Mi a neve a szállítási réteg PDU-jának?
- **szegmens**
- adat
- csomag
- keret
- bitek

6. A böngésző válasz oldalakat kap egy webkiszolgálótól. A kliens szemszögéből nézve mi a helyes sorrendje a protokolloknak, amelyek a
beérkezés után a kicsomagolást elvégzik?
- **Ethernet, IP, TCP, HTTP**
- HTTP, Ethernet, IP, TCP
- Ethernet, TCP, IP, HTTP
- HTTP, TCP, IP, Ethernet

7. Melyik módszert használhatja két számítógép, annak biztosítására, hogy hirtelen túl nagy mennyiségű adat elküldése esetén se kerüljenek a
csomagok eldobásra?
- **válaszidő túllépés**
- beágyazás
- hozzáférési mód
- atvitelvezerles

8. Melyik állítás írja le pontosan azt a TCP/IP beágyazási folyamatot, amikor a PC adatot küld a hálózatra?
- **A szegmenseket a szallitasi reteg kuldi az internet retegnek.**
- Az adatot az internet réteg küldi a hálózatelérési rétegnek.
- A csomagokat a hálózatelérési réteg küldi a szállítási rétegnek.
- A kereteket a hálózatelérési réteg küldi az internet rétegnek.

9. Melyik állítás helyes a hálózati protokollokra?
- Mind a TCP/IP hálózatelérési rétegében működnek.
- A hálózati protokollok meghatározzák a használható hardver típusát és a beszerelésének módját.
- **Meghatározzák a forrás és cél közti üzenetváltás modjait.**
- Csak távoli hálózatokon levő eszközök üzenetváltásakor van szerepük.

10. 1Ha az IPv4-címzés manuálisan van beállítva egy webkiszolgálón, akkor a konfiguráció melyik tulajdonsága választja szét a cím hálózati és állomás részét?
- DNS-szerver cim
- alapertelmezett atjaro
- DHCP-szerver cim
- **alhálózati maszk**

11. Melyik folyamat során kerül egy PDU egy másik PDU-ba?
- szegmentálás
- átvitelvezérlés
- kódolás
- **beágyazás**

12. Melyik módszer teszi lehetővé egy számítógép számára, hogy megfelelően reagáljon, amikor adatokat kér egy kiszolgálótól, de annak túl sok
időbe telik a válaszadás?
- hozzaferesi mod
- adatfolyam-vezerles
- beágyazás
- **válaszidő túllépés**

13. Egy fiókirodánál dolgozó alkalmazott árajánlatot készít egy ügyfél számára. A munkavállalónak bizalmas árazási információkat kell lekérnie a központi iroda belső szervereiről. Milyen típusú hálózathoz fér hozzá a munkavállaló?
- Internet
- extranet
- **intranet**
- helyi halozat

14. Párosítsuk össze a megbízhatósági követelményeket a hálózati architektúrával! (Nem mindegyik elemet kell felhasználni.)

| Meghatározás | Válasz |
| ----------- | ----------- |
| A hálózat védelme a jogosulatlan hozzáféréstől. | biztonság |
| Redundáns kapcsolatok es eszközök alkalmazása. | hibatűrő képesség |
| A kommunikáció típusokhozzárendelése egy adott prioritáshoz. |  |
| A hálózat bővítése a szolgáltatások elérhetőségének zavarása nélkül. | skálázhatóság |
| Nagy sebességű kapcsolat biztosítása a valós idejű adatforgalom számára. |  |

15. Párosítsuk össze a tulajdonságokat a hozzájuk tartozó internet kapcsolat típusával! (Nem mindegyik elemet kell felhasználni.)

| Meghatározás | Válasz |
| ----------- | ----------- |
| DSL | szélessávú kapcsolat telefonvonalon keresztül |
| betárcsázós telefon | általában nagyon alacsony sávszélességgel rendelkezik |
| műholdas | nem alkalmas sűrű erdős területeken történő használatra |
| kábeles | átviteli közege a koaxiális kábel |

16. Melyik OSI-rétegben kerül a PDU-ba az adat a beágyazási folyamat során?
- hálózati
- szállítási
- **alkalmazási**
- megjelenitesi

17. Tanulmányozza az ábrát! A rendszergazda megpróbál beállításokat végezni egy kapcsolón, de az ábrán látható hibaüzenetet kapja. Mi a
probléma?
```
Switch1> config t
% Invalid input detected at '^' marker.
```
- A rendszergazda már globális konfigurációs módban van.
- A teljes parancs, vagyis a configure terminal használandó.
- **A rendszergazdának először be kell lépnie privilegizált EXEC módba a parancs kiadása előtt.**
- A rendszergazdának konzol porton keresztul kell csatlakozni a globális konfigurációs mód eléréséhez.

18. Miért van szüksége egy 2. rétegbeli kapcsolónak IP-címre?
- A kapcsolónak lehetősége legyen szórásos kereteket küldeni a kapcsolódó PC-knek.
- A kapcsoló alapértelmezett átjáróként üzemelhessen.
- A kapcsoló képes legyen kereteket fogadni a kapcsolódó PC-ktől.
- **A kapcsoló távolról is menedzselhető legyen.**

19. Melyik eszköz feladata annak az útvonalnak a meghatározása, amelyen az üzenetek továbbítódnak a hálózatok között?
- **forgalomiranyito**
- tűzfal
- DSL modem
- webszerver

20. Nyissuk meg a PT-feladatot! Hajtsuk végre a feladat utasításait, majd válaszoljunk a kérdésre! Mi a switch0 eszköz virtuális interfészének (SVI) IP-címe?
- **192.168.5.10**
- 192.168.5.0
- 192.168.10.5
- 192.168.10.1

21. Miután a hálózati rendszergazda elvégezte a konfigurációs módosításokat egy Cisco switch-en, kiad egy *copy running-config startup-config*
parancsot. Mi az eredménye a parancs kiadásának?
- Az új konfiguráció a flash memóriában lesz eltárolva.
- **Az új konfiguráció töltődik be, ha a switch újraindul.**
- Az aktuális IOS-fájl helyére az újonnan konfigurált fájl kerül.
- A konfigurcios változások eltávolításra kerülnek, és helyreall az eredeti konfiguracio.

22. Melyik két állomásnév felel meg a Cisco IOS-eszközökön alkalmazott elnevezési irányelveknek? (Két jó válasz van.)
- Branch2!
- HO Floor 17
- **RM-3-Switch-2A4**
- **SwBranch799**
- Floor(15)

23. Tanulmányozzuk az ábrát! Egy hálózati rendszergazda korlátozni szeretné a hozzáférést SW1 switch-hez.Melyik jelszó szükséges a felhasználói
EXEC mód eléréséhez, ha a rendszergazda konzol kapcsolaton csatlakozik a switch-hez?
![Feladat kép](https://itexamanswers.net/wp-content/uploads/2019/12/CCNA-1-v7-Modules-1-3-Basic-Network-Connectivity-and-Communications-Exam-Answers-14.jpg)
- letmein
- secretin
- **lineconin**
- linevtyin

24. Mi a két jellemzője a RAM-nak egy Cisco eszközben? (Két jó válasz van.)
- **Az eszközön futó aktív konfiguráció a RAM-ban tárolódik.**
- **A RAM tartalma elvesz egy ujrainditas soran.**
- A RAM egy nem felejtő tárolóegység.
- A RAM képes tárolni tobb IOS-változatot és konfigurációs fájlt.
- A RAM Cisco switch-ekben van, viszont routerekben nincs.

25. Egy technikus egy switch konfigurálását végzi ezekkel a parancsokkal: Mit állít be a technikus?
```
SwitchA (config) # interface vlan 1
SwitchA (config-if) # ip address 192.168.1.1 255.255.255.0
SwitchA (config-if) # no shutdown
```
- fizikai kapcsolóport hozzáférés
- jelszó titkosítás
- Telnet hozzaferes
- **SVI**

26. Melyik parancs használható a switch interfészek állapotának és a konfigurált IP-címének ellenőrzésére?
- **show ip interface brief**
- ipconfig
- traceroute
- ping

27. A Cisco IOS részeinek vagy egészének elérése jelszavak segítségével korlátozható. Válassza ki azokat a módokat és interfészeket, amelyek
jelszóval védhetők! (Három jó válasz van.)
- **konzolinterfesz**
- Ethernet interfesz
- forgalomirányító-konfigurációs mód
- **privilegizalt EXEC mod**
- **VTY interfesz**
- IOS mod inditasa

28. Milyen funkciója van az IOS-ben a Tab billentyű megnyomásának egy parancs beírása közben?
- **Kiegészíti a részlegesen begépelt parancsot.**
- Kilép a konfigurációs módból és visszatér felhasználói EXEC módba
- A kurzort a sor elejere mozgatja.
- Megszakítja az aktuális parancsot, és visszatér konfigurációs módba.

29. Melyik parancs vagy billentyűkombináció teszi lehetővé egy felhasználó számára, hogy visszatérjen a menürendszer előző szintjére?
- Ctrl+C
- **exit**
- Ctrl+Z
- end

30. Egy rendszergazda jelszót konfigurál egy switch konzol portjához. Milyen sorrendben halad végig a rendszergazda az IOS-
üzemmódokon, hogy elérje azt a módot, amelyben a konfigurációs parancsokat beirhatja? (Nem mindegyik elemet kell
felhasználni.)

| Meghatározás | Válasz |
| ----------- | ----------- |
| interfész konfigurációs mód |  |
| privilegizált EXEC mód | második mód |
| vonali konfigurációs mód | végső mód |
| globális konfigurácios mod | harmadik mod |
| felhasználói EXEC mód | első mód |

31. Melyik parancs akadályozza meg azt, hogy a titkosítatlan jelszavak a konfigurációs fájlban sima szövegként jelenjenek meg?
- (config)# enable secret Encrypted_Password
- (config)# enable password secret
- (config-line)# password secret
- (config)# enable secret Secret_Password
- **(config)# service password-encryption**

32. Párosítsa ossze a leírasokat a nekik megfelelő parancssori gyorsbillentyűkkel es billentyukombinaciokkal! (Nem mindegyik
elemet kell felhasználni.)

| Meghatározás | Válasz |
| ----------- | ----------- |
| TAB |  |
| szóköz | megjeleníti a következő oldalt |
| felfele nyíl | visszalépked a legutobb kiadott parancsok között |
| Ctrl+C | visszalepked a legutobb kiadott parancsok között |
| ? | környezetérzékeny súgó |
| Ctrl+Shift+6 | megszakitja az olyan parancsokat, mint a traceroute es a ping |

33. Miben különbözik az SSH a Telnettől?
- **Az SSH az üzenetek titkosításával és a felhasználói hitelesítés használatával biztosítja a távoli munkamenetek biztonságát. A Telnet nem biztonságos, mert egyszerű szövegben küldi az üzeneteket.**
- Az SSH-t egy aktív hálózati kapcsolaton keresztül kell konfigurálni, míg a Telnet egy konzol kapcsolaton keresztül csatlakozik az eszközhöz.
- Az SSH a PuTTY terminál emulációs program használatát igényli. A Tera Term szükséges, hogy csatlakozzunk egy eszközökhöz a Telnet használatával.
- Az SSH a hálózaton keresztül csatlakozik, míg a Telnet a sávon kívűli hozzáférésre szolgál.

> Forrás: [itexamanswers.net](https://itexamanswers.net/ccna-1-v7-modules-1-3-basic-network-connectivity-and-communications-exam-answers.html)