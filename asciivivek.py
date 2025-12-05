import os
import msvcrt as msv
import sys

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

data = [
    " *  **   *  **  ** **  *  *   * ** ** *   * *     *   * *   *  *  **   *  **   ** ** *   * *   * *   * *   * *   * **        *                     *  *   **  **  *   * **  **  **  **  *** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     * * *  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * **                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * **  *     *   * *   **  *  * **   *      *  *   *     * * * * * * *   * **  *   * **  **   *   *   * *   * * * *   *     *     *         * * *       **       *   *   *       *   *  ** **  **      *  *  *** ",
    "** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  * *   * *     *   * *  *      *   *   *   *  * *  * *  * *    *    *          * * *              *  *   *   *   *       *     *     * *   *     * *   *     * ",
    "*   * **   *  **  ** *      **  *   * **  **  *   * ** *   * *   *  **  *      *  *   * **    *   **   *   *   * *   *   *   **        *  **        **   *  ** ** **      * **   *      *  *      * "
]

def oneCharacter():
    os.system("cls")
    print(YELLOW + "\n\n" + ""*10 + " ASCII ART PROJECT " + ""*10 + RESET)
    print(CYAN + "\n\n" + ""*10 + " One Character Module " + ""*10 + RESET)
    text = input(GREEN + "Enter a Character (Only One Character) -- " + RESET).upper()

    if len(text) != 1:
        print(RED + "\n\nPlease Enter Only One Letter -- \n\n" + RESET)
        oneCharacter()
    else:
        print(WHITE + f"\n\nYou Entered -- {text}\n\n" + RESET)
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else 26*6 if text ==" " else 27*6 if text=="@" else 28*6 if text=="_" else 29*6 if text=="-" else 30*6 if text=="." else ((ord(text)-64)-1)*6
        for i in data:
            for j in range(n, n+6):
                print(MAGENTA + i[j] + RESET, end="")
            print()

def alphaNumWords():
    os.system("cls")
    sys.stdin.flush()
    print(YELLOW + "\n\n" + ""*10 + " ASCII ART PROJECT " + ""*10 + RESET)
    print(CYAN + "\n\n" + ""*10 + " Alpha Numeric Words Module " + ""*10 + RESET)
    
    text = input(GREEN + "Enter String (Only <= 15 Character) -- " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(RED + "\n\nPlease Enter Only <=15 Letter -- \n\n" + RESET)
        alphaNumWords()
    else:
        print(WHITE + f"\n\nYou Entered -- {text}\n\n" + RESET)
        for i in data:
            for x in text:
                n = (ord(x)-17)*6 if ord(x)>=48 and ord(x)<=57 else 26*6 if x==" " else 27*6 if x=="@" else 28*6 if x=="_" else 29*6 if x=="-" else 30*6 if x=="." else ((ord(x)-64)-1)*6
                for j in range(n, n+6):
                    print(MAGENTA + i[j] + RESET, end="")
            print()

def alphaRange():
    os.system("cls")
    sys.stdin.flush()
    print(YELLOW + "\n\n" + ""*10 + " ASCII ART PROJECT " + ""*10 + RESET)
    print(CYAN + "\n\n" + ""*10 + " Alpha Range Module " + ""*10 + RESET)

    text = input(GREEN + "Enter Range Between (1 to 15 Character) & in Sequence Like (A-D) -- " + RESET).upper()

    if len(text) != 3:
        print(RED + "\n\nPlease Enter Valid Range -- \n\n" + RESET)
        alphaRange()
    else:
        print(WHITE + f"\n\nYou Entered -- {text}\n\n" + RESET)
        sr = ord(text[0]) - 64
        er = ord(text[2]) - 64

        if sr > er or abs(er-sr) >= 15:
            print(RED + "\n\nPlease Enter Valid Range in Sequence -- \n\n" + RESET)
            msv.getch()
            alphaRange()
        else:
            for i in data:
                for x in range(sr, er+1):
                    n = (x-1) * 6
                    for j in range(n, n+6):
                        print(MAGENTA + i[j] + RESET, end="")
                print()

def onlyAlpha():
    os.system("cls")
    sys.stdin.flush()
    print(YELLOW + "\n\n" + ""*10 + " ASCII ART PROJECT " + ""*10 + RESET)
    print(CYAN + "\n\n" + ""*10 + " Only Alphabets Module " + ""*10 + RESET)

    text = input(GREEN + "Enter String (Only <= 15 Character) -- " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(RED + "\n\nPlease Enter Only <=15 Letter -- \n\n" + RESET)
        msv.getch()
        onlyAlpha()
    elif not text.isalpha():
        print(RED + "\n\nPlease Enter Only Alphabets -- \n\n" + RESET)
        msv.getch()
        onlyAlpha()
    else:
        print(WHITE + f"\n\nYou Entered -- {text}\n\n" + RESET)
        for i in data:
            for x in text:
                n = ((ord(x)-64)-1)*6
                for j in range(n, n+6):
                    print(MAGENTA + i[j] + RESET, end="")
            print()

def onlyNum():
    os.system("cls")
    sys.stdin.flush()
    print(YELLOW + "\n\n" + ""*10 + " ASCII ART PROJECT " + ""*10 + RESET)
    print(CYAN + "\n\n" + ""*10 + " Only Numbers Module " + ""*10 + RESET)

    text = input(GREEN + "Enter String (Only <= 15 Character) -- " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(RED + "\n\nPlease Enter Only <=15 Letter -- \n\n" + RESET)
        onlyNum()
        msv.getch()
    elif not text.isnumeric():
        print(RED + "\n\nPlease Enter Only Numbers -- \n\n" + RESET)
        msv.getch()
        onlyNum()
    else:
        print(WHITE + f"\n\nYou Entered -- {text}\n\n" + RESET)
        for i in data:
            for x in text:
                n = (ord(x)-17)*6 if ord(x) >= 48 and ord(x) <= 57 else ((ord(x)-64)-1)*6
                for j in range(n, n+6):
                    print(MAGENTA + i[j] + RESET, end="")
            print()

def mainUI():
    os.system("cls")
    print(YELLOW + "\n\n" + ""*10 + " ASCII ART PROJECT " + ""*10 + RESET)
    print(BLUE + "OPTIONS -- \n")
    print(BLUE + "1. One Character")
    print(BLUE + "2. Words (Maximum 15 Letters)")
    print(BLUE + "3. Range (input in Sequence - Max 15 Letters)")
    print(BLUE + "4. Only Alphabets")
    print(BLUE + "5. Only Numbers")
    print(BLUE + "6. Exit")
    print(GREEN + "\n\nEnter Your Choice -- " + RESET, end="")

    ch = msv.getch()

    if ch.decode() == "1":
        oneCharacter()
    elif ch.decode() == "2":
        alphaNumWords()
    elif ch.decode() == "3":
        alphaRange()
    elif ch.decode() == "4":
        onlyAlpha()
    elif ch.decode() == "5":
        onlyNum()
    elif ch.decode() == "6":
        return

    print(GREEN + "\n\nDo you want to continue Project.. Press y else any key..." + RESET)
    ch = msv.getch()

    if ch.decode() == "y" or ch.decode() == "Y":
        mainUI()

mainUI()