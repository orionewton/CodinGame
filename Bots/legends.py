import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Player:
    def __init__(self, health, mana, deck, rune, draw):
        self.health = health
        self.mana = mana
        self.deck = deck
        self.rune = rune
        self.draw = draw


class Card:
    def __init__(self, number, instid, location, ctype, cost, attack, defense, abilities, p1_change, p2_change, draw):
        self.number = int(number)
        self.instid = int(instid)
        self.location = int(location)
        self.ctype = int(ctype)
        self.cost = int(cost)
        self.attack = int(attack)
        self.defense = int(defense)
        self.spec = abilities
        # spec: Break / Charge / Drain / Guard / Lethal / Ward
        self.p1_change = int(p1_change)
        self.p2_change = int(p2_change)
        self.draw = int(draw)
        if ctype == 0:
            # Creature
            if cost == 0:
                val = (attack+defense)+5
            else:
                val = (attack+defense-1)/(cost)
                if cost < 4:
                    val += 1
            if 'B' in abilities:
                val += 0.5
            if 'C' in abilities:
                val += 1
            if 'D' in abilities:
                val += 1
            if 'G' in abilities:
                val += 3
            if 'L' in abilities:
                val += 2
            if 'W' in abilities:
                val += 1
            
            self.value = val + p1_change*0.2 + p2_change*0.1 + draw*0.5
        else:
            # Items
            val = 0.1
            # ctype = [1,2,3]
            if ctype == 1:
                # Green item
                if cost == 0:
                    val = (attack+defense)
                else:
                    val = (attack+defense)/(cost)
                if 'B' in abilities:
                    val += 0.5
                if 'C' in abilities:
                    val += 1
                if 'D' in abilities:
                    val += 1
                if 'G' in abilities:
                    val += 2
                if 'L' in abilities:
                    val += 3
                if 'W' in abilities:
                    val += 1
            
            elif ctype == 2:
                # Red item
                val = (abs(attack)+abs(defense)-1)/(cost+1)

            elif ctype == 3:
                # Blue item
                val = cost/3 + p1_change/2 + p2_change/2
            self.value = val


def draftpick(c1, c2, c3, drafthand):
    best = max(c1.value, c2.value, c3.value)
    d1 = drafthand[c1.cost]
    d2 = drafthand[c2.cost]
    d3 = drafthand[c3.cost]
    if best == c1.value and d1 < 7:
        drafthand[c1.cost] += 1
        return "PICK 0"
    else:
        best = max(c2.value, c3.value)
        if best == c2.value and d2 < 7:
            drafthand[c2.cost] += 1
            return "PICK 1"
        elif best == c3.value and d3 < 7:
            drafthand[c3.cost] += 1
            return "PICK 2"
        else:
            best = min(d1, d2, d3)
            if best == d1:
                return "PICK 0"
            elif best == d2:
                return "PICK 1"
            else:
                return "PICK 2"

def playable_cards(cards, mana):
    playable = []
    for i in cards:
        if i.cost <= mana:
            playable.append(i)
    # Expensive cards in first
    playable.sort(key=lambda x: x.cost, reverse=False)
    return playable

def cards_location(cards):
    hand = []
    forces = []
    monsters = []
    for i in cards:
        if i.location == 0:
            hand.append(i)
        elif i.location == 1:
            forces.append(i)
        elif i.location == -1:
            monsters.append(i)

    for i in range(len(monsters)):
        # Guard creatures in first
        if 'G' in monsters[i].spec:
            monsters.insert(0, monsters[i])
            monsters.pop(i+1)

    return hand, forces, monsters

def attacks(forces, monsters): # Attack phase optimised
    command = ""
    cpt = 0
    for i in forces:
        if forces[cpt].attack == 0 or "G" in forces[cpt].spec:
            forces.pop(cpt)
        cpt += 1

    while len(forces) > 0:
        targets = len(monsters)
        if targets == 0:
            command += "ATTACK " + str(forces[0].instid) + " -1; "
            forces.pop(0)
        else:
            cpt = 0
            for j in monsters:
                # TODO: Determiner meilleur combat
                command += "ATTACK " + str(forces[0].instid) + " " + str(j.instid) + "; "
                j.defense -= forces[0].attack
                if j.defense < 1: # Update opponent forces
                    monsters.pop(cpt)
                cpt += 1
                forces.pop(0)

    return command

def best_target (cards):
    return cards[cards.index(max(cards, key=lambda item: item.value))].instid

p1 = Player(30,1,0,0,0)
p2 = Player(30,1,0,0,0)
draft = 0
drafthand = [0]*13

# game loop
while True:
    cards = []
    for i in range(2):
        # Players state
        health, mana, deck, rune, draw = [int(j) for j in input().split()]
        if i==1:
            p1.health = health
            p1.mana = mana
            p1.deck = deck
            p1.rune = rune
            p1.draw = draw
        else:
            p2.health = health
            p2.mana = mana
            p2.deck = deck
            p2.rune = rune
            p2.draw = draw
    
    opponent_hand, opponent_actions = [int(i) for i in input().split()]

    for i in range(opponent_actions):
        # Opponent actions
        card_number_and_action = input()

    card_count = int(input())
    
    for i in range(card_count):
        # Cards state
        number, instid, location, ctype, cost, attack, defense, abilities, p1_change, p2_change, draw = input().split()
        number = int(number)
        instid = int(instid)
        location = int(location)
        ctype = int(ctype)
        cost = int(cost)
        attack = int(attack)
        defense = int(defense)
        p1_change = int(p1_change)
        p2_change = int(p2_change)
        draw = int(draw)
        cards.append(Card(number, instid, location, ctype, cost, attack, defense, abilities, p1_change, p2_change, draw))

    if draft < 30:
        # draft phase
        print(draftpick(cards[0], cards[1], cards[2], drafthand))
        draft += 1

    else:
        # battle phase
        hand, forces, monsters = cards_location(cards) # Where are the cards ?

        play = playable_cards(hand, p2.mana) # What cards can i play ?
        command = ""

        # Summoning
        summon = []
        while len(play) > 0: # Playables cards
            if len(forces) <= 6 and play[0].ctype == 0: # There is space for creatures
                command += "SUMMON " + str(play[0].instid) + "; "
                if 'C' not in play[0].spec:
                    summon.append(play[0].instid)
                for x in cards:
                    if x.instid == play[0].instid:
                        x.location = 1
                p2.mana -= play[0].cost
                hand, forces, monsters = cards_location(cards)
                play = playable_cards(hand, p2.mana)

            elif play[0] == 1 and len(forces) > 0: # Green Item
                command += "USE " + str(play[0].instid) + str(best_target(forces)) + "; "

            elif play[0] == 2 and len(monsters) > 0: # Red Item
                command += "USE " + str(play[0].instid) + str(best_target(monsters)) + "; "

            else:
                play.pop(0)

        # items bleu ?

        # Attacking
        fighter = 0

        # Disable attack for creatures sumoned this turn
        cpt = 0
        for i in forces:
            for j in summon:
                if forces[cpt].instid == j:
                    forces.pop(cpt)
            cpt += 1

        command += attacks(forces, monsters)

        if command == "": # Nothing to do
            command = "PASS"
            
        print(command)

# To debug: print("Debug messages...", file=sys.stderr, flush=True)
