def who_doesnt_see(participants):
    list_of_people_that_dont_see = []
    for i in range(0, len(participants), 1):
        for j in range(0, len(participants[i]), 1):
            for k in range(0, i, 1):
                if participants[i][j] <= participants[k][j]:
                    list_of_people_that_dont_see.append((i,j))
                    break
    return list_of_people_that_dont_see

print(who_doesnt_see([[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]]))