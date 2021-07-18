<template>
  <div class="page-sign-up">
    <div class="column is-4 is-offset-4">
      <h2 class="title">SignUp</h2>
      <form @submit.prevent="submitForm">
        <div class="field">
          <label for=" ">Username</label>
          <div class="control">
            <input type="text" class="input" v-model="username" />
          </div>
        </div>
        <div class="field">
          <label for=" ">Password</label>
          <div class="control">
            <input
              type="password"
              class="input"
              v-model="password"
              autocomplete
            />
          </div>
        </div>
        <div class="field">
          <label for="">Confirm password</label>
          <div class="control">
            <input
              type="password"
              class="input"
              v-model="password2"
              autocomplete
            />
          </div>
        </div>
        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-dark">Sign Up</button>
          </div>
        </div>
        <hr />
        Or
        <router-link to="/log-in">Click here</router-link> to login in!
      </form>
    </div>
  </div>
</template>
<script>
import { Axios } from "@/axios.js";

export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];
      if (this.username === "") {
        this.errors.push("The Username is missing.");
      }
      if (this.password === "") {
        this.errors.push("The Password is missing.");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match.");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };
        Axios.post("/api/v1/users/", formData)
          .then((response) => {
            this.$router.push("/log-in");
            toast({
              message: "Account Created successfully",
              type: "is-danger",
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: "bottom-right",
            });
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}:${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            }
            // else if (error.message) {
            //   this.errors.push("Something went wrong, please try again");
            //   console.log(JSON.stringify(error));
            // }
          });
      }
    },
  },
};
</script>