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
      <ProductBox
        v-for="product in latestProductList"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import { Axios } from "../axios.js";
import ProductBox from "@/components/ProductBox";
export default {
  name: "Home",
  components: {
    ProductBox,
  },
  data() {
    return {
      latestProductList: [],
    };
  },
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      await Axios.get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProductList = response.data;
          document.title = "Home | E-Commerce";
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

