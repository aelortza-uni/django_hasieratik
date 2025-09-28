# Django Hasieratik 🚀

Tutorial honetan, Django erabiliz zure lehen web aplikazioa nola sortu
ikasiko duzu. Oinarrizko pauso guztiak jasotzen ditu: instalazioa,
proiektua sortzea, aplikazioak gehitzea, bistak eta URL-ak definitzea,
modeloak eta datu-basearekin lan egitea, shell-a erabiltzea,
administrazio-panela, txantiloiak, CRUD eragiketak eta fitxategi
estatikoak.

## 📂 Edukia

-   **Ingurunearen prestaketa**: Python, PIP, VSCode eta ingurune
    birtuala.
-   **Lehen proiektua**: Django instalatu eta `startproject` komandoa.
-   **Aplikazioak**: `startapp`, aplikazioak erregistratzea.
-   **Bistak eta URL-ak**: lehen "Hello World", URL routing.
-   **Modeloak eta migrazioak**: datu-basearen diseinua eta aldaketak
    aplikatzea.
-   **Django Shell**: datuak sortu, irakurri, eguneratu eta ezabatu.
-   **Administrazio-panela**: supererabiltzailea eta modeloak admin-era
    gehitzea.
-   **Parametroak URLetan**: `path()` eta `get_object_or_404`.
-   **Txantiloiak eta herentzia**: HTML dinamikoa eta `base.html`.
-   **Formularioak eta CRUD**: `CreateView`, `UpdateView`, `DeleteView`.
-   **Fitxategi estatikoak**: CSS, JS eta irudiak kudeatzea.

## 💻 Exekutatzeko

1.  Klona ezazu repositorioa:

    ``` bash
    git clone https://github.com/<zure-erabiltzailea>/<zure-repoa>.git
    cd <zure-repoa>
    ```

2.  Sortu eta aktibatu ingurune birtuala:

    ``` bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    .\venv\Scripts\activate    # Windows
    ```

3.  Instalatu beharrezko paketeak:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Migrazioak aplikatu eta zerbitzaria abiarazi:

    ``` bash
    python manage.py migrate
    python manage.py runserver
    ```

5.  Nabigatzailean ireki:

        http://127.0.0.1:8000/

## 🛠 Teknologiak

-   Python 3
-   Django
-   SQLite (defektuzko datu-basea)
-   HTML, CSS, JS

## 📜 Lizentzia

Proiektu hau MIT lizentziapean banatzen da.\
Ikasi, erabili eta partekatu libreki!
