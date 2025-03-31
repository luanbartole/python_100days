# Variable that determinate the outcome of the game
outcome = False


# Prints the header and the game's introduction
print('''
███╗░░██╗███████╗░█████╗░███╗░░██╗      ██╗░░░░░░█████╗░██████╗░██╗░░░██╗██████╗░██╗███╗░░██╗████████╗██╗░░██╗
████╗░██║██╔════╝██╔══██╗████╗░██║      ██║░░░░░██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗██║████╗░██║╚══██╔══╝██║░░██║
██╔██╗██║█████╗░░██║░░██║██╔██╗██║      ██║░░░░░███████║██████╦╝░╚████╔╝░██████╔╝██║██╔██╗██║░░░██║░░░███████║
██║╚████║██╔══╝░░██║░░██║██║╚████║      ██║░░░░░██╔══██║██╔══██╗░░╚██╔╝░░██╔══██╗██║██║╚████║░░░██║░░░██╔══██║
██║░╚███║███████╗╚█████╔╝██║░╚███║      ███████╗██║░░██║██████╦╝░░░██║░░░██║░░██║██║██║░╚███║░░░██║░░░██║░░██║
╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚══╝      ╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝''')
print("="*110)
print("Mission: Retrieve the stolen AI core.")
print("="*80)

#Choice 1 - Route selection
print('''The neon signs of Neon City flicker ominously as you step into the streets,
the rain mixing with the glow of holographic billboards. The AI core is 
hidden deep within enemy territory''')
print("\n[Route Selection]:")
choice1 = input("[1] Main Street / [2] Back Alley | ")
print("="*80)

if choice1 == "1":
    print('''The boulevard is alive with the hum of corporate drones patrolling the area. 
You keep your head low, weaving through the crowd of augmented citizens, avoiding eye 
contact with surveillance cameras. Soon, you arrive at the central hub, a towering 
structure pulsing with energy.\n''')

    # Choice 2 - Obstacle at the hub
    print('''The central hub is a massive, labyrinthine building with surveillance 
drones sweeping the area. The stolen AI core is inside, but you'll need to deal 
with the security systems first.''')
    print("\n[Obstacle at the hub]:")
    choice2 = input("[1] Hack Security / [2] Sneak Past | ")
    print("="*80)

    if choice2 == "1":
        print('''You jack into the network, your neural interface sparking as you 
bypass the corporate firewall. A sea of code scrolls past your vision until 
you disable the drones. The path is clear, and you move deeper into the hideout.\n''')

        # Choice 3 (Choose a door)
        print('''You find yourself in the hideout, a labyrinth of corridors lined 
with flickering neon lights and dampened by the hum of power generators. 
Three doors stand before you. The AI core is behind one, but which?''')
        print("\n[Choose a Door]:")
        choice3 = input("[1] Steel Door / [2] Glass Door / [3] Neon Door | ")
        print("=" * 80)

        if choice3 == "1":
            print('''The door slides open, releasing a cloud of knockout gas. 
You collapse to the ground as alarms sound in the distance.''')
        elif choice3 == "2":
            print('''As the door opens, a sentry bot swivels toward you, its 
red optics glowing menacingly. A burst of plasma ends your journey.''')
        elif choice3 == "3":
            print('''The door opens, revealing the AI core suspended in a 
containment field. You reach out, your cyberdeck glowing as you 
jack into the core and secure it. The mission is a success.''')
            outcome = True
        else:
            print('''You pick the wrong door. A jolt of electricity courses 
through your body, frying your augmentations.''')





    elif choice2 == "2":
        print('''You try to stay in the shadows, but the drones are equipped with 
thermal vision. One locks onto you, and the alarm blares. Moments later, 
a squad of corporate soldiers arrives, guns blazing''')
    else:
        print('''A hidden turret activates as you make your way forward, and the 
last thing you hear is the whir of its barrel spinning up.''')


elif choice1 == "2":
    print('''As you slip into the shadows, a gang of cyborg enforcers surrounds you, 
their mechanical claws gleaming under the dim light. Before you can react, one 
grabs your arm, and everything goes black.''')

else:
    print('''You hesitate, unsure which path to take. A red laser sight appears on 
your chest, followed by a silent thwip.''')



if outcome:
    print("=" * 80)
    print('''█░░█ █▀▀█ █░░█ 　 █░░░█ █▀▀█ █▀▀▄ 
█▄▄█ █░░█ █░░█ 　 █▄█▄█ █░░█ █░░█ 
▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ░▀░▀░ ▀▀▀▀ ▀░░▀''')
    print("=" * 80)
else:
    print("=" * 80)
    print('''█▀▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 
█░▀█ █▄▄█ █░▀░█ █▀▀ 　 █░░█ ░█▄█░ █▀▀ █▄▄▀ 
▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀''')
    print("=" * 80)



#