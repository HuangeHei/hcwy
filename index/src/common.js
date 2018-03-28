import axios from 'axios'

export function get_file_list(fileList){
    var ret_list = []
    console.log('测试一波',fileList[0].response.name)
    for(var i=0; i < fileList.length;i++){
        ret_list.push(fileList[i].response.name)
    }
    return ret_list
}


export function del_upload_img(fileList){
    var params = new URLSearchParams({'del_img_list':fileList});
    axios.post('http://127.0.0.1:8000/delupload/',params).then(response => {
      if(response.data == 'ok'){
        return true
      }
    }, response => {
      console.log(response);
    })
}

export function push_list_data(data){
  /* 一个将django  serializers 的数据转换成 list 返回*/
  var ret_list = []
  for(var i=0;i < data.length;i++){
    var is_data = data[i].fields
    is_data['id'] = data[i].pk
    ret_list.push(is_data)
  }
  return ret_list
}