var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');
var ut_sec = os.uptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
var totalMemory = os.totalmem();
var totMemKB = totalMemory/1024;
var totMemMB = totMemKB/1024;
var freeMemory = os.freemem();
var freeMemKB = freeMemory/1024;
var freeMemMB = freeMemKB/1024;
var cpuCount = os.cpus().length;

ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
  
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;



http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime:${ut_hour} Hours; ${ut_min}Minutes; ${ut_sec}Seconds;</p>
            <p>Total Memory:${totMemMB} MB </p>
            <p>Free Memory:${freeMemMB} MB </p>
            <p>Number of CPUs:${cpuCount} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3030);

console.log("Server listening on port 3030");