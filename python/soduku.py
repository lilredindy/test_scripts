def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
print (squares)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
print(unitlist)
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
print (units)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

