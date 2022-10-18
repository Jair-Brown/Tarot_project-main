import random

deck = [
    {"name": 'The Fool', 'Upright': 'Beginnings, Possibilities, Pleasure, Adventure, Opportunity',
     'Reversed': 'Indecision, Hesitation< Injustice, Apathy, Bad Choice'},
    {"name": 'The Magician', 'Upright': 'Creativity, Self-Confidence, Dexterity, Sleight of Hand, Will Power, Skill',
     'Reversed': 'Delay, Unimaginative, Insecurity, Lack of Self_confidence'},
    {"name": 'The Empress', 'Upright': 'Development, Accomplishment, Action, Evolution',
     'Reversed': 'Inaction, Lack of Concentration, Vacillation, Anxiety, Infidelity'},
    {"name": 'The Emperor', 'Upright': 'Authority, Structure, Control', 'Reversed': 'Tyranny, Rigidity, Coldness'},
    {"name": 'The High Priestess', 'Upright': 'Knowledge, Wisdom, Learning, Intuition, virtue, Purity',
     'Reversed': 'Selfishness, Shallowness, Misunderstanding, Ignorance'},
    {"name": 'The Hierophant', 'Upright': 'Mercy, Conformity, Forgiveness, Inspiration',
     'Reversed': 'Vulnerability, Foolish, Generosity, Frailty'},
    {"name": 'The Lovers', 'Upright': 'Harmony, trust, Romance, Optimism, Honor , Love',
     'Reversed': 'Separation, Frustration, Unreliability, Fickleness, Untrustworthy'},
    {"name": 'The Chariot', 'Upright': 'Perseverance, Rushed Decision, Turmoil,Vengeance, Adversity',
     'Reversed': 'Vanquishment, Defeat, Failure, Unsuccessful'},
    {"name": 'The Hermit', 'Upright': 'Inner Strength, Prudence, Withdrawal, Caution, Vigilance',
     'Reversed': 'Hastiness, Rashness, Immaturity, Imprudence, Foolishness'},
    {"name": 'Strength', 'Upright': 'Courage, Conviction, Strength, Determination, Action, Heroism',
     'Reversed': 'Pettiness, Sickness, Unfaithfulness, Weakness'},
    {"name": 'Justice', 'Upright': 'Equality, Righteousness, Virtue, Honor, Harmony, Balance',
     'Reversed': 'False Accusation, Unfairness, Abuse, Biased'},
    {"name": 'The Wheel of Fortune', 'Upright': 'Unexpected events, Advancement, Destiny, Fortune, Progress',
     'Reversed': 'Interruption. Outside, Influences, Failure, Bad Luck'},
    {"name": 'The Moon', 'Upright': 'Deception, Disillusionment, Trickery, Error, Danger, Disgrace',
     'Reversed': 'Trifling Mistakes, Deception, Discovered Negative Advantage'},
    {"name": 'The Sun', 'Upright': 'Accomplishment, Success, Love, Joy, Happy Marriage, Satisfaction',
     'Reversed': 'Loneliness, Canceled Plans, Unhappiness, Break Ups'},
    {"name": 'The Star', 'Upright': 'Balance, Pleasure, Optimism, Insight, Spiritual love, Hope, Faith',
     'Reversed': 'Disappointment, Bad Luck, Imbalance, Broken Dreams'},
    {"name": 'The Devil', 'Upright': 'Downfall, Unexpected Failure, Controversy, Disaster, lll tempered ',
     'Reversed': 'Release, Enlightenment, Divorce, Recovery'},
    {"name": 'The Hanged Man', 'Upright': 'Change, Reversal, Boredom, Improvement, Rebirth, Suspension, Change',
     'Reversed': 'False Prophecy, Useless Sacrifice, Unwillingness'},
    {"name": 'Death', 'Upright': 'Unexpected Change, Loss, Failure, Transformation, Death, Bad Luck',
     'Reversed': 'Immobility, SLow changes, Cheating, Death, Stagnation'},
    {"name": 'Temperance', 'Upright': 'Patience, Good Influence, Confidence, Moderation',
     'Reversed': 'Conflict, Disunion, Frustration, Impatience, Discord'},
    {"name": 'The Tower', 'Upright': 'Disruption, Abandonment, Bankruptcy, Downfall, Unexpected Events',
     'Reversed': 'Entrapment, Imprisonment, Old Ways, Rustic'},
    {"name": 'Judgement', 'Upright': 'Awakening, Renewal, Rejuvenation, Rebirth, Improvement',
     'Reversed': 'Indecision, Death, Failure, Ill-Health, Theft, Worry'},
    {"name": 'The World', 'Upright': 'Perfection, Recognition, Success, Fulfillment, Eternal Life',
     'Reversed': 'Lack of Vision, Disappointment, Imperfection'},
]

number_card = input("Hello my friend. How many cards would you like in your spread today? ")
card_amount = int(number_card)
spread = []
num = random.randint(1, len(deck) - 1 )
#card = deck[num]
inverse = random.randint(-1, 0)
defs = []
names = []
collective = {}


class TarotHand:
    def __init__(self):
        pass

    # this function is used to grab cards from the deck at random for the tarot spread
    def tarot_spread(self, card_amount, spread):
        self.card_amount = card_amount
        #card = deck.object[random.randint(1, len(deck) - 1)]
        global deck
        
        while len(spread) < card_amount:
            spread.append(deck[num])
            if IndexError:
                pass
            for thing in spread:
                if thing in deck:
                    deck.remove(thing)


            continue
                #spread  (deck["name"[random.randint(1, len(deck) - 1)]])



       # print(spread)
        return str(names)



    def tarot_visual(self, spread):
        global inverse
# this function needs to return inverse or upright for every value in spread.

        for object in spread:

            inverse = random.randint(-1, 0)
            if inverse == -1:
                print(str(object["name"]) + " inverse")
                defs.append(object["Reversed"])
                names.append(object["name"])
                continue


            if inverse == 0:
                print(str(object["name"]) + " upright")
                defs.append(object["Upright"])
                names.append(object["name"])
                continue
            else:
                print(str(object["name"]) + " upright")
                defs.append(object["Upright"])
                continue



        return str(defs)

    def printable(self, defs, names):
        global collective

        collective = dict(zip(names, defs))
        for name, reading in collective.items():
            print("Your card " + name +" says your future holds: " + reading)



tarot = TarotHand()
(tarot.tarot_spread(card_amount, spread))
(tarot.tarot_visual(spread))
print(tarot.printable(defs, names))
