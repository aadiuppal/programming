var fs = require('fs');
var path = require('path');

function get_files(dir,ext,call){
  var arr = []
  fs.readdir(dir,function callback(err,files){
      if (err){
        return call(err);
      }else{
         for(var i = 0;i<files.length;i++){
          if (path.extname(files[i]) == "."+ext){
            arr.push(files[i]);
          }
         }
      }
  call(null, arr);
  });
}
module.exports = get_files;
