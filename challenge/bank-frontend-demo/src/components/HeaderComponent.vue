<script>
export default {
  name: "HeaderComponent",
  props: {
    from: String,
  },
};
</script>

<template>
  <div class="container-fluid text-center">
    <header class="header" style="padding-left: 40px">
      <div class="header_toggle"><i class="bi bi-bank"></i> LIST Bank</div>
      <!-- <div class="header_img">
            <i class="bi bi-person-circle" style="font-size: 1.5em;"></i>
        </div> -->
      <div class="col-2 d-flex align-items-center justify-content-center hstack gap-3">
        <button type="button" class="btn btn-info" >
          <router-link style="text-decoration: none;color: white;" to="/onboarding" class="p-1 mx-1">Sign up</router-link>
        </button>
        
        <button type="button" class="btn btn-outline-info" >
        <router-link to="/login" class="p-1 mx-1" style="text-decoration: none;color: inherit;">Login</router-link>
      </button>
      </div>
    </header>
    <!-- <div class="row background p-2">
      <div class="col-2">
        <img src="../assets/bank-logo.svg" class="img-fluid" alt="logo" width="70">
      </div>
      <div class="col d-flex align-items-center justify-content-center">
        My BANK
      </div>
      <div class="col-2 d-flex align-items-center justify-content-center" v-if="from==='home'">
        <router-link to="/onboarding" class="p-1 mx-1">Sign up</router-link>
        <router-link to="/login" class="p-1 mx-1">Sign in</router-link>
      </div>
      <div class="col-2 d-flex align-items-center justify-content-center" v-if="from==='onboarding'">
        <router-link to="/">Back</router-link>
      </div>

    </div> -->
  </div>
</template>

<style scoped>
.background {
  background-color: #dad3e0;
}
</style>
