# Now Boarding

## Questions

1.

```c
typedef struct
{
    struct passenger *person;
    struct pqueue *next;
}
pqueue;
```

2. 1 Check the passenger's group
   2 If the passenger is in group 1, add the person to the front of pqueue.
     a. Make the pointer to the first node in pqueue point to the passenger
     b. Make the pointer for *next be to the previous first node of pqueue
   3 If the passenger is in group 2, add the person to the back of pqueueu
     a. Make the pointer in the last node in pqueue point to the passenger
     b. Make the pointer for *next be NULL
   4 return the pointer for the first node in pqueue

3. O(1) because it is an insertion, you have to go to either the first or last element in the linked list and modify the pointers.

4. //Assuming only dequeueing one person
   1 Check the group that needs a passenger to be dequeued from.
   2 If it is group 1, remove a person from the front of pqueue.
     a. Make the pointer to the first node in pqueue point to the next passenger instead of this one
     b. Delete the passenger
   3 If it is group 2, remove the person to the back of pqueueu
     a. Make the pointer in the second to last node in pqueue point to NUL
     b. Delete the last passenger
   4 return the pointer for the first node in pqueue

5. Also O(1) as it is a deletion, you go to either the first or the last position and delete the passenger there, only modifying the pointer to
point to the next or previous passenger.

## Debrief

1. None

2. 25
