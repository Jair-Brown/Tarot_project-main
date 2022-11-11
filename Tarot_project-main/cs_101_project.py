import random
from tkinter import *
from tkinter import ttk


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
     'Reversed': 'Immobility, Slow changes, Cheating, Death, Stagnation'},
    {"name": 'Temperance', 'Upright': 'Patience, Good Influence, Confidence, Moderation',
     'Reversed': 'Conflict, Disunion, Frustration, Impatience, Discord'},
    {"name": 'The Tower', 'Upright': 'Disruption, Abandonment, Bankruptcy, Downfall, Unexpected Events',
     'Reversed': 'Entrapment, Imprisonment, Old Ways, Rustic'},
    {"name": 'Judgement', 'Upright': 'Awakening, Renewal, Rejuvenation, Rebirth, Improvement',
     'Reversed': 'Indecision, Death, Failure, Ill-Health, Theft, Worry'},
    {"name": 'The World', 'Upright': 'Perfection, Recognition, Success, Fulfillment, Eternal Life',
     'Reversed': 'Lack of Vision, Disappointment, Imperfection'},
]

root = Tk()
root.title("Tarot reading")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky =( N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)




class Tarot:

    def __init__(self) -> None:
        
        self.number_card = int(input("Hello my friend. How many cards would you like in your spread today? "))
        self.hand = []
        
        

    def cards(self):
        deck1 = deck.copy()
        counter = self.number_card
        # self.hand = []
        show_hand = []
        ran_num = random.randint(0,len(deck1))
        card_number = ran_num
        inverse = random.randint(1,2)

    
        while len(self.hand) < counter:
            
            card = random.choice(deck1)
            if card in self.hand:
                pass
            else:
                self.hand.append(card)
                deck1.remove(card)

        name = []        
        # while len(name) > counter :
        for x in self.hand:
               
            name.append(x['name'])
            a = x['Upright']
            b = x['Reversed']
            choices = [a,b]
            show_hand.append(random.choice(choices))
        # print(show_hand)
        spread = {name[i]: show_hand[i] for i in range(len(name))}
        for j in spread.keys():
            print (" Your card " + j + " symbolizes: " + spread[j])
        # return spread.values(), spread.keys()

        
    
         
first = Tarot()
print(first.cards())
