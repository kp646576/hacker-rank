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
    var n = parseInt(readLine());
    var a = [];
    for(a_i = 0; a_i < n; a_i++){
       a[a_i] = readLine().split(' ');
       a[a_i] = a[a_i].map(Number);
    }
    
    s0(n, a);
}

function s0(n, a) {
    // How do you calculate the matrix diagonals?
    // 1x1: 0,0 | 0,0 
    // 2x2: 0,0 1,1 | 0,1 1,0
    // 3x3: 0,0 1,1 2,2 | 0,2 1,1 2,0
    // ltr [i][i] | rtl [i][n - 1 - i]
    var ltr = 0;
    var rtl = 0;
    
    for (var i = 0; i < n; i++) {
        ltr += a[i][i];
        rtl += a[i][n - 1 - i];
    }
    
    console.log(Math.abs(rtl - ltr));
}