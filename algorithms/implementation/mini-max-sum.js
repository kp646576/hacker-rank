process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var a_temp = readLine().split(' ');
    var a = parseInt(a_temp[0]);
    var b = parseInt(a_temp[1]);
    var c = parseInt(a_temp[2]);
    var d = parseInt(a_temp[3]);
    var e = parseInt(a_temp[4]);
    
    var min = Math.min(a, b, c, d, e);
    var max = Math.max(a, b, c, d, e);
    var sum = a + b + c + d + e;
    console.log(sum - max, sum - min)
}

/* 
 Sort (first 4, last 4)

 Find min/ max values subtract from sum

 Find all possible additions
 
 Hard code since small sample size
*/
