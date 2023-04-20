Ajouter une tabulation à un string
```python
>>> print("\tPython")
	Python
```

Ajouter des lignes dans un string
```python
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

Supprimer un whitespace (caractère non-imprimable) à droite
```python
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
```
`.lstrip` à gauche <br>
`.strip` pour les deux en même temps <br>


Enlever un préfixe:
```python
>>> url = "https://www.google.com"
>>> print(url.removeprefix('https://'))
www.google.com
```

Les underscores facilient la lecture des nombres:
```python
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000000
```

/!\ Les constantes se déclarent en majuscule
```python
MAX_CONNECTIONS = 6
```

L'instruction `import this` affiche The Zen of Python de Tim Peters, la philosophoe autour du dev Python

`pop()` supprime le dernier élément d'une liste, mais permet quand même de jouer avec
```python
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
```python
>>> motorcycles.remove('honda')
>>> print(popped_motorcycle)
suzuki
```
/!\ Ne supprime que la première occurence de la valeur spécifiée

/!\ `range()` commence à compter à la première valeur fournie
```python
>>> for value in range(1, 6):
...print(value)
...
1
2
3
4
5
```

On peut générer une liste de nombres en une seule ligne
```python
numbers = list(range(0,>>> numbers = list(range(0,10))
>>> print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Comprehensive list déclaration et remplissage selon règle en une seule ligne
```python
>>> squares = [value**2 for value in range(1, 11)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Copier une liste:
```python
>>> my_foods = ['pizza', 'falafel', 'carrot cake']
>>> friends_foods = my_foods[:]
>>> print(friends_foods)
['pizza', 'falafel', 'carrot cake']
```
/!\ Faire friend_foods = my_foods est faux car les deux variables pointent vers la même liste

Contrairement à une list, un tuple n'est pas modifiable <br>
MAIS on peut lui assigner une nouvelle valeur
```python
dimensions = (200, 50)
dimensions = (400, 100)
```