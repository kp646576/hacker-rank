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
    arr = readLine().split(' ');
    arr = arr.map(Number);
    
    var neg = 0;
    var zero = 0;
    var pos = 0;
    
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0)
            neg++;
        else if (arr[i] > 0)
            pos++;
        else 
            zero++;
    }
    
    console.log((pos * 1.0 / n).toFixed(6));
    console.log((neg * 1.0 / n).toFixed(6));
    console.log((zero * 1.0 / n).toFixed(6));

}