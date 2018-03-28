import Vue from 'vue'
import Router from 'vue-router'
import {store} from '../store/store'
import axios from 'axios'


import index from '../components/index'
import login from '../components/login'
import add_user from '../components/user/add_user'
import user_list from '../components/user/user_list'
import add_user_info from '../components/user/add_user_info'
import user_info from '../components/user/user_info'
import add_user_check from '../components/user/add_user_check'
import get_gps from '../components/gps/get_gps'


Vue.use(Router)

export const routes = [
  { path: '/index', component: index,meta:{is_login:true}},  //  首页
  { path: '/login', component: login,meta:{is_login:false}},  //  login
  { path: '/user/add_user', component: add_user,meta:{is_login:true}},// 添加用户美滋滋
  { path: '/user/user_list', component: user_list,meta:{is_login:true}},
  { path: '/user/add_user_check', component: add_user_check ,meta:{is_login:true}},
  { path: '/user/add_user_info/:add_user_id', component: add_user_info ,meta:{is_login:true},props: true},
  { path: '/user/user_info/:user_id', component: user_info ,meta:{is_login:true},props: true},

  { path: '/attence/attence/', component: get_gps ,meta:{is_login:true},props: true},


  { path: '/', component: index,meta:{is_login:true}},
]

export const router = new Router({
  mode: 'history',
  routes
})

function is_login(path){

  store.commit('get_login')

  if(path == '/login'){
    if(store.getters.is_login){
      return false
    }else{
      return true
    }
  }else if(store.getters.is_login){
    return true
  }else{
    return false
  }
    
}

router.beforeEach((to, from, next) => {
  if(is_login(to.path)){
    store.commit('set_sideitem')
    next()
  }else{
    next('login')
  }
})
