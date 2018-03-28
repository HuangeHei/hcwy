<template>
  <div class="upload">
    <el-upload
        class="upload-demo"
        :action="action"
        :with-credentials='true' 
        :on-remove="del_img_to_list"
        :on-success="push_img_to_list"
        list-type="picture">
        <el-button size="small" type="primary">点击上传</el-button>
    </el-upload>
  </div>
</template>

<script>
import {del_upload_img}  from '../../common'
export default {
  name: 'upload',
  data () {
    return {
      del_img_list:[]
    }
  },
  props:["action","filelist"],
  methods:{
    del_img_to_list(file, fileList) {
      this.del_img_list.push(file.response.name) // 把删除的文件放到一个列表 等这个销毁的时候 提交到后台进行删除
      this.filelist.remove(file.response.name); // 可以在这里做一个post 到服务器去删除
    },
    push_img_to_list(response, file, fileList){
      this.filelist.push(response.name)
    },
  },
  beforeDestroy(){
    if(this.del_img_list.length > 0){
      if(del_upload_img(this.del_img_list)){
        console.log("删除成功")
      }else{
        console.log("删除失败")
      }
    }
  },

  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
