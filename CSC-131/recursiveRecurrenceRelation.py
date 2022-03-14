test=int(input("What value should we test?"))

def recurrenceRelation(val):
    if val != 1:
        return (3*val-2+recurrenceRelation(val-1))
    else:
        return 8

print(recurrenceRelation(test))