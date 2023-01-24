

def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    loc = input("Enter location of vacuum (A/B): ") 
    status1 = input("Enter status of " + loc + ": ") 
    status2 = input("Enter status of other room: ")

    if loc == 'A':
        print("Vacuum is placed in Location A ")
        if status1 == '1':
            print("Location A is dirty. ")
            goal_state['A'] = '0'
            cost += 1                     
            print("Cost for cleaning A: " + str(cost))
            print("Location A has been cleaned.")

            if status2 == '1':
                print("Location B is dirty.")
                print("Moving RIGHT to the Location B. ")
                cost += 1                       
                print("Cost for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'
                cost += 1                       
                print("Cost for suck: " + str(cost))
                print("Location B has been cleaned. ")
            else:
                print("No action: " + str(cost))
                print("Location B is already clean.")

        if status1 == '0':
            print("Location A is already clean ")
            if status2 == '1':
                print("Location B is dirty.")
                print("Moving RIGHT to the Location B. ")
                cost += 1                      
                print("Cost for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'
                cost += 1                       
                print("Cost for suck: " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action: " + str(cost))
                print(cost)
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        if status1 == '1':
            print("Location B is dirty.")
            goal_state['B'] = '0'
            cost += 1  
            print("Cost for cleaning: " + str(cost))
            print("Location B has been cleaned.")

            if status2 == '1':
                print("Location A is dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  
                print("Cost for moving LEFT: " + str(cost))
                goal_state['A'] = '0'
                cost += 1 
                print("Cost for suck: " + str(cost))
                print("Location A has been cleaned.")

        else:
            print(cost)
            print("Location B is already clean.")

            if status2 == '1': 
                print("Location A is dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  
                print("Cost for moving LEFT: " + str(cost))
                goal_state['A'] = '0'
                cost += 1  
                print("Cost for suck: " + str(cost))
                print("Location A has been cleaned. ")
            else:
                print("No action: " + str(cost))
                print("Location A is already clean.")

 
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacuum_world()
