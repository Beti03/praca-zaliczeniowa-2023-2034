import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Search_Locators, Products_Locators, MainPageLocators, MessagePageLocators
"""
informacje dodatkowe na karcie produktu
Czy widoczna jest zakładka "Opis produktu" a w niej opis
Czy widoczna jest zakładka "Informacje dodatkow" a w niej opis
Czy widoczna jest zakładka "Recenzja":
    - walidacja formularza wszystkie pola nie uzupełnione, powinien wyświetlić się komunikacj to błędach
Czy widoczna jest zakładka "Tagi produktu":
    - dodanie taga i kliknięcie Dodaj tagi, po kliknięciu zostanie użytkownik przeniesionyc na stronę logowanie
    Założenie: Nie zalogowany użytkownik nie może dodać taga
Czy widoczna jest zakładka "Dodatkow opcje znakowe": a nie opis - nagłówek
"""
