let mergeSort = require('./merge-sort-func');
let insertSort = require('./insert-sort-func');

executeTests('merge', 'sorted');
executeTests('merge', 'random');
executeTests('merge', 'reversed');
executeTests('insert', 'sorted');
executeTests('insert', 'random');
executeTests('insert', 'reversed');

function executeTests(algorithm, useCase) {
    let title = `${algorithm.toUpperCase()} RUNTIME TEST. NUMBERS IN THE ARRAY ARE ${useCase.toUpperCase()}.`;
    console.log(title);
    let func;

    switch (algorithm) {
        case 'merge':
            func = mergeSort;
            break;
        case 'insert':
            func = insertSort;
            break;
    }

    for (let i = 1; i <= 10; i++) {
        test(func, i * 10000, useCase);
    }
}

function test(algorithm, qty, useCase) {
    let name = 'Number of elements: ' + qty;
    let arr;


    switch (useCase) {
        case 'sorted':
            arr = generateSortedArray(qty);
            break;
        case 'reversed':
            arr = generateReversedArray(qty);
            break;
        default:
            arr = generateRandomNumbers(qty);
    }

    console.time(name);
    algorithm(arr);
    console.timeEnd(name);
}


function generateRandomNumbers(qty) {
    let arr = [];

    for (let i = 0; i < qty; i++) {
        arr.push(randomNumber(10000));
    }

    return arr;
}

function generateSortedArray(length) {
    let arr = [];

    for (let i = 0; i < length; i++) {
        arr.push(i);
    }

    return arr;
}

function generateReversedArray(length) {
    let arr = [];

    for (let i = length - 1; i >=0; i--) {
        arr.push(i);
    }

    return arr;
}

function randomNumber(max) {
    let random = Math.random() * Math.floor(max);
    return Math.floor(random);
}