// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import App from './App'
import {router} from './router/index'
import {store} from './store/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)

//配置axios

axios.defaults.withCredentials = true
Vue.prototype.$http = axios

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router:router,
  store:store,
  components: { App },
  template: '<App/>'
})

// js 数组删除指定元素

Array.prototype.remove=function(obj){
  for(var i =0;i <this.length;i++){
    var temp = this[i];
    if(!isNaN(obj)){
      temp=i;
    }
    if(temp == obj){
      for(var j = i;j <this.length;j++){
        this[j]=this[j+1];
      }
      this.length = this.length-1;
    }
  }
}