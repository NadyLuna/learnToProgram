Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

#utlizando funcionalidades aleatórias importando o módulo random

#Elaborando 3 listas: uma de verbos, uma de adjetivos e uma de substatntivos.

verbs =['Leverage', 'Sync', 'Target', 'Gamify' 'offline', 'cCrowd-sourced', '24/7', 'Lean-in', '30,00 foot']
adjectives =['A/B tested', 'Freemium', 'Hyperlocal', 'Siliod', 'B-to-B', 'Oriented', 'Cloud-based', 'API-based']
nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']

#escolhendo um verbo, um adjetivo e um substantivo de cada lista.

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun= random.choice(nouns)

#criando uma frase somando as palavras

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)