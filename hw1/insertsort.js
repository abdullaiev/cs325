/*
 * This module invokes the sort function that takes care of I/O and invoking the given sorting algorithm on input data.
 * See insert-sort-func.js file for the implementation of the insertion sort.
 * See sort.js file for the I/O and insert-sort-func invocation.
 */

let sort = require('./sort');
sort('data.txt', 'insert.out', 'insert');