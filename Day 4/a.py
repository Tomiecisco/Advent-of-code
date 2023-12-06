cards = []

def splitter():
    tot_score = 0
    for outcome in cards:
        score =  0
        elf_out = outcome[0].split()
        my_out = outcome[1].split()
        for i in my_out:
            if i in elf_out:
                score = 1 if score == 0 else score *2 
        tot_score += score

    return(tot_score)
def main():
    with open("Day 4\input.txt", 'r') as reader:
       for line in reader.readlines():
          card = line.strip().split(':')
          card.pop(0)
          cards.append(card[0].split('|'))
    print(splitter())
   
       

if __name__ == "__main__":
    main()


