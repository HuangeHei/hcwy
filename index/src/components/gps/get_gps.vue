<template>
    <div class="get_gps">
        <span>你好:{{ user_name }}</span>
        <span>当前IP:{{ ip }}</span>
        <span>{{ gpsinfo }}</span>
        <el-button @click="GetGps" type="button" size="small">定位打卡</el-button>
        {{local_name}}
    </div>
</template>
<script>
export default {
  name: 'get_gps',
  data () {
    return {
        gpsinfo:'',
        ip:'',
        ak:'PF7EyA8EhVU4lYMHCpD2fkcRBNS12OeQ',
        coor:'bd09ll',
        location:"",
        pois:1,
        output:"json",
        local_name:'',
    }
  },
  computed:{
    user(){
      return this.$store.getters.get_user_name   // 获取用户名
    }
  },
  methods:{
    PostAttence(){
        var params = new URLSearchParams();
        params.append('local',this.local_name)
        params.append('ip',this.ip)
        params.append('user_name',this.user)
        params.append('grid',this.location)
        

        this.$http.post('http://127.0.0.1:8000/postattence/',params).then(response => {
                console.log(response.data);
            }, response => {
                console.log(response);
            }
        )
    },
    GetGps(){

        this.$jsonp("http://api.map.baidu.com/location/ip", {ip:this.ip,ak:this.ak,coor:this.coor}).then(res => {
            this.location = res.content.point.y+","+res.content.point.x
            this.$jsonp("http://api.map.baidu.com/geocoder/v2/",{location:this.location,ak:this.ak,output:this.output,pois:this.pois}).then(res => {
                console.log(res)
                this.local_name = res.result.formatted_address +  res.result.sematic_description
                this.PostAttence()
            }).catch(err =>{
                console.log("1",err)
            })
        }).catch(err => {
        　　console.log(err)
        })      
    },

  
  },
  computed:{
    user_name(){
      return this.$store.getters.get_user_name   // 获取用户名
    }
  },
  mounted(){

    this.$http.get('http://freegeoip.net/json/').then(response => {
        this.ip = response.data.ip
    }, response => {  // 错误的返回
        console.log(response) 
    })	
  },

}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
