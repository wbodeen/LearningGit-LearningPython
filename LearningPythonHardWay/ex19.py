def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("Or, we can use variables from our script:")
cheese_count = 10
boxes_of_crackers = 50

cheese_and_crackers(cheese_count,boxes_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(cheese_count+100, boxes_of_crackers+1000)
