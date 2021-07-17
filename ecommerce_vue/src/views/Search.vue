<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">Search terms :"{{ query }}"</h2>
      </div>
      <ProductBox
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>
<script>
import { Axios } from "../axios.js";
import ProductBox from "@/components/ProductBox.vue";
export default {
  name: "Search",
  components: {
    ProductBox,
  },
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search | E-commerce";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    if (params.get("query")) {
      this.query = params.get("query");
      this.performSeacrh();
    }
  },
  methods: {
    async performSeacrh() {
      this.$store.commit("setIsLoading", true);
      await Axios.post('/api/v1/products/search/', {'query': this.query })
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
