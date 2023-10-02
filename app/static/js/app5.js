const { createApp } = Vue 

const TaskApp = {
  data(){
    return {
      tasks: {},
      user: {
        'name': '',
        'surname': '',
        'age': ''
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
      const response = await fetch(window.location + '_upload', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(this.user)
      })
      await this.getTasks()
    }
    },
    delimiters: ['{', '}']
  }
  

createApp(TaskApp).mount('#app5')