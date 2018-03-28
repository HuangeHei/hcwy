<template>
  <div class="side_menu">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo side_height"
      @open="handleOpen"
      @close="handleClose"
      >
<!-- 人员管理页面开始 -->
      <!-- 人员管理页面开始 -->
      <side_item :index="item.Index" :name="item.Name" :item="item.Child" v-for="item in side_list" :key="item.Index"></side_item>
      <!-- 人员管理页面结束 -->

    </el-menu>
  </div>
</template>

<script>

import side_item from '../side/side_item'
export default {
  name: 'side_menu',
  data () {
    return {
    }
  },
  computed:{
    side_list(){
      return this.$store.getters.get_sideitem
    }
  },
  components:{
    side_item 
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.side_menu{

  height: 1000px;
  width:230px;

}
.side_height{
  height: 1000px;
  width:230px;
}
</style>
