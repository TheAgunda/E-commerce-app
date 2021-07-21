<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="title">Thank You</h2>
        <p>Your order will be proccessed within 48 hours.</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Success",
  mounted() {
    document.title = "Success | E-Commerce";
  },
};
</script>
