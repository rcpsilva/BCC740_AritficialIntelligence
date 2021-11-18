import copy as cp

def prove_DC_TD(kb, querry):
    g = querry
    derivation = []
    while g:
        print(g)
        a = g.pop(0)
        if  a in kb['rules']:
           B = kb['rules'][a][0]
           g = B + g
           derivation.append({a:B})
        elif a in kb['askables']:
            if not ask_der(a,derivation):
                return 'Could not complete the proof for {}.'.format(a) 
        else:
            return 'Could not complete the proof for {}.'.format(a) 

    return 'Yes.'

def ask_der(askable, derivation=[]):

    idx = -1

    ans = input('Is {} true?'.format(askable))

    while ans in ['w','why','por quê','pq']:
        if idx <= -len(derivation):
            for head in derivation[0]:
                print('Because: {} <- {}'.format(head,' & '.join(derivation[0][head])))
                print('Beacause {} is what you have asked.'.format(head))
        else:
            d = derivation[idx]

            for head in d:
                print('Because: {} <- {}'.format(head,' & '.join(d[head])))
            idx -= 1

        ans = input('Is {} true?'.format(askable))

    return True if ans in ['sim','yes','y','s'] else False

def prove_DC_BU(kb):
    c = []

    ask_askables(kb)

    rule_selected = True

    while rule_selected:
        rule_selected = False
        for head in kb['rules']:
            if head not in c:
                if not kb['rules'][head][0]:
                    c.append(head)
                    rule_selected = True
                else:
                    for b in kb['rules'][head]:
                        if set(b).issubset(set(c)):
                            c.append(head)
                            rule_selected = True
                            break
    return c

def ask_askables(kb):
    for atom in kb['askables']:
        if ask(atom):
            kb['rules'][atom] = [[]]
            kb['askables'].remove(atom)

def printkb(kb):

    rules = kb['rules']

    print('Rules:')
    for r in rules:
        bodies = rules[r]
        for b in bodies:
            if b:
                print('{} <- {}'.format(r,' & '.join(b)))
            else:
                print('{}.'.format(r))
    
    print('Askables:')

    print(kb['askables'])

def ask(askable):
    ans = input('Is {} true?'.format(askable))
    return True if ans in ['sim','yes','y','s'] else False

def how(atom, kb):
    """ How was the atom "atom" proved

    """
    if kb['rules'][atom]:
        for b in kb['rules'][atom]:
            if not b:
                print('{} is a fact.'.format(atom))
            else:
                print('{} <- {}'.format(atom,' & '.join(b)))

def whynot(atom,kb):
    return prove_DC_TD(kb, [atom])

if __name__ == "__main__":

    kb = {  'rules': {'l1_b':[['l_off','f0_live']],
                    'f0_live':[['f1_live','i0_down']],
                    'f1_live':[['f2_live','i1_down']],
                    'f2_live':[['f_on']],
                    'f_on':[[]]},
            'askables':['i0_down','i1_down','l_off']}

    kb = {  'rules': {
    'a': [['b', 'c']],
    'b': [['g', 'e'],['d', 'e']],
    'c': [['e']],
    'd': [[]],
    'e': [[]],
    'f': [['g', 'a']]
    },
    'askables':[]}

    printkb(kb)

    #c = prove_DC_BU(kb)

    #print(c)

    #print(prove_DC_TD(kb,['a']))

    how('b',kb)

    print(whynot('b',kb))