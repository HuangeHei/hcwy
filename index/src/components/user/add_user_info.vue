<template>
  <div class="add_user_info">
    <div class="add_user_info_head">
      <span class="page_title">添加人员信息</span>  
    </div>
    <div class="add_user_info_body">
      <div class="user_info">
        <table>
          <tr>
            <td class="td_title"><span>姓名</span></td>
            <td class="td_body"><el-input  v-model="this.user_info.user_name"></el-input></td>
            <td class="td_title"><span>身份证</span></td>
            <td class="td_body"><el-input  v-model="this.user_info.user_sex"></el-input></td>
            <!--<img :src="this.user_info.user_img" width="75" height="100"/>-->
          </tr>
           <tr>
            <td class="td_title"><span>人员职位</span></td>
            <td class="td_body"><el-input  v-model="this.user_info.user_type" ></el-input></td>
            <td class="td_title"><span>联系方式</span></td>
            <td class="td_body"> <el-input  v-model="this.user_info.user_phone" ></el-input></td>
          </tr>
          <tr>
            <td class="td_title"><span>申请时间</span></td>
            <td class="td_body"><el-input  v-model="this.user_info.user_create"></el-input></td>
            <td></td>
            <td></td>
          </tr>
        </table>
      </div>
      <div class="user_img">
        <h2>照片</h2>
            <img class="show_img" :src="this.user_info.user_img"/>
            <img class="show_img" v-for="item in this.user_info.user_id_img" :key="item" :src="item"/>
      </div>
      <div class="check_back">
        <h2>审核</h2>
        <check_info :info="this.user_check" ></check_info>
      </div>
    </div>
  </div>
</template>

<script>
import check_info from '../common/check_info'

export default {
  name: 'add_user_info',
  data () {
    return {
      user_info:'',
      user_check:[],
    }
  },
  props:[
    'add_user_id'
  ],
  components:{
    check_info
  },
  methods:{

  },
  mounted(){

    this.$http.get('http://127.0.0.1:8000/user/get_add_user_info/',{params:{add_user_id:this.add_user_id}}).then(response => {
      this.user_info = response.data[0]
    }, response => {  // 错误的返回
        console.log(response) 
    })

    this.$http.get('http://127.0.0.1:8000/user/get_add_user_check/',{params:{add_user_id:this.add_user_id}}).then(response => {
      this.user_check = response.data
    }, response => {  // 错误的返回
        console.log(response) 
    })

  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  el-input{
    color: black;
  }
  .add_user_info{
    padding: 10px;
    width: 100%;
  }
  .check_back{
    margin-top: 50px;
  }

  .add_user_info_head{
    height: 50px;
    text-indent: 30px;
    font-size: 30px;
    border-bottom: 1px solid #e6e6e6
  }

  .add_user_info_body{
    padding-top:10px; 
    padding-left:30px; 
  }
  .user_info_left{
    float: left;
    width: 30%;
  }
  .user_info_right{
    float: left;
    width: 60%;
  }

  table span{
    font-size: 14px;
  }
  .td_title{
    width: 200px;
    padding: 5px;
  }
  .td_body{
    width: 250px;
    padding: 5px;
  }

  .show_img{
    margin-left: 5px;
    width: 200px;
    height: 250px;
  }
  .user_img{
    margin-top: 50px;
  }

  h2{
    margin-bottom: 20px;
  }
  .img_div{
    width: 30px;
  }
</style>
