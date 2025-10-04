def modalane_fun(counting : int ) ->int :
    if(counting == 3):
        return    
    counting += 1
    print(f"{counting}")

    modalane_fun(counting)
    print(f"{counting}")

    modalane_fun(counting)

modalane_fun(0)