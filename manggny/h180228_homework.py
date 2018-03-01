def homework(num_conti,num_break,all_range):
    if all_range < 2:
        return 0
    else:
        for i in range(all_range):
            if i == num_conti:
                continue
            elif i == num_break:
                break
            else:
                print(i)

homework(5,8,10)
            
