/*
* This module reads an input file, sorts the numbers by a given sorting method and stores the result into an output file.
*
*/

let fs = require('fs');
let mergeSort = require('./merge-sort-func');
let insertSort = require('./insert-sort-func');

module.exports = function (input, output, sortType) {
    //Read the data file
    let numbersArr = parseInputFile(input);
    //For each line of data file, sort the integers and write result into data file
    let result = sort(numbersArr, sortType);
    //Save the result
    fs.writeFileSync(output, result);
};

function parseInputFile(inputFile) {
    let numbers = [];
    let dataFile = fs.readFileSync(inputFile, 'utf8');

    dataFile.split('\n').forEach((line) => {
        let arr = line.split(' ');
        //remove the first integer from the line string because
        // it denotes the number of integers to sort and it not really needed in JS implementation
        arr.shift();

        //Cast strings to numbers
        for (let i = 0; i < arr.length; i++) {
            arr[i] = Number(arr[i]);
        }
        numbers.push(arr);
    });

    return numbers;
}

function sort(numbersArr, sortingMethod) {
    let result = '';

    numbersArr.forEach(arr => {
        switch (sortingMethod) {
            case 'merge':
                arr = mergeSort(arr);
                break;
            case 'insert':
                arr = insertSort(arr);
                break;
        }

        result += arr.join(' ');
        result += '\n';
    });

    return result;
}
