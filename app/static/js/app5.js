document.addEventListener('DOMContentLoaded', function () {
  // Initialize data
  const search = {
    kr_name: ''
  };
  const task = {
    kr_name: '',
    name: '',
    kategor: '',
    tip: ''
  };
  let tasks = [];

  // Helper function to update the task table
  function updateTaskTable() {
    const tableBody = document.querySelector('tbody');
    tableBody.innerHTML = '';

    tasks.forEach((task, index) => {
      const row = tableBody.insertRow();
      const cell1 = row.insertCell(0);
      const cell2 = row.insertCell(1);
      const cell3 = row.insertCell(2);
      const cell4 = row.insertCell(3);

      cell1.innerHTML = task.kr_name;
      cell2.innerHTML = task.name;
      cell3.innerHTML = task.kategor;
      cell4.innerHTML = task.tip;
    });
  }

  // Event handler for the search form
  const searchForm = document.querySelector('.card-search form');
  searchForm.addEventListener('submit', async function (event) {
    event.preventDefault();

    const response = await fetch(window.location + '_search', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      body: JSON.stringify(search)
    });

    tasks = await response.json();
    updateTaskTable();
  });

  // Event handler for the create form
  const createForm = document.querySelector('.card-search:last-child form');
  createForm.addEventListener('submit', async function (event) {
    event.preventDefault();

    const response = await fetch(window.location + '_create', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      body: JSON.stringify(task)
    });

    // You can handle the response as needed, e.g., display a success message.
    // Optionally, you can update the tasks array and table if necessary.
  });
});
