const express = require('express');
const router = express.Router();	
const ImageClips = require('../ImageClips');


router.get('/', function(req, res, next){
	let clips = ImageClips.clipImages('sober');
	res.render('index', {imageList: clips })
});

router.get('/stylesheets/style.css', function(req, res, next){
	res.sendFile('/stylesheets/style.css', {root: __dirname + '/public'});

});

module.exports = router;