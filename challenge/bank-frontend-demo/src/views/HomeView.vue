<script>
import {Web3} from "web3";
import {ethers} from "ethers";
import md5 from 'crypto-js/md5';
import Base64 from 'crypto-js/enc-base64';
import {storeNewClient, updateClient} from "@/contracts";
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  name: 'HomeView',
  components: {HeaderComponent},
  data() {
    return {
      connected: false,
      contractResult: null
    }
  },
  mounted() {
    this.connect()
  },
  methods: {
    async storeNewClient(refClient, seller) {
      const time = new Date().toLocaleString()
      const hashProfile = md5(refClient + time)
      console.log('hashProfile: ', Base64.stringify(hashProfile))
      this.contractResult = await storeNewClient(refClient, Base64.stringify(hashProfile), seller, time)
    },
    async updateClient(refClient) {
      const time = new Date().toLocaleString()
      const hashProfile = md5(refClient + time)
      this.contractResult = await updateClient(refClient, Base64.stringify(hashProfile), time)
    },
    clearValue() {
      this.contractResult = null
    },
    connect() {
      // this connects to the wallet>
      if (window.ethereum) { // first we check if metamask is installed
        window.ethereum.request({method: 'eth_requestAccounts'})
            .then(() => {
              this.connected = true; // If users successfully connected their wallet
            });
      }
    },
  }
 }
</script>

<template>
  <main>
    <header-component from="home"/>
    <div>
      <p></p>
      <button v-if="connected" @click.prevent="storeNewClient('refClient2',  true)" class="btn btn-primary">Store new client</button>
      {{ contractResult }}
      <p></p>
      <button v-if="connected" @click.prevent="updateClient('refClient2')" class="btn btn-danger">Update client</button>
      {{ contractResult }}
      <p></p>
      <button v-if="connected" @click.prevent="clearValue">Clear value</button>
    </div>
  </main>
</template>
