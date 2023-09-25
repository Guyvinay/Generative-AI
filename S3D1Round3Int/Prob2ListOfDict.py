employees = [
    {'name':'John','salary':3000,'designation':'developer'},
    {'name':'Emma','salary':4500,'designation':'manager'},
    {'name':'Kelly','salary':3500,'designation':'tester'},
    {'name':'Dom','salary':1500,'designation':'tester'},
    {'name':'Tess','salary':7500,'designation':'tester'},
    {'name':'Tezz','salary':9500,'designation':'tester'},
    {'name':'Sully','salary':4500,'designation':'tester'},
]

max = 0
ans = {}
for ent in employees:
    if ent['salary'] > max :
        max = ent['salary']
        ans = ent
print(f"Employee with maximum salary is: {max}")
print(ans)