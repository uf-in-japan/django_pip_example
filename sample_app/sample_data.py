def generate():
    from receipts.models import Receipt, Item
    (receipt1 := Receipt()).save()
    (receipt2 := Receipt()).save()
    Item(description="Thing1", cost=55.9, receipt=receipt1).save()
    Item(description="Thing2", cost=10.1, receipt=receipt1).save()
    Item(description="Thing3", cost=9.99, receipt=receipt2).save()
    print("Other first time operations can go here. Need to add objects, for example?")
