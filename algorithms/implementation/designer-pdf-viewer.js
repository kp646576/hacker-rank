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
    h = readLine().split(' ');
    h = h.map(Number);
    var word = readLine();
    var l = word.length
    var a = 'a'.charCodeAt();
    var hmax = 0;

    for (i = 0; i < l; i++) {
        index = word[i].charCodeAt() - a;
        curh = h[index];
        if (hmax < curh) {
            hmax = curh;
        }
    }
    
    console.log(hmax * l);
}
