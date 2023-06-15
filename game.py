print("Welcome to maze.Your mission is to find the treasure.")
print('''   ___---___
                      .--         --.
                    ./               \.
                   /      o            \
                  /      ..       o     |
                 |     ;`         '.     |
                |      :           :      |
                |      `._       _.'      |
                |         ``--.-'  .-     |.
                .|              _.'|     |  :
               :  \         `--'--'     /    :
              :    \                   /      :
             :      `\               /'        :
            :         `--___   ___--'          :
           :                ---               _.'
           `-._              ~~/   \____...-'  `\
           :_. `----./        /       |``   . ._:
             :_:_:_: |__     ~~~   _.-`._:._:-'
                       /``````---``` \
                      /       |       \jgs
                 ____/        |        \___
          __.--''             |            ```---..__
         `\                  _|                    _.'
           `\           _.-''  `-._             _.'
             `\      .-'           `-._      _.'
               `\  .'                  `-._.'
                 `''')
print("START")

lr=input("L or R :".lower())
lr1=input("T or S :".lower())
lr2=input("K,B or Y :".lower())

if lr=="L":
    if lr1=="T":
        if lr2=="Y":
            print("You win")
        elif lr2=="K":
            print("You are dead.")
        elif lr2=="B":
            print("You are dead")
    elif lr1=="S":
        print("You are dead.")
elif lr=="R":
    print("You are dead")
else:
    print("Game Over")
       
