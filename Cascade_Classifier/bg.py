import os

def create_pos_n_neg():
    for f in ['neg']:
        for i in os.listdir(f):
            if f == 'neg':
                line = f + '/' + i + '\n'
                with open('bg.txt', 'a') as fi:
                    fi.write(line)
 
            elif f == 'pos':
                line = f + '/' + i + '1 0 0 50 50\n'
                with open('info.dat', 'a') as fi:
                    fi.wrtie(line)

create_pos_n_neg()
