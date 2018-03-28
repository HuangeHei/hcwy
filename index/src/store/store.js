import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


export const store =  new Vuex.Store({
    state:{
        login:false,
        user_name: '',
        Project:{
            ProjectName : "",
            ProjectColor : "",
            ProjectIcon : "",
        },
        SideItem:null
    },
    getters:{
        is_login:(state)=>{
            return state.login
        },
        get_user_name:(state)=>{
            return state.user_name
        },
        get_project:(state)=>{
            return state.Project
        },
        get_sideitem:(state)=>{
            return state.SideItem
        }
    },
    mutations:{
        get_login:(state)=>{
            if(window.sessionStorage.getItem('is_login')){
                state.login = true
                state.user_name = window.sessionStorage.getItem('user_name');
            }
        },
        del_login:(state,user_name)=>{  // 清空 用户名 并 修改登录状态为假
            window.sessionStorage.removeItem('is_login');
            window.sessionStorage.removeItem('user_name');
            state.login = false
            state.user_name = ''
        },
        set_login:(state,user_name)=>{
            window.sessionStorage.setItem('is_login',true);
            window.sessionStorage.setItem('user_name',user_name);
            state.is_login = true
            state.user_name = user_name
            console.log('调用了set_login',state.user_name,state.is_login )
        },
        set_project:(state)=>{ //获取项目配置，不需要验登录，严禁使用隐晦内容
            
            axios.get('http://127.0.0.1:8000/getprojectsetting/').then(response => {

                var project = response.data[0].fields
                state.Project.ProjectColor = project.ProjectColor
                state.Project.ProjectName = project.ProjectName
                state.Project.ProjectIcon = project.ProjectIcon
            }, response => {  // 错误的返回
                console.log(response) 
            })
           
        },
        set_sideitem:(state)=>{ // 从服务器获取sideitem
            axios.get('http://127.0.0.1:8000/index/').then(response => {
                state.SideItem = response.data
            }, response => {  // 错误的返回
                console.log(response) 
            })
        }
    }
})
