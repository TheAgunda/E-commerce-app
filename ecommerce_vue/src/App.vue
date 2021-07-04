<template>
  <div id="wrapper">
    <div class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>E-Commerce</strong>
        </router-link>
        <button
          class="navbar-burger"
          aria-labelledby="menu"
          aria-expanded="false"
          data-targer="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </button>
      </div>
      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/summer" class="navbar-item">Winter</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light">
                Login
              </router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa fa-shopping-cart"></i></span>
                <span>Cart</span> 
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <section class="section">
      <router-view />
    </section>
    <footer class="footer">
      <p class="has-text-right">© E-Commerce.</p>
    </footer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
};
</script>


<style lang="scss">
@import "../node_modules/bulma";
</style>
