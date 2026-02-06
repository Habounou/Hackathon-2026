def check_all_substrings(big_string, small_strings):
    # Returns True only if every sub in small_strings is found in big_string
    return all(sub in big_string for sub in small_strings)

def verify(big_string, small_strings):
    if big_string == None :
        print("No string...")
        return
    
    if check_all_substrings(big_string, small_strings):
        print("All substrings were found!")
        print("Length : ", len(big_string))
    else:
        print("One or more substrings are missing.")

def read_frags(filename):
    frags = []
    with open(filename, "r",encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            if not line:
                continue
            if len(line) == 0:
                continue
            frags.append(line)
    return frags

def initialize():
    frags = read_frags("input_demo.txt") # input_demo input_level_1 input_level_2 input_level_3 input_level_4
    return frags

def reverse_shreddify(frags):
    
    # *** recommandation : écrire votre code ici ***

    return None


if __name__ == "__main__":
    frags = initialize()

    solution_naive = "".join(frags)
    print(solution_naive)
    verify(solution_naive, frags)

    good_solution = reverse_shreddify(frags)
    # Pour input_demo.txt la meilleure réponse (la plus courte string) est de longeur 53
    #good_solution = "Demain,_dès_l’aube,_à_l’heure_où_blanchit_la_campagne"
    print(good_solution)
    verify(good_solution, frags)

