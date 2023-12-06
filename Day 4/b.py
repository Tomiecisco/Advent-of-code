cards = []
instances = []

def splitter():
    for index, outcome in enumerate(cards):
        elf_out = outcome[0].split()
        my_out = outcome[1].split()
        matchs = 0
        for i in my_out:
            if i in elf_out:
                matchs += 1
        
        if instances[index] > 1:
            p=0
            while p < instances[index]:
                add = matchs
                j = index + 1
                for i in range(0,matchs):
                    instances[j]=instances[j] + 1  
                    add -= 1
                    j+=1
                p+=1
        else:
            add = matchs
            j = index + 1
            for i in range(0,matchs):
                instances[j]=instances[j] + 1  
                add -= 1
                j+=1
            

    return(instances)

def main():
    with open("Day 4\input.txt", 'r') as reader:
       for line in reader.readlines():
          card = line.strip().split(':')
          card.pop(0)
          cards.append(card[0].split('|'))
          instances.append(1)
    print(sum(splitter()))
   
       

if __name__ == "__main__":
    main()

