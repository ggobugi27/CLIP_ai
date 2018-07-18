const express = require('express');
const router = express.Router();
const ImageClips = require('../ImageClips');
const runPy = require('./runPy')
const folderName = 'test2';

const respondWithAllImages = (req, res, next) => {
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

module.exports = router;