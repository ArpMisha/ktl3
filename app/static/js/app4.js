const { createApp } = Vue 

const TaskApp = {
  data(){
    return {
      tasks: {},
      user: {
        'email': '',
        'password': ''
        }
    }
  },
  async created(){
    await this.getTasks()
  },
  methods: {
    async getTasks(){
      const response = await fetch(window.location, {
        method: 'get',
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        } 
      })
      this.tasks = await response.json()
    },
    async createTask(){
      await this.getTasks()
      const response = await fetch(window.location + '_create', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(this.user)
      })
      await this.getTasks()
    },
    async deleteTask(){
      const response = await fetch(window.location + '_delete', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(this.tasks)
      })
      this.tasks = await response.json()
    }
    },
    delimiters: ['{', '}']
  }
  

createApp(TaskApp).mount('#app4')