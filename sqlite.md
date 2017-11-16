# SQLite Music

## Questions

2.1. When importing a table into a table with not enough rows, the foreign keys is added to track the leftover rows and their table of origin

2.2. AlbumID is unique to the album table. If we were to import rows from album into artist, artist doesnt have any foreign key to keep track
of the extra rows

2.3. CustomerId become an alias for the rowid column and makes sorting the data quicker

2.4. SELECT sum(Total) AS "Total" FROM "Invoice" WHERE strftime('%Y', InvoiceDate) = '2010'

2.5. SELECT Name FROM Track WHERE
        (SELECT TrackId FROM InvoiceLine WHERE
            (SELECT InvoiceId FROM "Invoice" WHERE CustomerId = 50))

2.6. * Assuming that the duplicate values are examples like
Adam Clayton, Bono, Larry Mullen & The Edge
Adam Clayton, Bono, Larry Mullen, The Edge
where its the same artist but small changes, and assuming question just asks for a general plan
1. Group and select tracks with similar composers using the % wildcard
2. Overwrite all of the tracks' composers by using one composer from the group


## Debrief

a. sqlite stackoverflow

b. 40 minutes
