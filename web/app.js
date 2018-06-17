const express = require('express');
const app = express();
const nunjucks = require('nunjucks');
const routes = require('./routes');
const fs = require('fs');
const path = require('path')
const mime = require('mime')



app.set('view engine', 'html'); // have res.render work with html files
app.engine('html', nunjucks.render); // when giving html files to res.render, tell it to use nunjucks
nunjucks.configure('views'); // point nunjucks to the proper directory for templates
//manually-wrtten static file middleware
// app.use(function(req, res, next){
// 	var mimeType = mime(req.path);
// 	fs.readFile('./public' + req.path, function(err, fileBuffer){
// 		if (err) return next();
// 		res.header('Content-Type', mimeType);
// 		res.send(fileBufferlookup);
// 	});
// });
var staticMiddleware = express.static(__dirname + '/public')
app.use(staticMiddleware);


app.use(routes);

var locals = {
    title: 'An Example',
    people: [
        { name: 'Gandalf'},
        { name: 'Frodo' },
        { name: 'Hermione'}
    ]
};

app.get('/', function(req, res){
	res.render('index', locals)
})


app.listen(3000, () => console.log('listening on port 3000'));