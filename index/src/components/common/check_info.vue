<template>
  <div class="check_info">

    <div class="">
        <el-table :data="this.info" style="width: 100%" max-height="1500">
          <el-table-column  prop="check_info" label="顺序"></el-table-column>
          <el-table-column  prop="check_user" label="审核用户"></el-table-column>
          <el-table-column  prop="check_status" label="审核状态"></el-table-column>
          <el-table-column  prop="check_note" label="审核状态"></el-table-column>
        </el-table>
    </div>
  </div>
</template>

<script>

 export default {
  name: 'check_info',
  data () {
    return {
    }

  },
  props:['info']

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
._check_info{
  width: 100%;
  font-size: 14px;
}
.check_item{
    float: left;
    height: 80px;
    width: 80px;
    overflow: hidden;
    color:#fff;
    text-align: center;
    background: #409EFF;
    
}


.arrow{
    float: left;
    height: 75px;
    width: 25px;
    margin-left: 5px;
    overflow: hidden;
    text-align: center; 
    line-height: 75px; 
}
</style>
