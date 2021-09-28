
import random   



verbs =['Leverage', 'Sync', 'Target', 'Gamify' 'offline', 'Crowd-sourced', '24/7', 'Lean-in', '30,00 foot']


adjectives =['A/B tested', 'Freemium', 'Hyperlocal', 'Siliod', 'B-to-B', 'Oriented', 'Cloud-based', 'API-based']


nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']



verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun= random.choice(nouns)



phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)
