<template>
  <div class="user_info">
    <div class="user_info_head">
      <span class="page_title">人员信息</span>  
    </div>
    <div class="user_info">
      <div>
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
            <td class="td_title"><span>入职时间</span></td>
            <td class="td_body"><el-input  v-model="this.user_info.user_create"></el-input></td>
            <td class="td_title"><span>所在项目部</span></td>
            <td class="td_body"><el-input  v-model="this.user_info.user_project"></el-input></td>
          </tr>
        </table>
      </div>
      <div class="user_img">
        <h2>照片</h2>
            <img class="show_img" :src="this.user_info.user_img"/>
            <img class="show_img" v-for="item in this.user_info.user_id_img" :src="item" :key="item" />
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'user_info',
  data () {
    return {
      user_info:[],
    }
  },
  props:[
    'user_id'
  ],
  methods:{

  },
  mounted(){

    this.$http.get('http://127.0.0.1:8000/user/get_user_info/',{params:{user_id:this.user_id}}).then(response => {
        console.log(response.data[0])
      this.user_info = response.data[0]
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
  .user_info{
    padding: 10px;
    width: 100%;
  }

  .user_info_head{
    height: 50px;
    text-indent: 30px;
    font-size: 30px;
    border-bottom: 1px solid #e6e6e6
  }

  .user_info_body{
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
