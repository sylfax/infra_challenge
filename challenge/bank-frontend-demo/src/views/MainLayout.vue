<template>
    <div :class="{ 'body-pd': isBodyPd }">
      <header class="header" :class="{ 'body-pd': isHeaderPd }" id="header">
        <div class="header_toggle" @click="toggleSidebar">
          <i :class="isSidebarOpen?'bi bi-x':'bi bi-list'"></i>
        </div>
        <div class="header_img">
            <i class="bi bi-person-circle" style="font-size: 1.5em;"></i>
        </div>
      </header>
      <div class="l-navbar" :class="{ show: isSidebarOpen }" id="nav-bar">
        <nav class="nav">
          <div>
            <a href="#" class="nav_logo text-center" >
              <i class="bi bi-bank"></i><br>
              <span class="nav_logo-name" style="text-decoration: none;">Bank LIST</span>
            </a>
            <div class="nav_list">
              <a class="nav_link" :class="{ active: activeLink === 'dashboard' }" @click="setActiveLink('dashboard'); setCurrentTab(0)">
                <i class="bi bi-speedometer2"></i>
                <span class="nav_name">Dashboard</span>
              </a>
              <a href="#" class="nav_link" :class="{ active: activeLink === 'users' }" @click="setActiveLink('users'); setCurrentTab(1)">
                <i class="bi bi-people"></i>
                <span class="nav_name">Users</span>
              </a>
              <a href="#" class="nav_link" :class="{ active: activeLink === 'transactions' }" @click="setActiveLink('transactions'); setCurrentTab(2)">
                <i class="bi bi-cash"></i>
                <span class="nav_name">Transactions</span>
              </a>
            </div>
          </div>
          <a href="#" class="nav_link" @click="signOut">
            <i class="bi bi-box-arrow-left"></i>
            <span class="nav_name">SignOut</span>
          </a>
        </nav>
      </div>
      <div class="container fluid bg-light" style="padding-top:100px ;">
        <dashboard-view v-if="currentTab===0"/>
        <clients-view v-if="currentTab===1"/>
    </div>
    </div>
  
  </template>
  
  <script>
  import ClientsView from './ClientsView.vue';
  import DashboardView from './DashboardView.vue';
  export default {
    components:{
        "clients-view":ClientsView,
        "dashboard-view":DashboardView
    },
    data() {
      return {
        isSidebarOpen: false,
        isBodyPd: false,
        isHeaderPd: false,
        activeLink: 'dashboard',
        currentTab:0
      };
    },
    methods: {
      toggleSidebar() {
        this.isSidebarOpen = !this.isSidebarOpen;
        this.isBodyPd = !this.isBodyPd;
        this.isHeaderPd = !this.isHeaderPd;
      },
      signOut() {
        // Add your sign out logic here
      },
      setActiveLink(link) {
        this.activeLink = link;
      },
      setCurrentTab(tabIndex) {
      this.currentTab = tabIndex;
    },
    },
  };
  </script>
  

<style>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap");
:root {
  --header-height: 3rem;
  --nav-width: 68px;
  --first-color: #000330;
  --first-color-light: #afa5d9;
  --white-color: #f7f6fb;
  --body-font: "Nunito", sans-serif;
  --normal-font-size: 1rem;
  --z-fixed: 100;
}
*,
::before,
::after {
  box-sizing: border-box;
}
body {
  position: relative;
  margin: var(--header-height) 0 0 0;
  padding: 0 1rem;
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
  transition: 0.5s;
}
.header {
  width: 100%;
  height: var(--header-height);
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1rem;
  background-color: var(--white-color);
  z-index: var(--z-fixed);
  transition: 0.5s;
  background-color: white; box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1)
}
.header_toggle {
  color: var(--first-color);
  font-size: 1.5rem;
  cursor: pointer;
}
.header_img {
  width: 35px;
  height: 35px;
  display: flex;
  justify-content: center;
  border-radius: 50%;
  overflow: hidden;
}
.header_img img {
  width: 40px;
}
.l-navbar {
  position: fixed;
  top: 0;
  left: -30%;
  width: var(--nav-width);
  height: 100vh;
  background-color: var(--first-color);
  padding: 0.5rem 1rem 0 0;
  transition: 0.5s;
  z-index: var(--z-fixed);
}
.nav {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
}
.nav_logo,
.nav_link {
  text-decoration: none ;
  color:white;
  display: grid;
  grid-template-columns: max-content max-content;
  align-items: center;
  column-gap: 1rem;
  padding: 0.5rem 0 0.5rem 1.5rem;
}
.nav_logo {
  text-decoration: none ;
  margin-bottom: 2rem;
  margin-left: 32px;
}
.nav_logo-icon {
  font-size: 1.25rem;
  color: var(--white-color);
}
.nav_logo-name {
  color: var(--white-color);
  font-weight: 700;
}
.nav_link {
  position: relative;
  color: var(--first-color-light);
  margin-bottom: 1.5rem;
  transition: 0.3s;
}
.nav_link:hover {
  color: var(--white-color);
}
.nav_icon {
  font-size: 1.25rem;
}
.show {
  left: 0;
}
.body-pd {
  padding-left: calc(var(--nav-width) + 1rem);
}
.active {
  color: var(--white-color);
}
.active::before {
  content: "";
  position: absolute;
  left: 0;
  width: 2px;
  height: 32px;
  background-color: var(--white-color);
}
.height-100 {
  height: 100vh;
}
@media screen and (min-width: 768px) {
  body {
    margin: calc(var(--header-height) + 1rem) 0 0 0;
    padding-left: calc(var(--nav-width) + 2rem);
  }
  .header {
    height: calc(var(--header-height) + 1rem);
    padding: 0 2rem 0 calc(var(--nav-width) + 2rem);
  }
  .header_img {
    width: 40px;
    height: 40px;
  }
  .header_img img {
    width: 45px;
  }
  .l-navbar {
    left: 0;
    padding: 1rem 1rem 0 0;
  }
  .show {
    width: calc(var(--nav-width) + 156px);
  }
  .body-pd {
    padding-left: calc(var(--nav-width) + 188px);
  }
}
</style>
