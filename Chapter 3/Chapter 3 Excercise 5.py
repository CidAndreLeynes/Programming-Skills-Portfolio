guests=["Sierra","Sydney","Stelle","Topaz","Kamiya"]
for i in guests:
    print("Dear", i.title(),",", "Do you want to come over to my place for some dinner? \npls reply soon \nthankss")
    print("Though", guests[0], "can't go")
    del guests[0]
guests.append("Scylla")
