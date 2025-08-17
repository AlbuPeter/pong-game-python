📝 Pong játék – Magyar nyelvű dokumentáció
1. Előkészületek
  1.1 Python letöltése és telepítése Microsoft Store-ból
  
    Nyisd meg a Microsoft Store alkalmazást a gépeden.
    
    Keresd meg: Python 3.12 (vagy a legfrissebb elérhető verziót).
    
    Kattints az Install gombra.
    
    Ez automatikusan telepíti a Pythont és a pip csomagkezelőt, és hozzáadja a rendszerhez (PATH beállítás nem kell külön).
  
  1.2 Ellenőrzés
  
    Nyiss egy Parancssort (cmd), és írd be:
    
      python --version
  
  
    Ha kiírja a verziót (pl. Python 3.12.3), akkor sikerült.
  
  1.3 pygame telepítése
  
    A Pong játékhoz szükség van a pygame könyvtárra. Telepítsd így:
    
      python -m pip install pygame
  
  
    Ha nem kapsz hibát, akkor a pygame készen áll.

2. Pong játék forráskódja

  A játék kódja a GitHubon érhető el, egy pong.py nevű fájlban.
  Töltsd le vagy másold a saját gépedre, és mentsd el egy tetszőleges mappába.

3. A játék futtatása

  Nyiss egy parancssort abban a mappában, ahová a pong.py fájlt elmentetted.
  Példa:
  
    cd <a mappa elérési útja>
  
  
  Indítsd el a programot:
  
    python pong.py

4. Játék irányítása

  Bal játékos:
  
    W → felfelé
    
    S → lefelé
  
  Jobb játékos:
  
    ↑ → felfelé
    
    ↓ → lefelé
  
  A pontszám megjelenik a képernyő tetején. Amikor a labda átmegy valamelyik oldalon, a másik játékos kap pontot.

✅ Ezzel készen van a teljes játékod!
