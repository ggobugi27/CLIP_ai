// Running a Python script:
var PythonShell = require('python-shell');
let info = {}
let runPy = (videoUrl, name = 'test1', interval=10) => {
  var options = {
    mode: 'text',
    pythonPath: '/usr/local/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '/Users/kateyun/Desktop/Fullstack/Senior-Phase/Stackathon/CLIP_ai/image_process',
    args: [videoUrl, name, interval]
  };
  let pyshell = new PythonShell('main.py', options)

  pyshell.send(options); // path, args etc
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
    if(message.startsWith('frame')) info[message[6]] = message.slice(7)
  });
  pyshell.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('finished');
    console.log('finished');
  });
}

module.exports = runPy;