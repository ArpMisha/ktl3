const { createApp } = Vue 

const TaskApp = {
  data() {
    return {
      photo: null
    };
  },
  methods: {
    async uploadPhoto() {
      if (!this.photo) {
        alert("Пожалуйста, выберите изображение");
        return;
      }

      const formData = new FormData();
      formData.append("photo", this.photo);

      try {
        const response = await fetch("/upload-photo", {
          method: "POST",
          body: formData
        });

        if (!response.ok) {
          throw new Error("Ошибка при загрузке фотографии");
        }

        // Опционально: обработка успешной загрузки
        alert("Фотография успешно загружена");

        // Очистить поле выбранного изображения после успешной загрузки
        this.photo = null;
      } catch (error) {
        console.error("Ошибка при загрузке фотографии:", error);
        alert("Ошибка при загрузке фотографии. Пожалуйста, попробуйте еще раз");
      }
    },
    handleFileInputChange(event) {
      this.photo = event.target.files[0];
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app6')