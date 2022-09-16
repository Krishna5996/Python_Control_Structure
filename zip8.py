questions = ['name', 'colour', 'shape']
answers = ['apple', 'red' ]
 
# using zip() to combine two containers
# and print values
for i, j in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(i, j))
