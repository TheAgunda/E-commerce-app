<template>
  <div class="home">
    <section class="hero is-meduum is-dark mb-5">
      <div class="hero-body">
        <p class="title">E-Commerce</p>
        <p class="sub-title">
          Lorem Ipsum is simply dummy text of the printing and typesetting
          industry. Lorem Ipsum has been the industry's standard dummy text ever
          since the 1500s, when an unknown printer took a galley of type and
          scrambled it to make a type specimen book.
        </p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2">Latest Product</h2>
      </div>
      <div
        class="column is-3"
        v-for="product in latestProductList"
        v-bind:key="product.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="product.get_thumbnail" />
          </figure>
          <h3 class="is-size-5">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">₹ {{ product.price }}</p>
          <router-link
            v-bind:to="product.get_absolute_url"
            class="button is-dark mt-4"
          >
            View Details
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {Axios} from "../axios.js";
export default {
  name: "Home",
  components: {},
  data() {
    return {
      latestProductList: [],
    };
  },
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      console.log(Axios.baseURL)
      Axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProductList = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
.image {
  margin-right: -1.25rem;
  margin-left: -1.25rem;
  margin-top: -1.25rem;
}
</style>
