<template>
  <div class="out" v-if="is_login">
    <div class="out">当前用户:{{ user }}<span @click="out">退出当前用户</span></div>
  </div>
</template>

<script>


export default {
  name: 'out',
  data () {
    return {
    }
  },
  computed:{
    is_login(){
      return this.$store.getters.is_login       // 登录信息
    },
    user(){
      return this.$store.getters.get_user_name   // 获取用户名
    }
  },
  methods:{
    out(){  // 点击退出触发
      this.$store.commit('del_login')
      location.reload()    
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped> 
.out{
  min-width: 150px;
  float:right;
  margin-right:50px;
  
}
span{
  width: 150px;
  margin-left:20px; 
}
span:hover{
  cursor:pointer 
}

</style>
