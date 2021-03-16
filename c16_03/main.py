note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

# Question 4
#a/ calculez la moyenne de eleve1

print(notes[0][0])
print(len(note2))

def moyenne(liste):
  valeurs = 0
  for i in range(len(liste)):
      valeurs = valeurs + liste[i][2]
      moyenne = valeurs/len(liste)
  return(moyenne)
listes_elev1 =  [note1, note2, note3, note4, note5, note6]
print("la moyenne de l'élève 1",moyenne(listes_elev1))

# b/ calculez la moyenne de eleve1 en maths

liste_elev1_maths = [note1, note3, note6]
print("la moyenne de l'élève 1 en maths", moyenne(liste_elev1_maths))


#c / 
moyenne_tuples = [(x,y) for x in ['eleve1','eleve2'] for y in ['math','physique','eco'] in notes]

print(moyenne_tuples('eleve1','math',moyenne(notes)))