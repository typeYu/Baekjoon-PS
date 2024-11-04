function solution(sizes) {
    var width = []
    var height = []
    for (let i = 0; i < sizes.length; i++) {
        if (sizes[i][0] > sizes[i][1]) {
            width.push(sizes[i][0])
            height.push(sizes[i][1])
        }
        else {
            height.push(sizes[i][0])
            width.push(sizes[i][1])
        }
    }
    var answer = Math.max(...height) * Math.max(...width);
    return answer;
}