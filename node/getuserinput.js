process.stdout.write("Hello. What is your name? ")

process.stdin.on('data', function(data) {
    console.log("Hello " + data.toString())
});