
# Maturaarbeit Lars Hoesli - Konzept


## Übersicht

Die Arbeit ist Produkt-orientiert. Sie untersucht die Umwandlung von Rastergraphiken zu Vektorgraphiken mithilfe von einem deeplearning Modell, das an automatisch generierten Daten trainiert wird. Das Produkt wird folglich diese Strategie verwenden, und soll eine Raster-ähnliche Repräsentation von einfachen Formen in eine Vektor-ähnliche umwandeln können.


### Umfang

Einfache Formen heisst hier:
- Mindestens Kreise, da sie einfach zu beschreiben sind (Mittelpunkt, Radius, möglicherweise Farbe)
- Linien (einfach zu beschreiben, und können schon viele Bilder annäherungsweise beschreiben)
- Drei- und Rechtecke

Möglicherweise kommen noch weitere Formen hinzu, die eine vollständige Vektorgraphik hätte:
- Kurven (Bezierkurven, Splines, Kreisbögen)
- Polygone (bzw Pfade)
- Ellipsen

Die Begriffe Raster- bzw Vektor-ähnlich meinen hier eine beliebige Art von Repräsentation eines Bildes und nicht ein bestimmtes konkretes Bildformat wie PNG, JPG oder SVG.
- Raster-ähnliche Bildrepräsentation kann beispielsweise eine Matrix aus Zahlen sein, die die Pixelwerte darstellen
- Vektor-ähnlich meint irgendetwas, das die Formen in einem Bild eindeutig beschreibt (Liste, Klasse, String, ...)



In dem schriftlichen Teil der Arbeit werde ich zunächst eine Einführung in das Gebiet von Raster- zu Vektorgraphiken wie auch zu Künstlicher Intelligenz erarbeiten, und danach auf die Motivation hinter dem Projekt eingehen. Ich werde traditionelle und neuere Ansätze dazu erläutern, und dann die Überlegungen hinter den Entscheidungen für die gewählten Strategien und Hilfsmittel darstellen (Sprache, Bibliotheken, AI-Model, Datengeneration).

Am Ende werde ich die Ergebnisse und Erfahrungen auswerten und die Erfolge, Misserfolge, Potenzial und Grenzen des Projekts aufzeigen. Vielleicht gehe ich genauer auf einige Schaukesselstellen im Code ein.



### Titel

Ich werde mir nebst einem wissenschaftlichen Titel noch einen leicht verständlichen Titel, wie auch eine deutsche Übersetzung und einen Kurznamen für das Computerprogramm ausdenken.
Der provisorische ausgeschriebene Titel der Arbeit wäre "Vectorization of raster images containing simple shapes using a neural network trained with on-the-fly generated data"\*, um den Umfang der Arbeit möglichst genau zu beschreiben, und etwas wie "RtoV" ("Raster to Vector") wäre der Name für das resultierende Programm selbst.

\* Möglicherweise auch eine (etwas) kürzere Alternative: "Training an AI with on-the-fly generated data for raster to vector graphics conversion"


