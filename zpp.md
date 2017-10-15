# Z++

## Questions

1.

```
function subtract($x, $y){
    $x <- add($x, -$y)
    return($x)
}
```

2.

```
function multiply($x, $y){
    $counter <- $y
    $sum <- 0
    while($counter){
        $sum <- add($sum, $x)
        $counter <- add($counter, -1)
    }
    return($sum)
}
```

3.

```
function multiply($x, $y){

    if($y){
        $y <- add($y, -1)
        //recursion
        multiply($x,$y)
    }
    return($x)
}
```

## Debrief

1. None

2. 40 minutes
