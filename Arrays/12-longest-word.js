/*

Write a function `longestWord(sentence)` that takes in a sentence string as an
argument. The function should return the longest word in the sentence.

You must use  `Array.forEach` in your solution.

Solve this using Array's `forEach()`, `map()`, `filter()` **OR** `reduce()`
methods.

Examples:

console.log(longestWord('where did everyone go')); // 'everyone'
console.log(longestWord('prefer simplicity over complexity')); // 'simplicity'
console.log(longestWord('')); // ''

*/

function longestWord(sentence) {
    if (sentence !== '') {
        let splitString = sentence.split(" ")
        return splitString.reduce((output, currentEl) => {
            (currentEl.length > output.length) ? output = currentEl : null
            return output
        }, '')
    } else {
        return ''
    }
}
console.log(longestWord('where did everyone go'))
console.log(longestWord('prefer simplicity over complexity'))
console.log(longestWord(''))


/**************DO NOT MODIFY ANYTHING UNDER THIS  LINE*****************/

try {
    module.exports = longestWord;
} catch (e) {
    module.exports = null;
}
