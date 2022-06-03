
using System;

/* Diese Namensräume benötigen Sie vermutlich zusätzlich... */
using System.Net;
using System.Globalization;
using System.Collections.Generic;

namespace webproghttpd {
  class WebProgHttpd {
    const string VERSION = "0.2";

    static void help() {
      /**
       * Hier könnte die Ausgabe der Hilfe erfolgen.
       *
       * Sie müssen diese Funktion allerdings nicht nutzen. Sie dürfen
       * sie entfernen und Ihr Programm anders strukturieren.
       *
       **/
    }

    static void Main(string[] args) {
      Console.WriteLine("*** webproghttpd v{0} - ein einfacher Webserver!", WebProgHttpd.VERSION);
      Console.WriteLine("");
      Console.WriteLine("Teil des Praktikums Web-Programmierung im Sommersemester 2020");
      Console.WriteLine("an der Technischen Hochschule Nürnberg Georg Simon Ohm.");
      Console.WriteLine("");

      /* 1. Prüfen Sie auf das Vorhandensein von Optionen */
      /*
       * -h soll einen kurzen Hilfetext zu den verfügbaren Optionen ausgeben
       * und dann das Programm beenden.
       *
       * -p N nimmt einen Integer N an und setzt den Port, auf dem der Webserver
       * auf eingehende Verbindungen wartet auf diesen Wert (z.B. -P 8080).
       * Ist diese Option nicht vorhanden, soll der Default-Port 80 sein.
       *
       */

      /* 2. Starten Sie den Server und warten auf eingehende Verbindungen. */

      /* 3. Bearbeiten Sie die Verbindungsanfragen entsprechend der Vorgaben. */

      /* 4. Zurück zu 2., es sei denn die Anfrage war "/exit". */

    }
  }
}
