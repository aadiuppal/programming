//1
//console.log("HELLO WORLD");

//2
//var nums = process.argv
//var s = 0;
//for (var i = 2;i<nums.length;i++){
//  s += Number(nums[i]);
//}
//console.log(s)

//3
//var fs = require('fs');
//var buf = new Buffer(fs.readFileSync(process.argv[2]));
//var l = buf.toString().split("\n").length-1;
//console.log(l);

//4
//var fs = require('fs');
//fs.readFile(process.argv[2],function callback(err,data) {
//    if (err){
//      console.log("error reading file");
//    }else{
//      console.log(data.toString().split("\n").length-1);
//    }
//});

//5
//var fs = require('fs');
//var path = require('path');
//fs.readdir(process.argv[2],function callback(err,files){
//    if (err){
//      console.log("error getting files");
//    }else{
//      for(var i=0;i<files.length;i++){
//        if (path.extname(files[i]) == "."+process.argv[3]){
//            console.log(files[i]);
//        }
//      }
//    }
//});

//6
//var mymodule = require('./mymodule');
//mymodule(process.argv[2],process.argv[3],callback);
//function callback(err,data){
//  if (err){
//    console.log('error');
//  }else{
//    for(var i =0;i<data.length;i++){
//      console.log(data[i]);
//    }
//  }
//}

//7
//var http = require('http');
//http.get(process.argv[2],function callback(res){
//  //console.log(res.statusCode);
//  res.setEncoding('utf8')
//  res.on('data',function call(d){
//      console.log(d);
//});
//});

//8
//var http = require('http');
//var bl = require('bl');
//http.get(process.argv[2],function callback(res){
//        res.setEncoding('utf8');
//        res.pipe(bl(function(err,data){
//          console.log(data.toString().length);
//          console.log(data.toString());
//        }));
//});

//9
//var http = require('http');
//var bl = require('bl');
//var count = 2;
//var arr = [];
//function get_data(url){
//  var dat = "";
//  var req = http.get(url,function (res){
//    res.setEncoding('utf8');
//    res.on('data',function (d) {
//      dat += d;
//    });
//    res.on('end',function () {
//      arr.push(dat);
//      if (count < 4){
//        count += 1;
//        get_data(process.argv[count]);
//      }else{
//        for (var i = 0 ;i< arr.length;i++){
//          console.log(arr[i]);
//        }
//      }
//    });
//  res.on('error',function (e) {
//   console.log(e);
//  });
//  });
//
//}
//get_data(process.argv[2]);

//10
//var net = require('net');
//var server = net.createServer( function(c){
//  var d = "";
//  var date = new Date();
//  d +=   date.getFullYear()+"-";
//  d +=   ("0"+(date.getMonth()+1)).slice(-2)+"-";
//  d +=   ("0"+date.getDate()).slice(-2)+" ";
//  d +=   ("0"+date.getHours()).slice(-2)+":";
//  d +=   ("0"+date.getMinutes()).slice(-2);
//  c.write(d+"\n");
//  c.end();
//  c.on('end',function(){
//    console.log('end');
//   });
//});
//server.listen(process.argv[2],function(){
//  console.log("listen");
//});

//11
var http = require('http');
var fs = require('fs');
var src = fs.createReadStream(process.argv[3],{encoding:'utf8'});
var server = http.createServer(function (request,response){
  src.pipe(response);
});
server.listen(process.argv[2]);
