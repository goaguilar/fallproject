# #functions

## Questions

1. There are many words that start with the same letter in the alphabet. This hash function will be
mapped out with multiple collisions, meaning any hash table implemented with this would have to place
multiple words with the same hash output.

2. Ideally each string would have their own distinct arrangements of words so the hash function would give a unique output for
each word. But there could be many words that have different arangements but whose outputs would be the same.

3. To save space, you don't have to bring up each individual jpg file to take up memory because you only need to check
the hash value which is 256 bits.

4. In a trie table, the complexity only depends on the string's length, if the next character in the string is not found in the corresponging
node, the search terminates without checking the rest of the string. For a hash table, you have to generate the hash output, then compare that
to the corresponding index in the hash table, not accounting for the fact that there could be strings that have the same hash output.

## Debrief

1. None

2. 30
