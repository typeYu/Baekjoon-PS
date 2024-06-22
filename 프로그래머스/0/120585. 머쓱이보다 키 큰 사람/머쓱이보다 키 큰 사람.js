function solution(array, height) {
    array.push(height);
    array.sort((a, b) => b - a);
    for (let i = 0; i < array.length; i++) {
        if (array[i] == height) {
            return i;
        }
    }
}