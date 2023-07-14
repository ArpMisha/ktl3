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
  methods: {
    async searchTask(){
      const response = await fetch(window.location + '_search', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(this.search)
      })
      this.tasks = await response.json()
    },
    async createTask(){
      const response = await fetch(window.location + '_create', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(this.task)
      })
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app2')