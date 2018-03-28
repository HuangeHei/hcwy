<template>
      <!-- 人员管理页面开始 -->
      <el-submenu :index="this.index">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>{{ this.name }}</span>
        </template>

        <el-menu-item :index="menu.Index" v-for="menu in item" :key="menu.Index" @click="router_push(menu.To)">
          {{ menu.Name }}
        </el-menu-item>
  
      </el-submenu>
      <!-- 人员管理页面结束 -->
</template>

<script>

export default {
  name: 'side_item',
  data () {
    return {
      item_index:[...Array(this.item.length).keys()]
    } 
  },
  props:['index','item','name'],
  computed:{
  
  },
  mounted(){
    console.log(this.item,this.index)
  },
  methods:{
    router_push(to){
      this.$router.push(to)
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
