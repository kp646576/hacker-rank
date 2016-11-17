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
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var k = parseInt(n_temp[1]);
    a = readLine().split(' ');
    a = a.map(Number);
    
    s1(n, k, a);
}

// timeout too slow
function s0(n, k, a) {
    for (var i = 0; i < k % n; i++) {
        for (var j = 0; j < n - 1; j++){
            var tmp = a[j];
            a[j] = a[j + 1];
            a[j + 1] = tmp;
        }
    }
    console.log(a.toString().replace(/,/g, ' '));
}

function s1(n, k, a) {
    for (var i = 0; i < k % n; i++) {
        var tmp = a[0];
        a.splice(0, 1);
        a.splice(n - 1, 0, tmp);
    }
    console.log(a.toString().replace(/,/g, ' '));
}

function s2(n, k, a) {
    var s = '';
    for (var i = 0; i < n; i++) {
        s += a[(k + i) % n] + ' '
    }
    console.log(s.trim());
}