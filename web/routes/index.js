const express = require('express');
const router = express.Router();	
const ImageClips = require('../ImageClips');

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

module.exports = () => {
  // a reusable function
  const respondWithAllImages = (req, res, next) => {
    let clips = ImageClips.clipImages('test2');
    clips.sort((a,b) => (a.info > b.info) ? 1 : ((b.info > a.info) ? -1 : 0)); 
    // console.log(clips)
    res.render('index', {
      title: 'CLIP.ai',
      imageList: clips,
      showForm: true,
      info: info,
    });
  };

  router.get('/', respondWithAllImages);

  router.post('/api/video', (req, res, next) => {
    const currentUrl = req.body.videoUrl;
    if (currentUrl) runPy(currentUrl, 'test2', 1)
    res.redirect('/');
  });
  return router;
};