print("\n ZAD 1 \n")

my_dictionary = {
  "piekarnia": "p_list",
  "warzywniak": "w_list"
}

p_list = ['chleb', 'pączek', 'bułki']
w_list = ['marchew', 'seler', 'rukola']

ammount = [len(p_list + w_list)]

print("Idę do", ((list(my_dictionary.keys())[0]).title()), "i kupuję tam:")

for skladnik in p_list:
    print(skladnik.title())

print("\n")

print("Idę do", ((list(my_dictionary.keys())[1]).title()), "i kupuję tam:")

for skladnik in w_list:
  print(skladnik.title())

print("W sumie kupuję " + str(ammount), "składników")

print("\n ZAD 2 \n")

for a in range(1, 101):
    if a % 5 == 0:
        print(a)
    if a % 5 == 0:
        print(a ** 3)
        
