<template>
    <div class="main-page">
      <h1>Welcome to the Main Page</h1>
      <p>This is a placeholder for the main content of your app.</p>
      <button @click="handleClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "MainPage",
    methods: {
      handleClick() {
        alert("Button clicked!");
      },
    },
  };
  </script>
  
  <style>
  .main-page {
    text-align: center;
    margin-top: 50px;
    font-family: Arial, sans-serif;
  }
  
  .main-page h1 {
    color: #42b983;
  }
  
  .main-page p {
    font-size: 18px;
    color: #333;
  }
  
  .main-page button {
    background-color: #42b983;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .main-page button:hover {
    background-color: #35495e;
  }
  </style>
  