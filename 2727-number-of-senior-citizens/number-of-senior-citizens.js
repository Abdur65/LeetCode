/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    let count = 0, age;
    for(let i = 0; i < details.length; i++)
    {
        age = Number(details[i][11]+details[i][12]);

        if (age > 60)
        {
            count += 1;
        }
    }

    return count;
};