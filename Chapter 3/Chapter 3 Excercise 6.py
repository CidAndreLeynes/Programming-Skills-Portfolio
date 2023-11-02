guests=["Sierra","Sydney","Stelle","Topaz","Kamiya"]
for i in guests:
    print("Dear", i.title(),",", "Do you want to come over to my place for some dinner? \npls reply soon \nthankss")
    print("Though", guests[0], "can't go")
    del guests[0]
guests.append("Scylla")
for i in guests:
    print("Dear", i.title(),",", "Do you want to come over to my place for some dinner? \npls reply soon \nthankss")    
print("Nevermind, I can only invite two girls")
No=[]
No.append(guests[0])
guests.pop(0)
No.append(guests[2])
guests.pop(2)
No.append(guests[1])
guests.pop(1)
print("Hello"+i.title()+"Sorry, as much as I want to have a harem, Mom said no harems")
print()