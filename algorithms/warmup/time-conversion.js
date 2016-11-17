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
    var time = readLine();
    
    s0(time);
}

function s0(time) {
    var arr = time.split(':');
    if (arr[2].substring(2) == 'PM') {
        if (parseInt(arr[0]) != 12) {
            time = parseInt(arr[0]) + 12 + time.substring(2);
        }
    } else if (parseInt(arr[0]) == 12) {
        time = '00' + time.substring(2);
    }

    console.log(time.substring(0, time.length - 2));
}