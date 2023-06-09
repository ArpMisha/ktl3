const { createApp } = Vue 

const TaskApp = {
  data(){
    return {
      task: '123'
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')