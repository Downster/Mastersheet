//Write a function choosePrimes(nums) that takes in an array of numbers as args.
//The function should return a new array containing the primes from the original array.
//A prime number is a number that is only divisible by 1 and itself.
//Hint: consider creating a helper function to check if a number is prime!

const isPrime = (num) => {
    if (num < 2) {
        //if its less than two
        return false
    }
    //return false
    for (let i = 2; i < num; i++) {
        //iterate through numbers from 2 up to num
        if (num % i === 0) {
            //return false
            return false
        }
    }
    return true;
    //if that doesnt happen return true
}

const choosePrimes = (nums) => {
    return nums.filter((el) => (isPrime(el)))
}

console.log(choosePrimes([36, 48, 9, 13, 19])); // [ 13, 19 ]
console.log(choosePrimes([5, 6, 4, 11, 2017])); // [ 5, 11, 2017 ]
