<template>
  <div>
    <div class="container">
      <div class="row" style="margin-bottom: 20px;">
        <div class="col-md-4">
          <div class="card" >
          <div class="card-body">
            <h5 class="card-title hstack gap-3">Transactions<i class="bi bi-cash-stack p-2 ms-auto" style="font-size: 1.5em;color:#a595e3;"></i></h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">1000</h6>
          </div>
        </div>
        </div>
        <div class="col-md-4">
          <div class="card" >
          <div class="card-body">
            <h5 class="card-title hstack gap-3">Clients<i class="bi bi-people p-2 ms-auto" style="font-size: 1.5em;color:#a595e3;"></i></h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">700</h6>
          </div>
        </div>
        </div>
        <div class="col-md-4">
          <div class="card" >
          <div class="card-body">
            <h5 class="card-title hstack gap-3">Market<i class="bi bi-graph-up-arrow p-2 ms-auto" style="font-size: 1.5em;color:#a595e3;"></i></h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">1000</h6>
          </div>
        </div>
        </div>
      </div>
      <div class="card shadow-sm p-3 mb-5 bg-body-tertiary rounded" style="background: white !important;">
        <h4 style="padding:10px">
        <small class="text-body-secondary" >Transactions history</small>
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
            <th>Check AML</th>
            <th>Rule 2</th>
            <th>Rule 7</th>
            <th>Decision</th>
            <th>Alert</th>
            <th>View Alert</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in filteredTrans" :key="item.uuid">
            <td>
              <i
                class="bi bi-person-circle"
                style="font-size: 1.5em; color: #a3a3a3"
              ></i>
            </td>
            <td>
              {{ item.username }}<br /><small>{{ item.date }}</small>
            </td>
            <td>Transfer money</td>
            <td>
              <button
                :class="item.status=='pending' ? 'btn btn-secondary' : item.status=='accepted'?'btn btn-success':'btn btn-danger'"
              >
                {{ item.status }}
              </button>
            </td>
            <td>{{ item.amount }} €</td>
            <td><button class="btn btn-info" @click="checkAML(item.uuid,item.amount)">Check</button></td>
            <td><button v-if="current_line==item.uuid" :class="result.rule2_status==0?'btn btn-success':'btn btn-danger'" >{{ result.rule2_status==0?"Safe":"Danger" }}</button></td>
            <td><button v-if="current_line==item.uuid" :class="result.rule7_status==0?'btn btn-success':'btn btn-danger'" >{{ result.rule7_status==0?"Safe":"Danger" }}</button></td>
         <td><button @click="UpdateStatut(item.uuid,'accepted')">Approve</button> <button @click="UpdateStatut(item.uuid,'rejected')">Block</button></td>
         <td><button class="btn btn-warning" @click="createAlert(item.from_client)">Create</button></td>
         <td><button @click="viewAlert()" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#alertModal">View</button></td>

        </tr>
        </tbody>
      </table>
    </div>
    </div>
    <div class="modal" id="alertModal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">
            View Alert
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
               Comment
               <br>
               Risky customer.
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
          <!-- <button
            type="button"
            class="btn btn-primary"
            @click="createTransaction"
          >
            Create
          </button> -->
        </div>
      </div>
    </div>
  </div> 


  </div>
</template>
<script>
import axios from "axios";
import { APIS_URL } from "@/apis";
import {check_rule2, check_rule7,get_aml_status} from "@/contracts";

export default {
    data() {
      return {
        transactions_list:[],
        data: [
        { id: 1, name: "Transaction Euro", client: "John Doe",date:'2023-11-20',amount:"8000" },
        { id: 2, name: "Transaction Euro", client: "John Doe",date:'2023-11-20',amount:"8000" },

        // Add more users as needed
      ],
        search: '',
        check:'',
        result:{rule2_status:0,rule7_status:0},
        current_line:''
      };
    },
    computed: {
      filteredTrans() {
        return this.transactions_list.filter((item) =>
          item.date.toLowerCase().includes(this.search.toLowerCase())
        );
      },
    },
    mounted(){
this.getAllTransactions()
    },
    methods:{
      createAlert(id_client){
        let data={
          ref_client: id_client,
          type: [2],
          comment: "Alert for client"
        }
        axios
        .post(APIS_URL + "/alerts",data, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log("create alert", response.data);
        })
        .catch((error) => {
          console.error(error);
        });
      },
      UpdateStatut(id,status){
        axios
        .put(APIS_URL + "/transactions/uuid/"+id+"/"+status, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.getAllTransactions()
          console.log("get all transa res", response.data);
        })
        .catch((error) => {
          console.error(error);
        });
      },
      getAllTransactions(){
      axios
        .get(APIS_URL + "/transactions/", {
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
    async checkAML(id,amount){
      console.log(id)
      this.current_line=id
       await check_rule2(id,amount)
       let nbr_tr=this.transactions_list.length
       console.log(nbr_tr)
       await check_rule7(id,nbr_tr)
       this.result=await get_aml_status(id)
       console.log('resultat',this.result)
 

    }
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
