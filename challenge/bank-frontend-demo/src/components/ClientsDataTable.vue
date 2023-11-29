<template>
    <div class="card shadow-sm p-3 mb-5 bg-body-tertiary rounded" style="background: white !important;">
        <h4 style="padding:10px">
        <small class="text-body-secondary" >Clients Table</small>
        </h4>
      <input
        v-model="search"
        class="form-control mb-2"
        type="text"
        placeholder="Search"
      />
      <table class="table table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in filteredUsers" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props:{
        data:Array,
    },
    data() {
      return {

        search: '',
      };
    },
    computed: {
      filteredUsers() {
        return this.data.filter((user) =>
          user.name.toLowerCase().includes(this.search.toLowerCase())
        );
      },
    },
    mounted(){
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  