<template>
  <div class="login">
    <el-input  class="input_height" v-model="username" placeholder="请输入账号"></el-input>
    <el-input  class="input_height" type="password" v-model="userpasswd" placeholder="请输入密码"></el-input>
    <el-button type="primary" @click="login">登录</el-button>
    <h1 class="warn">{{ warn }}</h1>
  </div>
</template>

<script>

export default {
  name: 'login',
  data () {
    return {
      username:'',   // 用户名
      userpasswd:'', // 密码
      warn:'',       // 错误信息
    }
  },
  methods:{
    login(){         // 点击登录 post 请求
      var params = new URLSearchParams();
      params.append('username',this.username)
      params.append('userpasswd',this.userpasswd)
      console.log(this.username,this.userpasswd)
      this.$http.post('http://127.0.0.1:8000/login/',params).then(response => {
          if(response.data == 'ok'){
            this.$store.commit('set_login',this.username)
            this.$router.push('/index')                    // 跳转到  index
          }else{
            this.warn='账号或密码错误'                      // 否则 密码错误
          }
        }, response => {
          console.log(response);
      })
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .login{
    width:500px;
    margin: 0 auto;
    margin-top: 50px;
  }
  .warn{
    display: block;
    margin-top: 10px;
    color: #FF4949;
    font-size: 15px;
  }
  .input_height{
    height: 50px;
    width: 490px;
  }
  .head{
    height: 50px;
    color: #ffffff;
    padding-left: 60px;
    text-align: left;
    background-color: #20A0FF;
    font-size: 30px;
    line-height: 50px;
  }
  
  span{
    display: block;
    height: 50px;
    line-height: 50px;
    font-size: 25px;
  }
</style>
