<template>
  <div class="head_title">
      <span>{{ this.date }}{{ this.time }}</span>
  </div>
</template>

<script>

var myDate = new Date();

 export default {
  name: 'head_bottom',
  data () {
    return {
        time: '',
        date: ''
    }
  },

}


//11111111111111111111111111
/*
function zeroPadding(num, digit) {
    var zero = '';
    for(var i = 0; i < digit; i++) {
        zero += '0';
    }
    return (zero + num).slice(-digit);
}

function updateTime(ok) {
    console.log('1')
    var cd = new Date();
    ok.time = zeroPadding(cd.getHours(), 2) + ':' + zeroPadding(cd.getMinutes(), 2) + ':' + zeroPadding(cd.getSeconds(), 2);
    ok.date = zeroPadding(cd.getFullYear(), 4) + '-' + zeroPadding(cd.getMonth()+1, 2) + '-' + zeroPadding(cd.getDate(), 2);
};
    var timerID = setInterval(updateTime(this), 1000);


    //updateTime();

//11111111111111111111111111*/






</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.head_title{
    height:25px;
    font-size: 15px;
    background-color: #DCDFE6;
    line-height: 25px;
    padding-left: 60px;
}
</style>
