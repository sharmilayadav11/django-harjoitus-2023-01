# django-harjoitus-2023-01
Django-harjoittelua 2023-01

#Asennus

1. Tee Python. virturaaliymparisto
    python -m venv venv

2. Aktivoi virtualiympäristö
- Voit tehdä tämän VSCodessa, joko vastaamalla Yes kun VSCode kysyy että aktivoidaanko virtuaaliympäristö tai jos tätä kysymystä ei tule, niin klikkaamalla versionumeroa Python-sanan vierestä alapalkista. Python-sana tulee alapalkkiin, kun avaat jonkin py-tiedoston (esim. manage.py).

-Vaihtoehtoisesti voit ajaa Linuxissa . venv/bin/activate tai Windowsissa venv\script\activate.ps1
-Kun virtuaaliympäristö on aktiivinen, niin terminaalissa lukee rivin alussa (venv)

3. Asenna tarvittavat Python-paketit
    pip install -r requirements.txt

4. Aja migraatiot tietokantaan:
'sh
    python manage.py migrate

    -Tämä luo SQLite-tietokannan db.sqlite3-tiedostoon

5. Luo pääkäyttäjä:
    'sh
    python manage.py createsuperuser

    -Käytä käyttäjätunnusta ja salasanaa, jotka muistat helposti. Esim. "admin" ja "admin".