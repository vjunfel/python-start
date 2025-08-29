def calculate_love_score(name1, name2):
    T = 0
    R = 0
    U = 0
    E = 0
    L = 0
    O = 0
    V = 0
    
    combined_names = (name1 + name2).lower()
    print("Combined names:", combined_names)
    
    for l in (combined_names):
        if l == "t":
            T += 1
        elif l == "r":
            R += 1
        elif l == "u":
            U += 1
        elif l == "e":
            E += 1
        elif l == "l":
            L += 1
        elif l == "o":
            O += 1
        elif l == "v":
            V += 1
        else:
            continue
    
    TRUE = T + R + U + E 
    LOVE = L + O + V + E
    
    print("TRUE = ", TRUE)
    print("LOVE = ", LOVE)
    print(f"{TRUE}{LOVE}")
        
    
calculate_love_score("Kanye West", "Kim Kardashian") # 42
