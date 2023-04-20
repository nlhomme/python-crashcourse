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

`pop()` supprime le dernier élément d'une liste, mais permet quand même de jouer avec
```
>>> motorcycles = ['honda', 'yamaha', 'suzuki']
>>> print(motorcycles)
['honda', 'yamaha', 'suzuki']
>>> popped_motorcycle = motorcycles.pop()
>>> print(motorcycles)
['honda', 'yamaha']
>>> print(popped_motorcycle)
suzuki
```
`pop(x)` où x est la position de pop souhaitée

Suppresion possible d'un élément d'une liste par sa valeur
```
>>> motorcycles.remove('honda')
>>> print(popped_motorcycle)
suzuki
```
/!\ Ne supprime que la première occurence de la valeur spécifiée
