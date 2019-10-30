<template>
  <div id="container">
    <div class="nav">
      <div><h1>ผู้ใช้ทั้งหมด</h1> (หน้านี้เรียกข้อมูลจาก http://localhost:8000/api/v1/)</div>
      <div>
        <nuxt-link tag="button" :to="'/users/add_user'">เพิ่มผู้ใช้งาน</nuxt-link>
        
        <input
          type="search"
          class="searchInput"
          placeholder="ค้นหา ไอดี, ชื่อ, นามสกุล, อีเมล์, เพศ, อายุ"
          v-model="search"
        />
        <p>(ค้นหาข้อมูลจาก http://localhost:8000/api/v1/?search= )</p>
      </div>
      
    </div>
    <div class="table-header">
      <div class="cell index">#</div>
      <div class="cell name">ชื่อ</div>
      <div class="cell name">นามสกุล</div>
      <div class="cell email">อีเมล</div>
      <div class="cell gender">เพศ</div>
      <div class="cell age">อายุ</div>
    </div>
    <Users
      v-for="(user,index) in users"
      :index="index+1"
      :key="user.id"
      :id="user.id"
      :first_name="user.first_name"
      :last_name="user.last_name"
      :email="user.email"
      :age="user.age"
      :gender="user.gender"
    />
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";
import APIList from "~/api/main.js";
import axios from "axios";
import Users from "@/components/Users";
export default {
  components: {
    Logo,
    Users
  },
  data() {
    // console.log("search ", search)
    return {
      users: null,
      search: ""
    };
  },
  watch: {
    search(value) {
      axios
        .get(`http://localhost:8000/api/v1/`, {
          params: {
            search: value
          }
        })
        .then(res => {
          this.users = res.data;
          console.log("users : ", this.users);
        });
    }
  },
  mounted() {
    axios.get(`http://localhost:8000/api/v1/`).then(res => {
      this.users = res.data;
      console.log("users : ", this.users);
    });
  }
};
</script>


<style lang="scss" scoped>
@import "@/styles/_mixins.scss";
#container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  justify-content: center;
  margin: 30px;
  .searchInput {
    appearance: none;
    width: 320px;
    outline: none;
    border: 1px solid $border;
    padding: 8px 8px;
    border-radius: 5px;
    &:hover,
    &:focus {
      border-color: $accent;
    }
  }
  .nav {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 16px 24px 8px;
    .nav-title {
      display: flex;
    }
    .heading {
      margin-right: 48px;
    }
    .input-group {
      display: flex;
    }
    button {
      padding: 4px 32px;
      height: 34px;
      background-color: $accent;
      outline: none;
      border: 0;
      border-radius: 8px;
      cursor: pointer;
      transition: 0.2s ease-out;
      &:hover {
        background-color: shade(rgba(255, 173, 51, 0.726), 5%);
      }

      &:hover {
        background-color: shade(rgba(255, 173, 51, 0.726), 30%);
      }
    }
  }
}
.table-header {
  display: flex;
  text-align: center;
  color: $accent;
  padding: 8px 24px;
  margin: 0;
  .cell {
    flex: 1;
    font-weight: normal;
  }
}
</style>