#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n)

b)
O(n log n)

c)
O(n)

## Exercise II

While there are more than one floor
Find the halfway point between floor 1 and floor n
Drop and egg
If the egg breaks it means we are too high.
Set the new highest floor to this current 'middle' floor
and we find the new halfway point between floor 1 and the new highest floor
Keep halving the amount of floors and dropping eggs until we are down to one floor or the egg doesnt break
In which case we have our floor f

Runtime complexity for this solution would be O(log n)
