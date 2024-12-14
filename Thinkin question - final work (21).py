def goodlist(list):
        if list[len(list) - 1] + 1 > 9:
            for i in range (len(list) -1 , 0 , -1):
                if list[len(list)-1] == 9:
                    list[len(list)-1] = 0
                    list[len(list) -2] = list[len(list) -2] + 1

                if list[i] > 9:
                    list[i] = 0
                    list[i - 1] = list[i-1] + 1
                if list[i-1] < 9:
                    break
        else:
            list[len(list) -1 ] = list[len(list) - 1] + 1
        return  list