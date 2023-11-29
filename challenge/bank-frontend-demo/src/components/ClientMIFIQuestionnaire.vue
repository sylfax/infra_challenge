<script>
export default {
  name: "ClientMIFIQuestionnaire",
  data() {
    return {
      MIFIDData: {
        riskLevel: 'low',
        actionKnowledge: 'no'
      }
    }
  },
  methods: {
    updateMIFIDData(data) {
      this.$emit('updateMIFIDData', this.MIFIDData)
    }
  }
}
</script>

<template>
  <div class="container-fluid p-2 d-flex justify-content-center" style="padding-top: 100px !important;">
    <div class="card" style="width: 32rem;">
      <div class="card-body">
        <h5 class="card-title fw-bolder">Markets in Financial Instruments Directive</h5>
        <div class="card-text d-flex flex-column">
          <div class="row">
            <div class="col-6">
              <p>Risk level</p>
            </div>
            <div class="col">
              <div class="input-group">
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" value="low" v-model="MIFIDData.riskLevel" @change="updateMIFIDData">
                  <label class="form-check-label" for="flexRadioDefault1">
                    Low
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" value="middle" v-model="MIFIDData.riskLevel">
                  <label class="form-check-label" for="flexRadioDefault2">
                    Middle
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault3" value="high" v-model="MIFIDData.riskLevel">
                  <label class="form-check-label" for="flexRadioDefault3">
                    High
                  </label>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Do you know what is an action?</p>
            </div>
            <div class="col">
              <div class="input-group">
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="actionKnowledge" id="actionKnowledge1" value="no" v-model="MIFIDData.actionKnowledge" checked>
                  <label class="form-check-label" for="flexRadioDefault1">
                    No
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="actionKnowledge" id="actionKnowledge2"  value="yes" v-model="MIFIDData.actionKnowledge">
                  <label class="form-check-label" for="flexRadioDefault2">
                    Yes
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
