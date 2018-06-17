const _ = require('lodash');

const fs = require('fs');
const dir = './public/sober';

var numImg;
fs.readdir(dir, (err, files) => {
  numImg = files.length;
});

const clipImages = (directory)=> {
	let imageClips = []
	for (var i =0; i < numImg; i++){
	  let image = {
	    url : `./${directory}/face${i+1}.jpg`,
	    info : ''
	  }
  	  imageClips.push(image);
	}
	return imageClips
}

module.exports = { clipImages, };