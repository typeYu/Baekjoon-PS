function solution(angle) {
    if (0 < angle && angle < 90) {
        var answer = 1;
    }
    else if (angle == 90) {
        var answer = 2;
    }
    else if (90 < angle && angle < 180) {
        var answer = 3;
    }
    else {
        var answer = 4;
    }
    
    return answer;
}