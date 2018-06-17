// const py = require('python-shell')

// Running a Python script:
var PythonShell = require('python-shell');
 
// PythonShell.run('my_script.py', function (err) {
  if (err) throw err;
  console.log('finished');
});
// If the script writes to stderr or exits with a non-zero code, an error will be thrown.

// Running a Python script with arguments and options:

var options = {
  mode: 'text',
  pythonPath: 'path/to/python',
  pythonOptions: ['-u'],
  scriptPath: 'path/to/my/scripts',
  args: ['value1', 'value2', 'value3']
};
 
// PythonShell.run('my_script.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});
// Exchanging data between Node and Python:
var PythonShell = require('python-shell');
var pyshell = new PythonShell('my_script.py');
 
// sends a message to the Python script via stdin
pyshell.send('hello');
 
pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});
 
// end the input stream and allow the process to exit
pyshell.end(function (err,code,signal) {
  if (err) throw err;
  console.log('The exit code was: ' + code);
  console.log('The exit signal was: ' + signal);
  console.log('finished');
  console.log('finished');
});