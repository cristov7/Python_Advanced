# You come across an old JS Basics teamwork game.
# It is about bunnies that multiply extremely fast.
# There's also a player that should escape from their lair.
# You like the game, so you decide to port it to Python because that's your language of choice.
# The last thing left is the algorithm that determines if the player will escape the lair or not.
# First, you will receive a line holding integers N and M, representing the lair's rows and columns.
# Next, you receive N strings that can consist only of ".", "B", "P".
# They represent the initial state of the lair.
# There will be only one player.
# The bunnies are marked with "B", the player is marked with "P",
# and everything else is free space, marked with a dot ".".
# Then you will receive a string with commands (e.g., LRRULUD)
# each letter represents the next move of the player:
# •	L - the player should move one position to the left
# •	R - the player should move one position to the right
# •	U - the player should move one position up
# •	D - the player should move one position down
# After every step made, each bunny spreads one position up, down, left, and right.
# If the player moves to a bunny cell or a bunny reaches the player, the player dies.
# If the player goes out of the lair without encountering a bunny, the player wins.
# When the player dies or wins, the game ends.
# All the activities for this turn continue (e.g., all the bunnies spread normally),
# but there are no more turns.
# There will be no cases where the moves of the player end before he dies or escapes.
# In the end, print the final state of the lair with every row on a separate line.
# On the last line, print either "dead: {row} {col}" or "won: {row} {col}".
# "Row" and "col" are the cell coordinates
# where the player has died or the last cell he has been in before escaping the lair.

# Input
# •	On the first line of input,
# the numbers N and M are received - the number of rows and columns in the lair
# •	On the following N lines,
# each row is received in the form of a string.
# The string will contain only ".", "B", "P".
# All strings will be the same length.
# There will be only one "P" for all the input
# •	On the last line,
# the directions are received in the form of a string, containing "R", "L", "U", "D"

# Output
# •	On the first N lines, print the final state of the bunny lair
# •	On the last line, print:
# o	If the player won - "won: {row} {col}"
# o	If the player dies - "dead: {row} {col}"

# Constraints
# •	The dimensions of the lair are in the range [3…20]
# •	The directions string length is in the range [1…20]


# Попадате на стара игра за работа в екип на JS Basics.
# Става дума за зайчета, които се размножават изключително бързо.
# Има и играч, който трябва да избяга от леговището си.
# Харесвате играта, така че решавате да я пренесете на Python, защото това е избраният от вас език.
# Последното нещо, което остава, е алгоритъмът, който определя дали играчът ще избяга от леговището или не.
# Първо, ще получите ред, съдържащ цели числа N и M, представляващи редовете и колоните на леговището.
# След това получавате N низа, които могат да се състоят само от ".", "B", "P".
# Те представляват първоначалното състояние на бърлогата.
# Ще има само един играч.
# Зайчетата са маркирани с "B", играчът е маркиран с "P",
# и всичко останало е свободно място, отбелязано с точка ".".
# Тогава ще получите низ с команди (напр. LRRULUD)
# всяка буква представлява следващия ход на играча:
# • L - играчът трябва да се премести една позиция наляво
# • R - играчът трябва да се премести една позиция надясно
# • U - играчът трябва да се премести с една позиция нагоре
# • D - играчът трябва да се премести една позиция надолу
# След всяка направена стъпка, всяко зайче се разпространява с една позиция нагоре, надолу, наляво и надясно.
# Ако играчът се премести в клетка със зайче или зайче стигне до играча, играчът умира.
# Ако играчът излезе от леговището, без да срещне зайче, играчът печели.
# Когато играчът умре или спечели, играта приключва.
# Всички дейности за този ход продължават (напр. всички зайчета се разпространяват нормално),
# но няма повече завои.
# Няма да има случаи, в които ходовете на играча приключват преди той да умре или да избяга.
# Накрая отпечатайте крайното състояние на леговището с всеки ред на отделен ред.
# На последния ред отпечатайте или "dead: {row} {col}" или "won: {row} {col}".
# "Row" и "col" са координатите на клетката
# където играчът е умрял или последната клетка, в която е бил преди да избяга от леговището.

# Вход
# • На първия ред на въвеждане,
# се получават числата N и M - броя на редовете и колоните в леговището
# • На следващите N реда,
# всеки ред се получава под формата на низ.
# Низът ще съдържа само ".", "B", "P".
# Всички низове ще бъдат с еднаква дължина.
# Ще има само едно "P" за целия вход
# • На последния ред,
# указанията се получават под формата на низ, съдържащ "R", "L", "U", "D"

# Изход
# • На първите N реда отпечатайте крайното състояние на леговището на зайците
# • На последния ред отпечатайте:
# o Ако играчът спечели - "спечели: {row} {col}"
# o Ако играчът умре - "мъртъв: {ред} {кола}"

# Ограничения
# • Размерите на леговището са в диапазона [3…20]
# • Дължината на низа с посоки е в диапазона [1…20]


