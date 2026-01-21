/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    var sum_char = 0;
    for(let i = 0; i < s.length-1; i++)
    {
        sum_char += Math.abs(s.charCodeAt(i) - s.charCodeAt(i+1));
    }

    return sum_char;
};