function solution(my_string) {
    const nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var answer = [];
    for (let i = 0; i < my_string.length; i++) {
        if (my_string[i] in nums) {
            answer.push(parseInt(my_string[i]))
        }
    }
    return answer.sort();
}