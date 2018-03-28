<template>
  <div class="add_user_check">
    <div class="user_list_head">
      <span class="page_title">人员入职审核列表</span>  
    </div>
    <div class="user_list_body">
        <el-table :data="check_user_list" style="width: 100%" max-height="1500">
          <el-table-column prop="user_name" label="姓名"></el-table-column>
          <el-table-column prop="user_sex" label="性别"></el-table-column>
          <el-table-column  prop="user_phone" label="用户电话"></el-table-column>
          <el-table-column  prop="user_id_number" label="身份证"></el-table-column>
          <el-table-column  prop="user_create" label="入职日期"></el-table-column>
          <el-table-column  label="操作">
            <template slot-scope="scope">
              <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
            </template>
          </el-table-column>
        </el-table>
    </div>
  </div>
</template>

<script>
import { push_list_data } from '../../common'


export default {
  name: 'add_user_check',
  data () {
    return {
        check_user_list:[]
    }
  },
  methods:{
      handleClick(item){
        this.$router.push('/user/add_user_info/'+item.user_id)
        console.log(item.user_id)
    }
  },
  mounted(){
    this.$http.get('http://127.0.0.1:8000/user/check_user/').then(response => {
      this.check_user_list = response.data
    }, response => {  // 错误的返回
        console.log(response) 
    })
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .add_user_check{
    padding: 10px;
    width: 100%;
  }

  .user_list_head{
    height: 50px;
    text-indent: 30px;
    font-size: 30px;
    border-bottom: 1px solid #e6e6e6
  }

  .user_list_body{

  }
</style>
