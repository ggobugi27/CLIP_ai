const _ = require('lodash');
const fs = require('fs');
const dir = 'public/test2';

let currentFiles;
fs.readdir(dir, (err, files) => {
	currentFiles = files.filter(file => file.startsWith('face'))
})

info = {
	7: ['taeyang'],
	19: ['taeyang'],
	26: ['g dragon'],
	31: ['g dragon'],
	35: ['taeyang'],
	39: ['daesung'],
	47: ['taeyang'],
	48: ['taeyang'],
	52: ['daesung'],
	56: ['daesung'],
	62: ['taeyang'],
	63: ['g dragon'],
	64: ['g dragon'],
	81: ['daesung'],
	96: ['daesung'],
	102: ['g dragon'],
	110: ['g dragon'],
	111: ['g dragon'],
	119: ['daesung'],
	120: ['daesung'],
	132: ['g dragon'],
	143: ['taeyang'],
	149: ['g dragon'],
	151: ['daesung'],
	154: ['g dragon'],
	167: ['taeyang'],
	168: ['seungri'],
	170: ['taeyang'],
	172: ['seungri'],
	194: ['taeyang'],
	196: ['taeyang'],
	197: ['taeyang'],
	197: ['taeyang'],
	229: ['taeyang'],
	231: ['taeyang', 'seungri'],
	232: ['taeyang', 'seungri', 'g dragon', 'daesung', 'top'],
	233: ['seungri', 'taeyang', 'top'],
	234: ['taeyang'],
}

const clipImages = (directory)=> {
	console.log(currentFiles)
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