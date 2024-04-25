import sys

def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)

s = input()
change_count = int(input())
changes = []
if "\\n" in s:
        s = s.replace("\\n", "\n")
lines = s.split("\n")

for i in range(change_count):
    raw_change = input()
    line, column, content = raw_change.split("|")
    line = int(line)
    column = int(column)
    # Remplacement de "\n" par un véritable saut de ligne
    if "\\n" in content:
        content = content.replace("\\n", "\n")
    changes.append((line, column, content))

changes.sort(key=lambda x: (x[0], x[1]))
decal = 0
line_start = changes[0][0]

for change in changes:
    line_num, column, content = change
    if line_num != line_start:
        decal = 0
        line_start = line_num
    column += decal
    # S'assurer que la ligne à modifier existe
    while len(lines) <= line_num:
        lines.append("")  # Ajouter des lignes vides si nécessaire
    
    # Modifier la ligne spécifiée
    line_content = lines[line_num]
    # On doit insérer au bon endroit, donc on utilise des opérations de chaîne
    if column > len(line_content):
        # Si la colonne est plus grande que la longueur de la ligne, ajouter des espaces
        line_content += " " * (column - len(line_content))
    # Insérer le contenu à la position spécifiée
    updated_content = line_content[:column] + content + line_content[column:]
    # Mettre à jour la ligne avec le contenu modifié
    lines[line_num] = updated_content
    decal += len(content)

for i in lines:
    i = i.replace("\\n", "\n")
    for j in i.split("\n"):
        print(j)
