<script>
import axios from "axios";
import { APIS_URL } from "@/apis";

export default {
  name: "TransactionForm",
  data() {
    return {
      transactionData: {
        recipient: "",
        amount: "",
        description:""
      },
    };
  },
  methods: {
    updateTransactionData() {
      this.$emit("updateTransactionData", this.transactionData);
    },
    createTransaction() {
      console.log("data: " + JSON.stringify(this.transactionData));
      axios
        .post(APIS_URL + "/login", this.transactionData, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log("login res", response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<template>
  <div class="modal modal-dialog-centered" id="transacModal">
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
            style="padding-top: 100px !important"
          >
            <div class="card" style="width: 32rem">
              <div class="card-body">
                <div class="card-text">
                <div class="mb-3">
                  <select
                    class="form-select"
                    aria-label="Default select example"
                    v-model="transactionData.recipient"
                    placeholder="Select recipient"
                    @input="updateTransactionData"
                    >
                    <option selected>Select recipient</option>
                    <option value="1">John</option>
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
</template>

<style scoped></style>
