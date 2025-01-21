# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'

# The expression causes an error because 99 is an integer and cannot concatenate str and int. To fix it we convert the 99 in to str '99':
print('I have eaten ' + str(99) + ' burritos.')