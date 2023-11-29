<template>
  <div class="container fluid">
    <div
      class="card shadow-sm p-3 mb-5 bg-body-tertiary rounded"
      style="background: white !important"
    >
      <h4 class="hstack gap-3" style="padding: 10px">
        Welcome John
        <i class="bi bi-filetype-pdf p-2 ms-auto" style="font-size: 1em"></i>
      </h4>
      <div style="display: flex; justify-content: center">
        <div
          class="card shadow-sm p-3 mb-5 bg-body-tertiary rounded text-center border-0"
          style="background: #0dcaf0 !important; width: 270px; color: white"
        >
          My balance<br />
          <b style="font-size: 26px">{{ balance }} €</b>
        </div>
      </div>
    </div>
    <div
      class="card shadow-sm p-3 mb-5 bg-body-tertiary rounded"
      style="background: white !important"
    >
      <h4 style="padding: 10px" class="hstack gap-3">
        My transactions
        <button type="button" class="btn btn-outline-info p-2 ms-auto btn-sm" data-bs-toggle="modal" data-bs-target="#transacModal">
          <i class="bi bi-send-plus-fill"></i>&nbsp;&nbsp;New Transaction
        </button>
      </h4>
      <input
        v-model="search"
        class="form-control mb-2"
        type="text"
        placeholder="Search"
      />
      <table class="table table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Detail</th>
            <th>Description</th>
            <th>Status</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in filteredItems" :key="item.id">
            <td>
              <i
                class="bi bi-person-circle"
                style="font-size: 1.5em; color: #a3a3a3"
              ></i>
            </td>
            <td>
              {{ item.to_client }}<br /><small>{{ item.date }}</small>
            </td>
            <td>Transfer money</td>
            <td>
              <button
                :class="item.status=='pending' ? 'btn btn-secondary' :item.status=='accepted' ?'btn btn-success':'btn btn-danger'"
              >
                {{ item.status }}
              </button>
            </td>
            <td>{{ item.amount }} €</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Button trigger modal -->
    <div class="modal" id="transacModal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">
            Create a new transaction
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div
            class="container-fluid p-2 d-flex justify-content-center bg-light"
          >
            <div class="card" style="width: 32rem">
              <div class="card-body">
                <div class="card-text">
                <div class="mb-3">
                  <label for="firstNameClient" class="form-label"
                      >Select recipient</label
                    >
                  <select
                    class="form-select"
                    aria-label="Default select example"
                    v-model="transactionData.to_client"
                    @input="updateTransactionData"
                    >
                    <option selected>Select recipient</option>
                    <option value="f36879f5-82b0-44f4-9a7a-0d6e15e13d79">Lara Gold</option>
                    <option value="2">Lola</option>
                    <option value="3">Mark</option>
                  </select>
                </div>
                  <div class="mb-3">
                    <label for="firstNameClient" class="form-label"
                      >Amount</label
                    >
                    <input
                      type="text"
                      class="form-control"
                      id="firstNameClient"
                      placeholder="Amount €"
                      v-model="transactionData.amount"
                      @input="updateTransactionData"
                    />
                  </div>
                  <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label"
                      >Description</label
                    >
                    <textarea
                      class="form-control"
                      id="exampleFormControlTextarea1"
                      rows="3"
                      v-model="transactionData.description"
                      @input="updateTransactionData"
                    ></textarea>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button
            type="button"
            class="btn btn-primary"
            @click="createTransaction"
          >
            Create
          </button>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import { APIS_URL } from "@/apis";
import {storeNewClient, updateClient} from "@/contracts";
import md5 from 'crypto-js/md5';

export default {

  data() {
    return {
      showModal:false,
      transactionData: {
        to_client: "",
        amount: "",
      },
      data: [
        {
          id: 1,
          description: "Send money to jack",
          recipient: "Jack Lor",
          date: "2023-11-20",
          status: 1,
          amount: "8000",
        },
        {
          id: 2,
          description: "Send money to Lola",
          recipient: "Lola mp",
          date: "2023-11-20",
          status: 0,
          amount: "8000",
        },
      ],
      search: "",
      balance: 12.4567,
      transactions_list:[],
      client_id:'',
      client_id:{}
    };
  },
  computed: {
    filteredItems() {
      return this.transactions_list.filter((item) =>
        item.date.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  mounted() {
    let client_id=localStorage.getItem('client_id')
      if(client_id){
        this.client_id=client_id
        this.client_obj=JSON.parse(localStorage.getItem('client_obj'))
        console.log('client obj',this.client_obj)
      }else{
        this.$router.push('/login')
      }
      this.getTransactionsByClient(client_id)
  },
  methods:{
    updateTransactionData() {
      this.$emit("updateTransactionData", this.transactionData);
    },
    async createTransaction() {
      console.log("data: " + JSON.stringify(this.transactionData));
      axios
        .post(APIS_URL + "/transactions/"+this.client_id, this.transactionData, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then(async(response) => {
          console.log("login res", response.data);
          const hashProfile = md5(this.client_id + this.client_obj['firstName']+this.client_obj['lastName'])
          const time = new Date().toLocaleString()
          this.getTransactionsByClient(this.client_id)
          // await storeNewClient(this.client_id,hashProfile,this.client_obj['company'],time)
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getTransactionsByClient(client_id){
      axios
        .get(APIS_URL + "/transactions/"+client_id, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.transactions_list=response.data
          console.log("get all transa res", response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  }
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
