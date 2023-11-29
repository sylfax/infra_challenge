<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import ClientCommonInformation from "@/components/ClientCommonInformation.vue";
import ClientMIFIQuestionnaire from "@/components/ClientMIFIQuestionnaire.vue";
import axios from "axios";
import { APIS_URL } from "@/apis";

export default {
  name: "ClientOnboarding",
  components: {
    ClientMIFIQuestionnaire,
    ClientCommonInformation,
    HeaderComponent,
  },
  data() {
    return {
      clientData: {
        firstNameClient: "",
        lastNameClient: "",
        birthDateClient: "",
        nationalityClient: "",
        addressClient: "",
        cityClient: "",
        countryClient: "",
        emailClient: "",
      },
      MIFIDData: {
        riskLevel: "low",
        actionKnowledge: "no",
      },
      show_success:false
    };
  },
  methods: {
    updateClientData(data) {
      this.clientData = data;
      console.log(JSON.stringify(this.clientData));
    },
    updateMIFIDData(data) {
      this.MIFIDData = data;
    },
    saveClientData() {
      console.log("data: " + JSON.stringify(this.clientData));
      axios
        .post(APIS_URL + "/onboarding", this.clientData, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.show_success=true
          console.log("res onboarding", response.data);
        })
        .catch((error) => {
          this.show_success=false
          console.error(error);
        });
    },
  },
};
</script>

<template>
  <div class="bg-light">
    <HeaderComponent from="onboarding" />
    <div class="alert alert-success" role="alert" style="padding-top: 100px;" v-if="show_success">
      register success !
    </div>
    <div class="row">
      <div class="col-md-6">
        <ClientCommonInformation v-on:updateClientData="updateClientData" />
      </div>
      <div class="col-md-4">
        <ClientMIFIQuestionnaire v-on:updateMIFIDData="updateMIFIDData" />
        <button
          class="btn btn-primary"
          style="margin: 10px 0px 0px 10px"
          @click.prevent="saveClientData"
        >
          Save your information
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
