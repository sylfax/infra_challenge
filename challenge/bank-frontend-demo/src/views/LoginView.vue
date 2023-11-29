<script>
import axios from "axios";
import {APIS_URL} from "@/apis";

export default {
  name: "LoginView",
  data() {
    return {
      userData: {
        username: "",
        password: "",
      },
    };
  },
  mounted(){
      let client_id=localStorage.getItem('client_id')
      if(client_id){
        this.$router.push('/client')
      }else{
        this.$router.push('/login')
      }
  },
  methods: {
    updateUserData() {
      this.$emit("updateUserData", this.userData);
    },
    login() {
      console.log("data: " + JSON.stringify(this.userData));
      axios
        .post(APIS_URL + "/auth/login", this.userData, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log("login res",response.data);
          let re=response.data
          localStorage.setItem('client_id',re['uuid'])
          localStorage.setItem('client_obj',JSON.stringify(re))
          this.$router.push('/client')
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<template>
  <div
    class="container-fluid p-2 d-flex justify-content-center bg-light"
    style="padding-top: 100px !important"
  >
    <div class="card" style="width: 32rem">
      <div class="card-body">
        <h5 class="card-title fw-bolder">Login into your account</h5>
        <div class="card-text">
          <div class="mb-3">
            <label for="firstNameClient" class="form-label">Username</label>
            <input
              type="text"
              class="form-control"
              id="firstNameClient"
              placeholder="Username"
              v-model="userData.username"
              @input="updateUserData"
            />
          </div>
          <div class="mb-3">
            <label for="lastNameClient" class="form-label">Password</label>
            <input
              type="password"
              class="form-control"
              id="lastNameClient"
              placeholder="Password"
              v-model="userData.password"
              @input="updateUserData"
            />
          </div>
          <div class="mb-3 form-check">
            <input
              type="checkbox"
              class="form-check-input"
              id="exampleCheck1"
            />
            <label class="form-check-label" for="exampleCheck1"
              >Check me out</label
            >
          </div>
          <button type="submit" class="btn btn-primary" @click="login">Login</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
