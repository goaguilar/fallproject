// Helper functions for music

#include <cs50.h>
#include <math.h>
#include "helpers.h"
#include <string.h>

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int x = (fraction[0]) - '0';
    int y = (fraction[2]) - '0';

    //half note
    if(y == 2)
        return x * 4;
    //quarter note
    else if (y == 4)
        return x * 2;
    //whole note
    else if (y == 1)
        return x *8;
    //Assume rest are already in eighths
    else
        return x;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    //n represents the octave of the note
    double n = 0;
    //steps is the number of steps away from A
    double steps = 0;
    double tempnote = 440;
    //Checks if not has a sharp or a flat
    if(note[1] == '#' || note[1] == 'b'){
        n = note[2] - '4';
        tempnote = round(tempnote*pow(2,n));

        //for the case of the 2nd string being sharp
        if(note[1] == '#'){
            steps += 1;
            if(note[0] >= 'A' && note[0] <= 'B')
                steps += note[0] - 'A';
            else
                steps -= 'H' - note[0];
            return round(tempnote*pow(2,(steps/12)));
         }
        if(note[1] == 'b')
            steps -= 1;
            if(note[0] >= 'A' && note[0] <= 'B')
                steps += note[0] - 'A';
            else
                steps -= 'H' - note[0];
            return round(tempnote*pow(2,(steps/12)));
    }
    else
        //n represents the octave of the note
        n = note[1] - '4';
        tempnote = round(tempnote*pow(2,n));
        if(note[0] >= 'A' && note[0] <= 'B')
            steps += note[0] - 'A';
        else
            steps -= 'H' - note[0];
            return round(tempnote*pow(2,(steps/12)));

}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    // returns True is s is a line ending or nothing
    if(*s == '\n' || strcmp(s,"") == 0)
        return true;
    else
        return false;
}
