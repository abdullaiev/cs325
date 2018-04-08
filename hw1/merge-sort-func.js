module.exports = function mergeSort(arr) {
    if (arr.length < 2) {
        return arr;
    }

    const middle = Math.floor(arr.length / 2);
    const left = arr.slice(0, middle);
    const right = arr.slice(middle, arr.length);
    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);
    return merge(sortedLeft, sortedRight);
};

function merge(left, right) {
    let results = [];

    while (left.length && right.length) {
        if (left[0] < right[0]) {
            shift(left);
        } else {
            shift(right);
        }
    }

    while (left.length) {
        shift(left);
    }

    while (right.length) {
        shift(right);
    }

    function shift(arr) {
        results.push(arr.shift());
    }

    return results;
}