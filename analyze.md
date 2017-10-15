# Analyze This

## Questions

1a. Yes

1b. O(n), because step i. goes through n cards, ii. just adds 10 piles, iii. goes through the same n cards, and iv. adds 10 piles again.
The total for this is O(2n + 20), which is just O(n).

2a.Yes

2b. O(n^3), the algorithm would have 3 nested for loops, one making sure it goes through every element, one going forwards making swaps inside that, and one going backwards
making swaps inside that one.

3a. Yes

3b. O((nlogn)^2), assuming the worst case scenario is that the last card is the queen of hearts, the code has to perform a shuffle n times. Assuming a shuffle is basically a sort,
and that the complexity of the sort is typicaly nlogn, then the upper bound is n*nlogn.

## Debrief

1. Section Notes

2. 30 minutes
