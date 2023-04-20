Ajouter une tabulation à un string
```
>>> print("\tPython")
	Python
```

Ajouter des lignes dans un string
```
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

Supprimer un whitespace (caractère non-imprimable) à droite
```
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
```
`.lstrip` à gauche <br>
`.strip` pour les deux en même temps <br>


Enlever un préfixe:
```
>>> url = "https://www.google.com"
>>> print(url.removeprefix('https://'))
www.google.com
```

Les underscores facilient la lecture des nombres:
```
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000000
```

/!\ Les constantes se déclarent en majuscule
```
MAX_CONNECTIONS = 6
```

L'instruction `import this` affiche The Zen of Python de Tim Peters, la philosophoe autour du dev Python
