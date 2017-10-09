# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

Invented word of lung disease caused by fine ash ad dust

## According to its man page, what does `getrusage` do?

Returns resource usage measure for who, which can be the calling process, the chidren of the calling process, or the calling thread

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

So that we can use the -> to reference a value in the struct.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.
Loads the dictionary, calculating the loading time. Spell checks each word in the text, ignoring words with numbers in them or words that are too long.
Determine the dictionary size and unload the dictionary. calculating the time for each action. Report if there are error. If not, then report on the benchmarks.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

If we used fscanf, we would get EOF added to the string as well.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

So that we dont modify the characters or words that we are inputting into the function
