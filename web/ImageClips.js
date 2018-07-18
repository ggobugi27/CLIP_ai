const _ = require('lodash');
const fs = require('fs');
const dir = 'public/test2';

let currentFiles;
fs.readdir(dir, (err, files) => {
	currentFiles = files.filter(file => file.startsWith('face'))
})

const clipImages = (directory)=> {
	imageClips = []
	for (var i =0; i < currentFiles.length; i++){
	  let image = {
	    url : `./${directory}/${currentFiles[i]}`,
	    info : info[currentFiles[i].slice(4).split('.')[0]]
	  }
  	  imageClips.push(image);
	}
	return imageClips
}

module.exports = {clipImages}