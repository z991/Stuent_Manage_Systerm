
'''import itertools
nums={x for x in range(1,10)}
sequence_3nums={p for p in itertools.permutations(nums,3) if sum(p)==15}
print(sequence_3nums)'''
class Dog(object):
    def __init__(self):
        print('Init the Dog')
        print(self)
dog_obj=Dog()

