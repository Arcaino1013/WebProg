<?php

/* Fehlt hier vielleicht auch etwas? */

class ShopEngine {

  /* Überlegen Sie sich, welche privaten oder öffentlichen Membervariablen Ihre Klasse braucht. */

  public function __construct() {
    /* Initialisieren Sie hier die Datenbankverbindung und ggf. das Session-Management */
    /* Achten Sie dabei auf korrekte Fehlerbehandlung! */
    /* HINWEISE:

       - Verwenden Sie ausschliesslich PHP Data Objects (PDO) für den Datenbankzugriff.
       - Verwenden Sie ausschliesslich die globalen Konstanten DB_DSN, DB_USER und DB_PASS aus
         der config.php, um die Verbindung zur Datenbank herzustellen!

    */
  }

  public function generateArticleTable() {

    /*
      Hier erzeugen Sie die Artikelübersicht. Der Rückgabewert der Funktion ist eine Zeichenkette,
      die die einzelnen Tabellenzeilen enthält. Vergleichen Sie Ihr Ergebnis mit der Beispielimplementierung.
    */

  }

  public function numberOfItemsInCart() {
    /* Diese Funkion gibt die Anzahl der Elemente im Warenkorb zurück. */
  }

  public function addToCart($itemId) {
    /* Diese Funktion fügt das Element mit der ID $itemId dem Warenkorb hinzu. */
  }

  public function generateCartTable() {

    /*
      Hier erzeugen Sie die Warenkorbübersicht, sofern Artikel im Warenkorb sind.
       Der Rückgabewert der Funktion ist eine Zeichenkette, die die einzelnen Tabellenzeilen enthält.
       Vergleichen Sie Ihr Ergebnis mit der Beispielimplementierung!
    */

  }
}
