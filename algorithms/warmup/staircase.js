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
    s1(n);


}

function s0(n) {
    var spaces;
    var hashes;
    
    for (var i = 1; i < n + 1; i++) {
        spaces = '';
        hashes = '';
        
        for (var j = 0; j < n - i; j++) {
            spaces += ' ';
        }
        for (var k = 0; k < i; k++) {
            hashes += '#'
        }
        
        console.log(spaces + hashes)
    }
}

function s1(n) {
    for (var i = 1; i < n + 1; i++) {
        console.log(' '.repeat(n - i) + '#'.repeat(i));
    }
}