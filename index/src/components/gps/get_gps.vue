<template>
    <div class="get_gps">
        <span>当前IP:{{ ip }}</span>
        <span>{{ gpsinfo }}</span>
        <el-button @click="GetGps" type="button" size="small">获取当前定位</el-button>
    </div>
</template>

<script>



export default {
  name: 'get_gps',
  data () {
    return {
        gpsinfo:'',
        ip:''
    }
  },
  methods:{
    GetGps(){

    }
  },
  mounted(){
    this.$http.get('http://freegeoip.net/json/').then(response => {
        this.ip = response.data.ip
    }, response => {  // 错误的返回
        console.log(response) 
    })

    this.$http.get('http://api.map.baidu.com/location/ip/',{ip:this.ip,ak:"PF7EyA8EhVU4lYMHCpD2fkcRBNS12OeQ"}).then(response => {
        console.log(response.data)
    }, response => {  // 错误的返回
        console.log(response) 
    })


    	
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
