module.exports = function insertSort(arr) {
    if (arr.length < 2) {
        return arr;
    }

    for (let i = 1; i < arr.length; i++) {
        let key = arr[i];
        let j = i - 1;

        for (; j >= 0 && arr[j] > key; j--) {
            arr[j + 1] = arr[j];
        }

        arr[j + 1] = key;
    }

    return arr;
};
