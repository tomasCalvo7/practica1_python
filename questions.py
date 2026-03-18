import random
words = {"lenguaje":["python"],
         "datos":["variable","entero","cadena"],
         "modulo":["lista","funcion","bucle","programa"]}
letras_validas = "abcdefghijklmnopqrstuvwkxyz"
print("¡Bienvenido al Ahorcado!")
print()
print("Las categorias disponibles son :")
for cat in words.keys():
  print(f"{cat}")
eligio = input("seleccione una categoria ").lower()
palabras = random.sample(words[eligio],k = len(words[eligio]))   
for rondas in palabras : 
  word = rondas
  puntaje = 0    # reinicio el puntaje por ronda
  guessed = []   #reinicio el contador de palabras en cada ronda
  attempts = 6   #reinicio los intentos por palabra de cada ronda
  print("Nueva ronda")
  while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
      if letter in guessed:
        progress += letter + " "
      else:
        progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
      puntaje += 6
      print("¡Ganaste!")
      break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or letter not in letras_validas:
      print("Entrada no valida")
      continue
    elif letter in guessed:
      print("Ya usaste esa letra.")
    elif letter in word:
      guessed.append(letter)
      print("¡Bien! Esa letra está en la palabra.")
    else:
      guessed.append(letter)
      attempts -= 1
      puntaje -= 1
      print("Esa letra no está en la palabra.")
    print()
  else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
  print(f"tu puntaje fue :{puntaje}")