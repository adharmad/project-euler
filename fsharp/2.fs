# light
// By considering the terms in the Fibonacci sequence whose values do not 
// exceed four million, find the sum of the even-valued terms.
// Each new term in the Fibonacci sequence is generated by adding the 
// previous two terms. By starting with 1 and 2, the first 10 terms will be:
//
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values do not 
// exceed four million, find the sum of the even-valued terms.


open System

let rec fib n =
    match n with 
    | 0 -> 1
    | 1 -> 1
    | _ -> fib (n-1) + fib (n-2) 

[<EntryPoint>]
let main (args : string[]) = 
    let mutable not_over = true
    let mutable sum = 0
    let mutable n = 1

    while not_over do
        let fib_n = fib n
        if fib_n < 4000000 then
            if fib_n%2 = 0 then
                sum <- sum + fib_n
            n <- n + 1
        else
            not_over <- false
    
    printfn "sum = %i" sum

    0
