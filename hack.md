# Introduction to Networks ( Version 7.00) – Modules 14 – 15 Exam HUN key

| Kérdés | Válasz |
|--------|--------|
| Melyik műveletet hajtja végre az ügyfél, amikor a kiszolgálóval való kommunikációt az UDP használatával a szállítási rétegben hozza létre? | Az ügyfél véletlenszerűen választ egy forrásport számot. |
| Melyik szállítási réteg jellemzője garantálja a munkamenet létrehozását? | TCP 3-lépéses kézfogás (3-way handshake) |
| Mi a jól ismert TCP és UDP portok teljes skálája? | 0-tól 1023-ig |
| Mi az az aljzat/foglalat/socket? | A forrás IP-cím és portszám vagy a cél IP-cím és portszám kombinációja. |
| Egy számítógép nagyméretű fájlt tölt le egy szerverről. A TCP-ablak 1000 bájt. A kiszolgáló 100 bájtos szegmensekkel küldi a fájlt. Hány szegmenst küld a szerver, mielőtt visszaigazolást kér a PC-től? | 10 szegmens |
| Melyik tényező határozza meg a TCP-ablak méretét? | A célállomás által egyszerre feldolgozható adatmennyiség |
| Mit tesz egy ügyfél, ha UDP-adatcsomagokat kell küldenie? | Csak elküldi az adatcsomagokat/datagrams. |
| Melyik három mezőt használja az UDP szegmensfejléc? | Hosszúság (Length), Forrás Port (Source Port), Ellenőrző összeg (Checksum) |
| Mi a szállítási réteg két szerepe a hálózati adatkommunikációban? | A megfelelő alkalmazás azonosítása minden egyes kommunikációs folyamhoz; A forrás- és célállomáson lévő alkalmazások közötti egyedi kommunikáció nyomon követése. |
| Milyen információt használ a TCP a fogadott szegmensek újrarendezéséhez és újrarendezéséhez? | Sorszámok/sequence numbers |
| Milyen fontos információ kerül a TCP/IP szállítási réteg fejlécébe a távoli hálózati eszközzel való kommunikáció és kapcsolódás biztosítása érdekében? | Cél- és forrásport számok |
| Melyik két jellemző tartozik az UDP munkamenetekhez? | A céleszközök minimális késleltetéssel fogadják a forgalmat; A fogadott adatok vissza nem igazoltak/nem nyugtázták. |
| Egy ügyfélalkalmazásnak meg kell szüntetnie egy TCP-kommunikációs munkamenetet egy kiszolgálóval. Helyezze a befejezési folyamat lépéseit az előfordulásuk sorrendjébe. | 1. A kliens elküldi az FIN üzenetet; 2. A szerver elküldi az ACK üzenetet; 3. A szerver elküldi az FIN üzenetet; 4. A kliens elküldi az ACK üzenetet. |
| A TCP fejlécben lévő melyik jelzőt használják válaszul a kapott FIN-re, hogy megszüntessék a kapcsolatot két hálózati eszköz között? | ACK (acknowledgement) |
| Melyik protokoll vagy szolgáltatás használja az UDP-t az ügyfél-kiszolgáló közötti kommunikációhoz és a TCP-t a kiszolgáló-kiszolgáló közötti kommunikációhoz? | DNS |
| Mi az UDP egyik jellemzője? | Az UDP a fogadott adatcsomagokat a fogadás sorrendjében rakja össze újra. |
| Milyen portot kell kérni az IANA-tól ahhoz, hogy egy adott alkalmazással használható legyen? | Regisztrált/bejegyzett port |
| Melyik három alkalmazási réteg protokoll használja a TCP-t? | SMTP, FTP, HTTP |
| Melyik három állítás jellemzi az UDP-t? | 1. Az UDP alapvető kapcsolat nélküli szállítási rétegfunkciókat biztosít; 2. Az UDP az alkalmazási réteg protokolljaira támaszkodik a hibák észlelésében; 3. Az UDP egy alacsony terhelési költségű protokoll, amely nem biztosít szekvencia- vagy folyamszabályozási mechanizmusokat. |
| Melyik két mező szerepel a TCP fejlécben, de az UDP fejlécben nem? | Ablak (window), Sorszám (sequence number) |
| A TCP fejléc melyik mezője jelzi a háromirányú kézfogadási folyamat állapotát? | Vezérlőbitek/ellenőrző bitek (control bits) |
| Miért használja a HTTP a TCP-t szállítási réteg protokollként? | Mert a HTTP megbízható kézbesítést/szállítást igényel. |
| Melyik két alkalmazástípus alkalmas a legjobban az UDP használatára? | Olyan alkalmazások, amelyek maguk kezelik a megbízhatóságot; Olyan alkalmazások, amelyek elviselnek némi adatvesztést, de kevés vagy semmilyen késleltetést nem igényelnek. |
| Hogyan használják a portszámokat a TCP/IP-kapszulázási folyamatban? | Ha több olyan beszélgetés is előfordul, amely ugyanazt a szolgáltatást használja, a forrásport száma a különálló beszélgetések nyomon követésére szolgál. |
| Milyen két helyzetben lenne jobb az UDP, mint a TCP, mint a preferált szállítási protokoll? | Ha gyorsabb szállítási mechanizmusra van szükség; Amikor az alkalmazásoknak nem kell garantálniuk az adatok kézbesítését. |
| Mi a szállítási réteg három feladata? | 1. Az alkalmazások megbízhatósági követelményeinek való megfelelés; 2. Több felhasználó vagy alkalmazás több kommunikációs folyamának multiplexelése ugyanazon a hálózaton; 3. Azon alkalmazások és szolgáltatások azonosítása, amelyeknek a továbbított adatokat kezelniük kell. |
| Melyik három állítás jellemzi a DHCP Discover/felfedezés üzenetet? | 1. A cél IP-cím 255.255.255.255; 2. Az üzenet egy IP-címet kereső ügyféltől érkezik; 3. Minden állomás megkapja az üzenetet, de csak egy DHCP-kiszolgáló válaszol. |
| Melyik két protokollt használhatják az eszközök az e-mailt küldő alkalmazásban? | SMTP, DNS |
| Mi igaz a Server Message Block/SMB protokollra? | Az ügyfelek hosszú távú kapcsolatot hoznak létre a kiszolgálókkal. |
| Mi a HTTP GET üzenet funkciója? | HTML oldal kérése egy webkiszolgálótól. |
| Melyik OSI réteg biztosítja az interfészt a kommunikációra használt alkalmazások és a mögöttes hálózat között, amelyen keresztül az üzeneteket továbbítják? | Alkalmazási réteg (application layer). |
| Milyen hálózati modellt használnak, amikor egy szerző egy fejezet dokumentumát feltölti egy könyvkiadó fájlszerverére? | Ügyfél (kliens)/kiszolgáló (szerver). |
| Mi a közös a kliens/szerver és a peer-to-peer hálózati modellekben? | Mindkét modell támogatja a kiszolgáló és az ügyfél szerepkörben lévő eszközöket. |
| Milyen hálózati modellben használnák az eDonkey-t, az eMule-t, a BitTorrentet, a Bitcoint és a LionShare-t? | Peer-to-peer/egyenrangú. |
| Milyen közös protokollt használnak az olyan peer-to-peer alkalmazások, mint a WireShare, a Bearshare és a Shareaza? | Gnutella. |
| Mi a peer-to-peer hálózati modell egyik legfontosabb jellemzője? | Erőforrás-megosztás dedikált szerver nélkül. |
| A TCP/IP modell alkalmazási rétege az OSI-modell melyik három rétegének funkcióit látja el? | Munkamenet (viszonylati)/session, Bemutató (megjelenítési)/presentation, Alkalmazási/application. |
| Mi a példa a kliens-szerver modellt használó hálózati kommunikációra? | A munkaállomás DNS-kérést kezdeményez, amikor a felhasználó beírja a www.cisco.com címet a webböngésző címsorába. |
| A TCP/IP modell melyik rétegét használják az adatok formázására, tömörítésére és titkosítására? | Alkalmazási réteg (application). |
| Mi az SMB előnye az FTP-vel szemben? | Az SMB-ügyfelek hosszú távú kapcsolatot létesíthetnek a kiszolgálóval. |
| Egy gyártó vállalat előfizet bizonyos hosztolt szolgáltatásokra az internetszolgáltatójától. Az igényelt szolgáltatások közé tartozik a világháló, a fájlátvitel és az e-mail. Mely protokollok képviselik ezt a három kulcsfontosságú alkalmazást? | FTP, HTTP, SMTP. |
| Melyik alkalmazási réteg protokoll használ olyan üzenettípusokat, mint a GET, PUT és POST? | HTTP. |
| Milyen típusú információkat tartalmaz egy DNS MX rekord? | A mail exchange szerverekhez hozzárendelt tartománynév. |
| Melyik három protokoll működik a TCP/IP modell alkalmazási rétegén? | FTP, POP3, DHCP. |
| Melyik protokollt használja az ügyfél a webkiszolgálóval való biztonságos kommunikációra? | HTTPS. |
| Mely alkalmazások vagy szolgáltatások teszik lehetővé, hogy a hosztok egyidejűleg ügyfélként és kiszolgálóként is működjenek? | P2P/Peer-to-Peer alkalmazások. |
| Mi a peer-to-peer hálózatok két jellemzője? | Decentralizált erőforrások, erőforrás-megosztás dedikált szerver nélkül. |
| Melyik forgatókönyv írja le a szállítási réteg által biztosított funkciót? | Egy diák két webböngészőablakot nyit meg, hogy két weboldalt érjen el. A szállítási réteg biztosítja, hogy a megfelelő weboldalt a megfelelő böngészőablakba juttassa el. |
| Az OSI-modell melyik három rétege nyújt hasonló hálózati szolgáltatásokat, mint a TCP/IP-modell alkalmazási rétege? | Munkamenet (viszonylati)/session, Bemutató (megjelenítési)/presentation, Alkalmazási/application. |
| A webkiszolgálóval kommunikáló számítógép TCP-ablakmérete adatküldéskor 6000 bájt, csomagmérete pedig 1500 bájt. Melyik bájt információt fogja a webkiszolgáló nyugtázni, miután két adatcsomagot kapott a PC-től? | 3001. |
| A webkiszolgálóval kommunikáló számítógép TCP-ablakmérete adatküldéskor 6000 bájt, csomagmérete pedig 1500 bájt. Melyik bájt információt fogja a webkiszolgáló nyugtázni, miután három adatcsomagot kapott a PC-től? | 4501. |
| A webkiszolgálóval kommunikáló számítógép TCP-ablakmérete adatküldéskor 6000 bájt, csomagmérete pedig 1500 bájt. Melyik bájt információt fogja a webkiszolgáló nyugtázni, miután négy adatcsomagot kapott a PC-től? | 6001. |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél TFTP szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 69. |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél FTP szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 21 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél SSH szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 22 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél HTTP szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 80 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél POP3 szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 110 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél telnet szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 23 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél SNMP szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 161 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél SMTP szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 25 |
| Az ügyfél létrehoz egy csomagot, amelyet elküld a kiszolgálónak. Az ügyfél HTTPS szolgáltatást kér. Milyen számot fog használni a célport számaként a küldő csomagban? | 443 |
