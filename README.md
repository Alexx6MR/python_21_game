# The game "21" in Python
This is the group project of nackademin's programming course 1 of the DevsOps engineer career. This is a Python project to create the card game "21", The Swedish version of blackjack. The most important differences between these two games are partly the value of the cards, partly that the banker in twenty-one plays against one player at a time and not, as in Black Jack, against everyone at once.

The idea of ​​the game is to try with two or more cards to reach the total value of 21, or get as close as possible without exceeding 21. Aces are worth either 1 or 14, kings 13, queens 12, jacks 11. The number cards have the same values ​​as the denomination .

[21 Game rules](https://sv.wikipedia.org/wiki/Tjugoett_(kortspel))

## Game rules

1. The game is played so that the player is dealt one card at a time and after each card must decide whether he wants additional cards or not.
2. It is up to the player to try to get the sum of the card values ​​as close as possible to 21 without exceeding this number.
3. Ace counts as either 1 or 14. user can choose which value to use.
4. If the player gets over 21, he loses and the computer wins.
5. If the player stays below 21, the computer must also draw one card at a time and after each card decide whether to continue or not.
6. If the computer scores more than 21 points or less than the user, the user wins, otherwise the computer wins.
7. The computer thus wins on the same score


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
