<template>
  <div class="page-sign-up">
    <div class="column is-4 is-offset-4">
      <h2 class="title">Login</h2>
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
        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-dark">Login</button>
          </div>
        </div>
        <hr />
        Or
        <router-link to="/sign-up">Click here</router-link> to SignUp!
      </form>
    </div>
  </div>
</template>
<script>
import { Axios } from "../axios.js";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Login In | E-commerce";
  },
  methods: {
    async submitForm() {
      Axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      await Axios.post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          Axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          const toPath = this.$route.query.to || "cart";
          console.log(toPath);
          this.$router.push(toPath);
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}:${error.response.data[property]}`);
            }
            console.log(JSON.stringify(error.response.data));
          } else {
            this.errors.push("sdaljf;kas");
            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>