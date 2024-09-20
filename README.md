# Spelet "21" i Python

Detta är ett Python-projekt för att skapa kortspelet "21", även känt som Blackjack. Målet med spelet är att ha en hand vars värde är så nära 21 som möjligt utan att överstiga det.

## Spelregler

1. Varje spelare börjar med två kort.
2. Korten med siffror har sitt eget värde, klädda kort (knekt, dam, kung) är värda 10 och ess kan vara värda antingen 1 eller 14.
3. Spelaren kan välja att dra fler kort ("hit") eller stanna med sin nuvarande hand ("stand").
4. Om en spelares hand överstiger 21 förlorar spelaren omedelbart.
5. Om spelaren stannar under 21 får också datorn dra ett kort i taget och efter varje kort avgöra om den skall fortsätta eller inte
6. Om datorn får mer än 21 poäng eller lägre poäng än användaren vinner användaren, annars vinner datorn.

## Hur man kör spelet

För att köra spelet måste du ha Python installerat på din dator. Följ stegen nedan:

1. Klona projektet eller ladda ner källkoden.
2. Öppna en terminal och navigera till projektets rotmapp.
3. Kör spelet med följande kommando:
    ```bash
    python main.py
    ```

## Projektstruktur

Projektet är organiserat enligt följande mappstruktur:

- `src/`: Innehåller spelets källkod.
- `tests/`: Innehåller testfiler för att verifiera spelets funktionalitet.
- `README.md`: Dokumentation för projektet (denna fil).
- `.gitignore`: Anger vilka filer som ska ignoreras av Git.

## Krav
Validation av user inputs
- pip install pyinputplus

## Bidrag

Om du vill bidra till projektet, vänligen följ standard arbetsflödet för Git:
1. Fork projektet.
2. Skapa en ny gren för din funktion eller buggfix.
3. Gör ändringarna och skapa en pull request.
