<template>
  <div id="app">
    <head_title :project="this.project"></head_title>
    <head_bottom v-if="is_login"></head_bottom>
    <div class='side' v-if="is_login">
      <side_menu></side_menu>
    </div>
    <div :class='is_body'>
      <router-view/> 
    </div>
  </div>
</template>

<script>
import head_title from './components/common/head_title'
import side_menu from './components/common/side_menu'
import head_bottom from './components/common/head_bottom'

export default {
  name: 'App',
  computed:{
    is_login(){
      return this.$store.getters.is_login
    },
    project(){
      return this.$store.getters.get_project
    },
    is_body(){
      if(this.$store.getters.is_login){
        return 'ok_login'
      }else{
        return 'not_login'
      }
    }
  },
  components:{
    head_title,
    side_menu,
    head_bottom
  },
  mounted(){
    this.$store.commit('set_project')
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
.side{
  float:left;
}
.not_login{
  width:1000px;
  margin: 0 auto;
}
.ok_login{
  float:left;
  width:80%;
  margin: 0 auto;
}

</style>
