const express = require('express');
const router = express.Router();
const ImageClips = require('../ImageClips');
const runPy = require('./runPy')
const folderName = 'test2';//hardcoded

module.exports = router;
console.log('something')

const respondWithAllImages = (req, res, next) => {
  console.log('aa')
  let clips = ImageClips.clipImages(folderName);
  clips.sort((a,b) => (a.info > b.info) ? 1 : ((b.info > a.info) ? -1 : 0)); 
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
  if (currentUrl) runPy(currentUrl, folderName, 1)
  res.redirect('/');
});

router.use((req, res, next) => {
  const error = new Error('Not Found')
  error.status = 404
  next(error)
})
