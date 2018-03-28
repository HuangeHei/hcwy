<template>
  <div class="add_user">
    <div class="add_user_head">
      <span class="page_title">人员入职申请表</span>  
    </div>
    <div class="add_user_body">
      <el-form ref="form" :model="form" label-width="100px" class="from_class">

        <el-form-item label="人员姓名">
          <el-col :span="4">
            <el-input v-model="form.user_name"></el-input>
          </el-col>
          <el-col class="el-form-item__label" :span="3">身份证号码</el-col>
          <el-col :span="7">
            <el-input v-model="form.user_id_number"></el-input>
          </el-col>
          <el-col class="el-form-item__label" :span="3">员工手机号码</el-col>
          <el-col :span="7">
            <el-input v-model="form.user_phone"></el-input>
          </el-col>
        </el-form-item>
        

        <el-form-item label="性别">
          <el-radio-group v-model="form.user_sex">
            <el-radio label="男"></el-radio>
            <el-radio label="女"></el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item label="员工职位">
          <el-select v-model="form.user_type" placeholder="选择入职职位">
            <el-option :label="item.type_name" :key="item.id" v-for="item in this.user_type"  :value="item.id"></el-option>
          </el-select>
        </el-form-item>

         <el-form-item label="审核类型">
          <el-select v-model="form.check_type" placeholder="选择审核类型">
            <el-option :label="item.process_name" :key="item.id" v-for="item in this.check_type"  :value="item.id"></el-option>
          </el-select>
        </el-form-item>
      
        <el-form-item label="人员履历">
          <el-input type="textarea" v-model="form.user_desc"></el-input>
        </el-form-item>

        <el-form-item label="员工入职照片">
          <upload :action="url" :filelist="form.img" ></upload>
        </el-form-item>

        <el-form-item label="身份证正反面">
          <upload :action="url" :filelist="form.id_img" ></upload>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSubmit">办理入职</el-button>
          <el-button>取消</el-button>
        </el-form-item>

      </el-form>
    </div>
  </div>
</template>

<script>

import { get_file_list,del_upload_img,push_list_data } from '../../common'
import upload from '../common/upload'

export default {
  name: 'add_user',
  data () {
    return {
      url:'http://127.0.0.1:8000/upload/',
      mb_ok:true,
      user_type:[],
      check_type:[],
      form: {
        user_sex:'',
        user_name: '',
        user_phone: '',
        id_img:[],
        img:[],
        user_id_number: '',
        user_type: '',
        user_desc: '',
        check_type:'',
      }
    }
  },
  methods:{
    onSubmit(){
      if(this.form.id_img.length != 2 || this.form.img.length != 1 ){
        this.$message.error('请检查上传的图片');
      }else{
        var params = new URLSearchParams(this.form);
        
        this.$http.post('http://127.0.0.1:8000/user/add_user',params).then(response => {
         
          if(response.data == 'ok'){
            this.mb_ok = false // 设置false 就表示已经提交了图片不用删除，否则 就删除
            this.$message({message: '添加成功',type: 'success'});
            this.$router.push('/index')  
          }else{
            this.$message.error('添加失败,服务器端错误');
          }
          
        }, response => {
            console.log(response);
        })
      }
    },

  },

  
  mounted(){
    this.$http.get('http://127.0.0.1:8000/user/add_user/').then(response => {
      this.user_type = push_list_data(response.data) 
    }, response => {  // 错误的返回
        console.log(response) 
    })

    this.$http.get('http://127.0.0.1:8000/getchecktype/').then(response => {
      this.check_type = push_list_data(response.data)
    }, response => {  // 错误的返回
        console.log(response) 
    })


  },
  beforeDestroy(){
    if(this.mb_ok){
      if(del_upload_img(this.form.id_img)||del_upload_img(this.form.img)){
        console.log("-删除成功")
      }else{
        console.log("-删除失败")
      }
    }
  },
  components:{
    upload
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .add_user{
    padding: 10px;
    width: 100%;
  }
  .add_user_head{
    height: 50px;
    text-indent: 30px;
    font-size: 30px;
    border-bottom: 1px solid #e6e6e6
  }
  .from_class{
      margin-top: 30px;
      width:1000px;
  }
  .span_class{
    text-align:right;
    padding: 0 12px 0 0;
  }

</style>
