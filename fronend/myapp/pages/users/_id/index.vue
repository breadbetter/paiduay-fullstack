<template>
  <div id="container">
    <div class="nav">
    </div>
    <div class="add-form">
      <form @submit.prevent="updateUser">
        ในส่วนอัพเดทข้อมูล และลบข้อมูลใช้ http://localhost:8000/api/v1/user/id/
        <div class="lebel">
          <div class="sub-lebel">ชื่อ</div>
          <div class="sub-lebel">
            <input v-model="users.first_name" type="text" />
          </div>
        </div>
        <div class="lebel">
          <div class="sub-lebel">นามสกุล</div>
          <div class="sub-lebel">
            <input v-model="users.last_name" type="text" />
          </div>
        </div>
        <div class="lebel">
          <div class="sub-lebel">อีเมล์</div>
          <div class="sub-lebel">
            <input v-model="users.email" type="text" />
          </div>
        </div>
        <div class="lebel">
          <div class="sub-lebel">เพศ</div>
          <div class="sub-lebel">
            <select v-model="users.gender" name="gender" id="gender">
              <option v-for="(gender, i) in OptionGender" :key="i" :value="gender">{{gender}}</option>
            </select>
          </div>
        </div>
        <div class="lebel">
          <div class="sub-lebel">อายุ</div>
          <div class="sub-lebel">
            <input v-model="users.age" type="text" />
          </div>
        </div>
        <div class="button-group">
          <button type="submit" class="accept button">บันทึก</button>
          <nuxt-link tag="button" class="cancel button" :to="'/users'">ยกเลิก</nuxt-link>
          <button @click.prevent="deleteUser" class="delete button">ลบ</button>
        </div>
      </form>
      
    </div>
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";
import APIList from "~/api/main.js";
import axios from "axios";
export default {
  props: {
    post: {
      type: Object,
      required: false
    }
  },
  data() {
    return {
      OptionGender: ['female','male'],
      users: {
          first_name: "",
          last_name: "",
          email: "",
          gender: "",
          age: "",
      }
    }
  },
  methods: {
    updateUser() {
      axios.put(`http://localhost:8000/api/v1/user/${this.users.id}/`,this.users)
        .then(response => {
          alert("แก้ไขข้อมูลเรียบร้อยแล้ว");
          // this.$router.push("/users");
        })
        .catch(err => {
          console.log("err", err);
          alert("แก้ไขข้อมูลล้มเหลว");
        });
    },
    deleteUser() {
      axios.delete(`http://localhost:8000/api/v1/user/${this.users.id}/`,this.users)
        .then(response => { 
          alert("ลบข้อมูลเรียบร้อยแล้ว");
          this.$router.push("/users");
        })
    }
  },
  mounted() {
    axios.get(
      `http://localhost:8000/api/v1/user/${this.$route.params.id}`
    ).then(res => {
        this.users = res.data
    }) 
  },
};
</script>

<style lang="scss" scoped>
@import "@/styles/_mixins.scss";
#container {
  display: flex;
  flex-direction: column;
}
.add-form {
  display: flex;
  //width: 50%;
  justify-content: center;
  margin: 16px;
  background-color: $img-bg;
  border-radius: 16px;
  .lebel {
    display: flex;
    flex: 1;
    margin: 16px;
    .sub-lebel {
      width: 100%;
    }
    input {
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
    select{
      // appearance: none;
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
  }
}
.content {
  padding: 8px 16px;
  flex-flow: column wrap;
}
.button-group {
  padding: 8px;
  display: flex;
  justify-content: center;
  button {
      padding: 8px 32px;
      margin: 8px;
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
    &.cancel {
      background-color: shade($primary, 5%);
      &:hover {
        background-color: shade($primary, 50%);
      }
    }
    &.delete {
      background-color: rgb(255, 68, 68);
      &:hover {
        background-color: shade(rgb(255, 68, 68), 50%);
      }
    }
    }
}
</style>