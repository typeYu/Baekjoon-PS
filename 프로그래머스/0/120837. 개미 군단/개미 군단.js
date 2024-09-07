function solution(hp) {
    let answer = 0;
    array = [5, 3, 1]
    for (let i = 0; i < array.length; i++) {
        quot = Math.floor(hp / array[i])
        answer += quot
        hp = hp % array[i]
    }
    return answer;
}