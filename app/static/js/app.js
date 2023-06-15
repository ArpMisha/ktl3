const { createApp } = Vue 

const TaskApp = {
  data(){
    return {
      search: {
      'kr_name': ''
      },
      task: {
      'kr_name': '',
      'name': '',
      'kategor': '',
      'tip': ''
      },
      tasks: []
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
 
    async searchTask(){
      await this.getTasks()

      const response = await fetch(window.location + '_search', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(this.search)
      })
      await this.getTasks()
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')