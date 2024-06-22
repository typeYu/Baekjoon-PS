function solution(array) {
    midIndex = Math.floor(array.length / 2);
    array.sort((a, b) => a - b);
    return array[midIndex];
}