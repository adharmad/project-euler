#light
// Find the largest prime factor of a composite number.
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ? 

open System

let isPrime n =
    let bound = int (System.Math.Sqrt(float n))
    seq {2 .. bound} |> Seq.exists (fun x -> n % x = 0) |> not

[<EntryPoint>]
let main (args : string[]) = 
    isPrime 1
    0
