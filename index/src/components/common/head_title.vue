<template>
  <div class="head_title">
    <div class='_head' :style="this.headStyle" @click="goto_index" >{{ this.project.ProjectName }}
    <out></out>
    </div>
  </div>
</template>

<script>
import out from './out'

export default {
  name: 'head_title',
  methods:{
    goto_index(){
      this.$router.push('/index')
    }
  },
  computed:{
    headStyle(){
      return {"backgroundColor":this.project.ProjectColor}
    },
  },
  components:{
    out
  },
  props:[
    'project',
  ],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
._head{
  height: 50px;
  color: #ffffff;
  padding-left: 60px;
  text-align: left;
  font-size: 30px;
  line-height: 50px;
  cursor: pointer;
}
</style>
