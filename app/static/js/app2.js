const { createApp } = Vue 

const TaskApp = {
  data(){
    return {
      attack: '<a onmouseover=alert(document.cookie)>click me!</a>'
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

  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app2')