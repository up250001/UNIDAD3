# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(f"The lenght of it companies is {len(it_companies)}")

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)

it_companies.discard("Youtube")
print(it_companies)

print("The discard() method removes the specified element from the set. Unlike the remove() method, discard() does not raise an error if the specified element is not present.")


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C)

print(A.intersection(B))
print(A.isdisjoint(B))

AB = A.union(B)
BA = B.union(A)
print(AB,BA)

print(A.symmetric_difference(B))

del A,B

age_list = [21, 19, 23, 25, 27, 20, 25, 20]

age_set = set(age_list)

if len(age_set) == len(age_list):
    print('The set and the list are equal')

elif len(age_set) > len(age_list):
    print('Set is bigger')

else:
    print('List is bigger')

'''
String: Text-based data.
List: Ordered, mutable collection of items.
Tuple: Ordered, immutable collection of items.
Set: Unordered collection of unique items.

'''

sentence = 'I am a teacher and I love to inspire and teach people'
words = set(sentence.split())
print(f'The number of unique words is {len(words)}')

