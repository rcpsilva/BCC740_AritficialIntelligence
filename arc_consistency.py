import copy as cp

def gac(N, C, to_do):
    
    while to_do:
        edge = to_do.pop(0)
        main_var = edge['var']
        remain_vars =  cp.copy(edge['constraint']['scope'])
        remain_vars.remove(main_var)

        domain = cp.copy(N[main_var])
        
        new_domain = []

        while domain:
            m_val = domain.pop(0)

            for r_var in remain_vars:
                
                if m_val in new_domain:
                    break

                for r_val in N[r_var]:
                    if edge['constraint']['c'](**{main_var:m_val ,r_var:r_val}):
                        new_domain.append(m_val)
                        break


        if N[main_var] != new_domain:
            N[main_var] = cp.copy(new_domain)
            c_name = edge['constraint']['c_name']
            for v in remain_vars: 
                for c in C:
                    if c['c_name'] != c_name and v in c['scope']:
                        for _v in c['scope']:
                            if _v != v:
                                to_do.append({'var':_v, 'constraint':c})

if __name__ == "__main__":
    variables = ['A','B','C']

    nodes = {'A':[1,2,3,4],
     'B':[1,2,3,4],
     'C':[1,2,3,4],
     'D':[1,2,3,4],
     'E':[1,2,3,4]}

    consts = [{'c_name':'C1', 'scope':['A','B'], 'c': lambda A,B : A > B},
        {'c_name':'C2', 'scope':['B','C'], 'c': lambda B,C : B == C},
        {'c_name':'C3', 'scope':['E','B'], 'c': lambda E,B : E > B},
        {'c_name':'C4', 'scope':['E','A'], 'c': lambda E,A : E < A}]

    to_do = [ {'var':v, 'constraint':c} for c in consts for v in c['scope']]

    for td in to_do:
        print(td)
    
    gac(nodes, consts, to_do)

    for n in nodes:
        print('{} : {}'.format(n,nodes[n]))



    
