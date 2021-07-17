<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Cart</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLength">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>
            <CartItem
              v-for="item in cart.item"
              v-bind:key="item.product.id"
              v-bind:initialItem="item"
            />
          </tbody>
        </table>
        <p>You Don't have any product in your cart..</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Cart",
};
</script>
