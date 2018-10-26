import HuckelFunctions as hfc

exit = 1
while(exit == 1):                                                   #while loop for repeating the entire program
    print("\nWelcome to our Huckel Program!")

    compound_dic = {                                                #Dictionary for printing names more efficiently 
        1 : "length n poly-ene",                                    #Value of compound determines which compound to run.
        2 : "length n cyclic poly-ene",
        3 : "sp2-hybridised Platonic Solids"
    }

    while(1):                                                       #while loop to ensure user input is within the choices given
        compound = int(input('''                                    
    Please Choose your compound:
        1. length n poly-ene
        2. length n cyclic poly-ene
        3. sp2-hybridised Platonic Solids
    >>> '''))
        if compound >= 1 and compound <=3: 
            print("\n==============================================")
            break
        else:
            print("Please choose from the options above.")
            print("\n==============================================") 
           

    while(1):                                                       #while loop to ensure user input is within the choices given
        print("\nThis is the",compound_dic[compound],"program.")
        if compound <= 2:                                           #You only need to input the value of n for n-polyene and cyclic poly-ene
            n = int(input("Please choose the value of n : "))
            break
        elif compound == 3:                                         #You require the shape of the molecules for platonic solids.
            n = int(input('''
    Choose your platonic solid:
        1. Tetrahedron
        2. Cube
        3. Dodecahedron
        4. Octahedron
        5. Icosahedron
    >>>'''))
            if n<=5 and n>=1:
                break
            else:
                print("Please choose from the options above.")
            print("\n==============================================")

    

    if compound == 1:           #n-Polyene program
        print("\n",compound_dic[compound],", with n =",n,":\n")
        print(hfc.Hkl_Polyene(n))
        print("\nEigen values : \n\n", hfc.get_eig(hfc.Hkl_Polyene(n))[0])
        _dic = hfc.get_degen(hfc.Hkl_Polyene(n))
        key = list(_dic.keys()) 
        value = list(_dic.values())
        for i in range(0,len(_dic)):
            if key[i] <= 0:
                print(" E = α ",key[i], "β : ", value[i]," degeneracies", sep="")
            else:
                print(" E = α +",key[i], "β : ", value[i]," degeneracies", sep="")
        print("\nEigen vectors : \n\n", hfc.get_eig(hfc.Hkl_Polyene(n))[1])

    elif compound == 2:         #n-Cyclic polyene Program
        print("\n",compound_dic[compound],", with n =",n,":\n")
        print(hfc.Hkl_Cyclic(n))
        print("\nEigen values : \n\n", hfc.get_eig(hfc.Hkl_Cyclic(n))[0])
        _dic = hfc.get_degen(hfc.Hkl_Cyclic(n))
        key = list(_dic.keys()) 
        value = list(_dic.values())
        for i in range(0,len(_dic)):
            if key[i] <= 0:
                print(" E = α ",key[i], "β : ", value[i]," degeneracies", sep="")
            else:
                print(" E = α +",key[i], "β : ", value[i]," degeneracies", sep="")
        print("\nEigen vectors : \n\n", hfc.get_eig(hfc.Hkl_Cyclic(n))[1])

    elif compound == 3:         #Platonic Solid program
        print("\n",compound_dic[compound],", with n =",n,":\n")
        print(hfc.Hkl_Platonic(n))
        print("\nEigen values : \n\n", hfc.get_eig(hfc.Hkl_Platonic(n))[0])
        _dic = hfc.get_degen(hfc.Hkl_Platonic(n))                   #Dictionary for more efficient printing of two parallel lists.
        key = list(_dic.keys()) 
        value = list(_dic.values())
        for i in range(0,len(_dic)):
            if key[i] <= 0:
                print(" E = α ",key[i], "β : ", value[i]," degeneracies", sep="")
            else:
                print(" E = α +",key[i], "β : ", value[i]," degeneracies", sep="")
        print("\nEigen vectors : \n\n", hfc.get_eig(hfc.Hkl_Platonic(n))[1])
    print("\n==============================================")
    
    exit = int(input('''
Thank you for using this Huckel Program.

    Please choose what to do next:
        1. Go back to Start
        2. Exit
    >>>'''))
    print("\n==============================================")
