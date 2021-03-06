def warn_the_sheep(queue):
    if queue.pop() == 'wolf':
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number "+str(queue[::-1].index('wolf')+1)+"! You are about to be eaten by a wolf!"
