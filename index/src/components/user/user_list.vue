<template>
  <div class="user_list">
    <div class="user_list_head">
      <span class="page_title">人员列表</span>  
    </div>
    <div class="user_list_body">
        <el-table :data="user_list" style="width: 100%" max-height="1500">
          <el-table-column prop="user_name" label="姓名"></el-table-column>
          <el-table-column prop="user_sex" label="性别"></el-table-column>
          <el-table-column  prop="user_phone" label="用户电话"></el-table-column>
          <el-table-column  prop="user_project" label="所属项目"></el-table-column>
          <el-table-column  prop="user_id_number" label="身份证"></el-table-column>
          <el-table-column  prop="user_create" label="入职日期"></el-table-column>
          <el-table-column  label="操作">
            <template slot-scope="scope">
              <el-button @click="handleClick(scope.row)" type="text" size="small">操作</el-button>
            </template>
          </el-table-column>
        </el-table>
    </div>
  </div>
</template>

<script>

export default {
  name: 'user_list',
  data () {
    return {
        user_list:[]
    }
  },
  methods:{
    handleClick(item){
        this.$router.push('/user/user_info/'+item.user_id)
    }
  },
  mounted(){
    this.$http.get('http://127.0.0.1:8000/user/list/').then(response => {
      this.user_list = response.data
    }, response => {  // 错误的返回
        console.log(response) 
    })
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .user_list{
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
