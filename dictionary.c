// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>

#include "dictionary.h"

//define the size of the hashtable to be larger than 143,091
# define tablesize 150000;
//global variable for the size of the dictionary
int size = 0

//hash function djb2 http://www.cse.yorku.ca/~oz/hash.html
unsigned long
hash(unsigned char *str)
{
    unsigned long hash = 5381;
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}

// using nodes for a link list
typedef struct node
{
    //creates a character array with a max size of the max word length
    char word[LENGTH+1];
    //pointer to next node in the list
    struct node* next;
}
node;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    if (table[hash(word)] != NULL)
    {
        if(strcmp(table[hash(word)],word) = 0)
        return true;
    }
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    //opens up dictionary, taken from speller.c
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
        return false;

    //opens up the file
    whie(fscanf(file, "%s\n", word)!= EOF)
    {
        //allocated resources for node
        node* newdictword = malloc(sizeof(node));
        //copys the word from the file into the node
        strcpy(newdictword->word, word);
        //puts the node in the dictionary table at the hash created index
        table[hash(word)] = newdictword;
        //sets the next pointer for the node to be null
        newdictword->next = NULL;
        //increment size of dictionary table
        size++;
    }
    //closes the file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if(size > 0)
        return size;
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    int i = 0;
    while(i < size)
    {
        table[i] = table[i]->next;
        free(table[i]);
        return true;
    }
    return false;
}
