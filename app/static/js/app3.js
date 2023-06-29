const { createApp } = Vue 

const TaskApp = {
  data(){
    return {
      search: {
      'name': ''
      },
      tasks: {}
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
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app3')