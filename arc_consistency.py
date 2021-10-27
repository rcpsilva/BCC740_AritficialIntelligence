import copy as cp

def gac(nodes, consts):
    
    to_do = [{'var':v, 'cons':c} for c in consts for v in c['scope']]
    gac2(nodes,consts,to_do)


def gac2(nodes, consts, to_do):

    while to_do:
        arc = to_do.pop(0)
        X = arc['var']
        Ys = cp.copy(arc['cons']['scope']) 
        Ys.remove(X)
        cons = arc['cons']

        ND = []
        Dx = cp.copy(nodes[X])

        while Dx:

            x_val = Dx.pop(0)

            for Yi in Ys:
                if x_val in ND:
                    break
                for y_val in nodes[Yi]:
                    if cons['cons'](**{X:x_val,Yi:y_val}):
                        ND.append(x_val)
                        break

        if ND != Dx:
            nodes[X] = cp.copy(ND)
            for c_prime in consts:
                if c_prime['name'] != cons['name'] and X in c_prime['scope']:
                    for Z in c_prime['scope']:
                        if Z != X:
                            to_do.append({'var':Z, 'cons':c_prime})

if __name__ == "__main__":
    
    nodes = {'A':[1,2,3,4],
            'B':[1,2,3,4],
            'C':[1,2,3,4],
            'D':[1,2,3,4]}

    consts = [{'name':'C1', 'scope':['A','B'], 'cons': lambda A,B : A > B },
             {'name':'C2','scope':['B','C'], 'cons': lambda B,C : B > C },
             {'name':'C3','scope':['C','D'], 'cons': lambda C,D : C == D }]

    for n in nodes:
        print('{} : {}'.format(n,nodes[n]))

    gac(nodes,consts)

    for n in nodes:
        print('{} : {}'.format(n,nodes[n]))
