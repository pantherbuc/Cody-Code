# This is a short Text Adventure game, utilizing Booleans#

print("This game allows the player 2 types of interactions. You can input to either 'look' or 'interact'. Objects that you can observe or interact with will be sourounded by *astrics*. for example, to look at a *sword*, you would type 'look sword'. To interact with the *sword*, you would type 'interact sword'.")
print("")
print("")
print("----------------------")
print("THE GREATEST ADVENTURE")
print("----------------------")
print("")

#This block tricks the player into revealing if they are a horse

horsedatabase = ['horse', 'horses', 'equine', 'equines', 'neigh', 'neighs', 'maverick', 'stallion', 'mare', 'pony', 'steed', 'colt',]

name = input("Please enter character name: ")
horsecheck = name.lower()
if horsecheck in horsedatabase:
  print("NO. HORSES.")
  print("GAME OVER")
  quit(0)


#This block is the first room

print("")
print("")
action = 'Empty'
print("You find yourself in a hallway leading *north*")
while action != 'interact north':
  action = input("")
  if action == 'look north':
    print("The *north* looks pretty good")

#second room with multiple options to interact with, along with variables to keep track of player actions here to use later

print("----------------------------")
action = 'empty'
sword = False
print("You make your way north, and come across a room. There is a *sword* on the ground and a *door* in front of you")

while action != 'interact door':
  action = input("")
  if action == 'look sword' and(sword == False):
    print("The *sword* is on the ground, and glistens against the dust and rocks")
  if action == 'look sword' and(sword == True):
    print("The *sword* looks mighty in your hands")
  if action == 'interact sword':
    print("You pick up the sword. Its weight is heavy.")
    sword = True
  if action == 'look door':
    print("The *door* is unlocked, and made of wood.")

#Third room. Wizard encounter

print("----------------------------")
action = 'empty'
wizard = 'unsearched'
wizardlife = 'alive'

print("You open the door to the next room and enter. Before you stands a mighty *wizard*, he turns his attention to you and says, ""So, you have finally come to vanquish me, " + name + ". Unfortunetaly you do not know my secret weakness.\"")

while action != ('interact wizard') and(wizardlife != 'dead'):
  action = input("")
  if action == 'look wizard':
    print("You examine the *wizard* closely, and believe to see his weakness. He seems very sword-able")
  if action == 'interact wizard' and(sword == False):
    print("You lunge at the wizard, and try to beat him with your fists. He lights you aflame with magic.")
    print("He laughs over your charred body and says, 'You should have brought a sword!'")
    print("GAME OVER")
    quit()
  if action == 'interact wizard' and(sword == True):
    print("You lunge at the 'wizard' wielding your mighty sword. You stab him and he evaporates immediatly. You feel accomplished.")
    wizardlife = 'dead'

print("---------------------------------")

#Third room but now explorable options are different

mirror = False
print("Left on the ground are the *ashes* of the old man. An old magical *door* also opens up in front of you.")
while (action != ('look mirror' or 'interact mirror')):
  action = input("")
  if action == 'look ashes' and mirror == False:
    print("They look like some *ashes*.")
  if action == 'look ashes' and mirror == True:
    print("There is nothing left in the *ashes*. Only the *mirror*.")
  if action == 'interact ashes':
    print("after disturbing the old man's ashes for a while, you notice a a shiny silver *mirror* in them")
    mirror = True
  if action == 'look mirror' and (mirror == True):
    print("You look into the mirror and come to the horrible realization that YOU were the wizard all along.")
    break
  if action == 'interact mirror' and (mirror == True):
    print("You look into the mirror and come to the horrible realization that YOU were the wizard all along.")
    break
  if action == 'look door':
    print("The 'door' looks magical.")
  if action == 'interact door':
    if mirror == False:
      print("You make your way out the door. Your quest completed")
      break
    if mirror == True:
      print("You ignore the 'mirror' you just found for some reason, and exit through the magical door. You feel content that certainly you did not miss out on any game content by not exploring everything (like for example, the mirror).")
      break

print("")
print("GAME OVER")