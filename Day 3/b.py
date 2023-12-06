eng_sche = []
total = 0
def grab_full_number(cell, row):
    """Retrieve the full number starting from the specified position with given steps."""
    number = []

    i = cell

    # Check left side
    while i >= 0:
        if str(eng_sche[row][i]).isdigit():
            number.insert(0, eng_sche[row][i])
            i -= 1
            continue

        break

    z = cell + 1
    # Check right side
    while z < len(eng_sche[row]):
        if str(eng_sche[row][z]).isdigit():
            number.append(eng_sche[row][z])
            z += 1
            continue

        break

    return (int(''.join(number)))
def searcher():
    total = 0
    for i, j in enumerate(eng_sche):
        for k, l in enumerate(j):
            if l == '*':
                numbers = []
                if find_adj_u(i,k).isdigit():
                    numbers.append(grab_full_number(k, i - 1))   
                    
                elif findadj_ul(i,k).isdigit() or findadj_ur(i,k).isdigit():  
                    if findadj_ul(i,k).isdigit():
                        numbers.append(grab_full_number(k - 1, i - 1))

                    if findadj_ur(i,k).isdigit():
                       numbers.append(grab_full_number(k + 1, i - 1))

                if find_adj_b(i,k).isdigit():
                    numbers.append(grab_full_number(k, i + 1))
                elif findadj_bl(i,k).isdigit() or findadj_br(i,k).isdigit():  
                    if findadj_bl(i,k).isdigit():
                        numbers.append(grab_full_number(k - 1, i + 1))

                    if findadj_br(i,k).isdigit():
                        numbers.append(grab_full_number(k + 1, i + 1))
                if find_adj_l(i,k).isdigit():
                    numbers.append(grab_full_number(k-1, i))
                if find_adj_r(i,k).isdigit():
                    numbers.append(grab_full_number(k+1, i))
                
                if len(numbers) != 2:
                     total+= 0

                else:
                    total += numbers[0] * numbers[1]

   
        
    return total
                

def find_adj_l(i, k):
    if k != 0:
        return eng_sche[i][k-1]
    else:
        return '.'   

def find_adj_r(i, k):
    if k != len(eng_sche[i]) -1:
        return  eng_sche[i][k+1]
    else:
        return '.'   
    
def find_adj_b(i, k):
    if i != len(eng_sche)-1:
        return  eng_sche[i+1][k]
    else:
        return '.'
    
def find_adj_u(i, k):
    if i != 0:
        return eng_sche[i-1][k]
    else:
        return '.'   
    
def findadj_ul(i,k):
    if i != 0 and k !=0:
        return eng_sche[i-1][k-1]
    else:
        return '.'
    
def findadj_ur(i,k):
    if i != 0 and k != len(eng_sche[i]) -1:
        return eng_sche[i-1][k+1]
    else:
        return '.'

def findadj_bl(i,k):
    if i != len(eng_sche)-1 and k!=0:
        return  eng_sche[i+1][k-1]
    else:
        return '.'

def findadj_br(i,k):
   if i != len(eng_sche)-1 and len(eng_sche[i]) -1:
        return  eng_sche[i+1][k+1]
   else:
        return '.'




def main():
    with open("Day 3\input.txt", 'r') as reader:
       for line in reader.readlines():
           eng_sche.append(list(line.strip()))
    print(searcher())
       

if __name__ == "__main__":
    main()