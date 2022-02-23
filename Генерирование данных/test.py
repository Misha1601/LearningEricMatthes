def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list0 = []

    m = n = 0

    while n < len(list1) and m < len(list2):
        if list1[n] <= list2[m]:
            list0.append(list1[n])
            n += 1
            print(n)
        else:
            list0.append(list2[m])
            m += 1
            print(m)


    if n < len(list1):
        list0 += list1[n:]
    if m < len(list2):
        list0 += list2[m:]

    print(list0)
