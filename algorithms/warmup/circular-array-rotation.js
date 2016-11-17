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
    var q = parseInt(n_temp[2]);
    a = readLine().split(' ');
    a = a.map(Number);
    
    s0(n, k, q, a);
    
   

}

function s0(n, k, q, a) {
    // rotate a 'k' times (n is the number of elements in a)
    for (var i = 0; i < k; i++) {
        a.splice(0, 0, a[n - 1])
        a.splice(n, 1);
    }

    for(var a0 = 0; a0 < q; a0++){
        var m = parseInt(readLine());
        // log the query of index m
        console.log(a[m]);
    }
}