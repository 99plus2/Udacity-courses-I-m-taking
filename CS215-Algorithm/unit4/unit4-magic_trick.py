#            animal       speed   weight lifespan brain
#                          (mph)   (kg)  (years) mass (g)
animals = [("dog",          46,   35,     13,  280    ),
           ("elephant",     30, 3500,     50, 6250    ),
           ("frog",          5,    0.5,    8,    3    ),
           ("hippopotamus", 45, 1600,     45,  573    ),
           ("horse",        40,  385,     30, 642     ),
           ("human",        27,   80,     78, 2000    ),
           ("lion",         50,  250,     30,  454    ),
           ("mouse",         8,    0.025,  2,    0.625),
           ("rabbit",       25,    4,     12,   40    ), 
           ("shark",        26,  230,     20,   92    ),
           ("sparrow",      16,    0.024,  7,    2    )]



def import_rank(items,weights):
    names  = [item[0] for item in items]
    scores = [sum([a*b for (a,b) in zip(item[1:],weights)]) for item in items] 
    results = zip(scores,names)
    return sorted(results)
#weights can be change to whatever
weights =(.3,.6,.4,.8)
answer = import_rank(animals,weights)
for i in range(len(answer)):
    print answer[i][1], "(", answer[i][0], ")"


#notice which always come out at 4Th postion,no matter what weights you can to .