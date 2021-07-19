<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>
    </div>
    <div class="column is-12 box">
      <table class="table is-fullwidth" v-if="cartTotalLength">
        <thead>
          <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in cart.items" v-bind:key="item.product.id">
            <td>{{ item.product.name }}</td>
            <td>{{ item.product.price }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ getItemTotal(item).toFixed(2) }}</td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td colspan="2">Total</td>
            <td>{{ cartTotalLength }}</td>
            <td>{{ cartTotalPrice.toFixed(2) }}</td>
          </tr>
        </tfoot>
      </table>
      <p v-else>You Don't have any product in your cart..</p>
    </div>
    <div class="column is-12">
      <h2 class="subtitle">Shopping Details</h2>
      <p>* All Field are required</p>
      <div class="columns is-multiline">
        <div class="column is-6">
          <div class="field">
            <label for=" ">First Name *</label>
            <div class="control">
              <input type="text" class="input" v-model="first_name" />
            </div>
          </div>
          <div class="field">
            <label for=" ">Last Name *</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="last_name"
                autocomplete
              />
            </div>
          </div>
          <div class="field">
            <label for=" ">Email *</label>
            <div class="control">
              <input type="text" class="input" v-model="email" autocomplete />
            </div>
          </div>
          <div class="field">
            <label for=" ">Phone</label>
            <div class="control">
              <input type="text" class="input" v-model="phone" autocomplete />
            </div>
          </div>
        </div>
        <div class="column is-6">
          <div class="field">
            <label for=" ">Address *</label>
            <div class="control">
              <input type="text" class="input" v-model="address" autocomplete />
            </div>
          </div>
          <div class="field">
            <label for=" ">Zipcode *</label>
            <div class="control">
              <input type="text" class="input" v-model="zipcode" autocomplete />
            </div>
          </div>
          <div class="field">
            <label for=" ">Place *</label>
            <div class="control">
              <input type="text" class="input" v-model="place" autocomplete />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Axios } from "../axios.js";
export default {
  name: "Checkout",
  data() {
    return {
      cart: {
        items: [],
      },
      stripe: {},
      card: {},
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      zipcode: "",
      place: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Checkout | E-Commerce";
    this.cart = this.$store.state.cart;
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },

    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>
