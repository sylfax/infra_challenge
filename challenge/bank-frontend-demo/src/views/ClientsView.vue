<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        <clients-data-table :data="this.users" />
      </div>
      <div
        class="col-md-4 card shadow-sm p-3 mb-5 bg-body-tertiary rounded"
        style="background: white !important"
      >
        <h5 style="padding: 10px 0px 10px 0px">Add client</h5>
        <form>
          <div class="row">
            <div class="col">
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label"
                  >First name</label
                >
                <input
                  name="email"
                  type="text"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                />
              </div>
            </div>
            <div class="col">
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label"
                  >Last name</label
                >
                <input
                  name="email"
                  type="text"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                />
              </div>
            </div>
          </div>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label"
              >Email address</label
            >
            <input
              name="email"
              type="email"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
            />
            <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
          </div>
          <div class="row">
            <div class="col">
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label"
                  >Address</label
                >
                <input
                  name="email"
                  type="text"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                />
              </div>
            </div>
            <div class="col">
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label"
                  >Country</label
                >
                <input
                  name="email"
                  type="text"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                />
              </div>
            </div>
          </div>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label"
              >Phone number</label
            >
            <input
              name="email"
              type="email"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
            />
            <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
          </div>
          <!-- <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1">
            </div> -->

          <div class="mb-3 form-check">
            <input
              type="checkbox"
              class="form-check-input"
              id="exampleCheck1"
            />
            <label class="form-check-label" for="exampleCheck1">Check</label>
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%">
            Add new client
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import ClientsDataTable from "../components/ClientsDataTable.vue";
export default {
  name: "HeaderComponent",
  components: {
    "clients-data-table": ClientsDataTable,
  },
  data() {
    return {
      users: [
        { id: 1, name: "John Doe", email: "john@example.com" },
        { id: 2, name: "Jane Doe", email: "jane@example.com" },
        { id: 3, name: "John Doe", email: "john@example.com" },
        { id: 4, name: "Jane Doe", email: "jane@example.com" },
        { id: 5, name: "John Doe", email: "john@example.com" },
        { id: 6, name: "Jane Doe", email: "jane@example.com" },
        { id: 7, name: "John Doe", email: "john@example.com" },
        { id: 8, name: "Jane Doe", email: "jane@example.com" },
        // Add more users as needed
      ],
      currentTab: 0,
      email: "",
    };
  },
};
</script>
