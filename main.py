meme_dict = {
    "cringe": "Algo embarazante",
    "lol": "algo increible o gracioso",
    "idk": "No lo se (i dont know)",
    "creepy": "terror miedo etc"
}


word = input('palabra que no sepas:').lower()

if word in meme_dict.keys():
    print(f"la palabra {word} significa {meme_dict[word]}")
else:
    print("No conocemos esa palabra")