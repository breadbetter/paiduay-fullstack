<template>
  <div>
      <form @submit.prevent="updateUser">
    <div>
      <div>ชื่อ</div>
      <input v-model="users.first_name" type="text" />
    </div>
    <div>
      <div>นามสกุล</div>
      <input v-model="users.last_name" type="text" />
    </div>
    <div>
      <div>อีเมล์</div>
      <input v-model="users.email" type="text" />
    </div>
    <div>
      <div>เพศ</div>
      <input v-model="users.gender" type="text" />
    </div>
    <div>
      <div>อายุ</div>
      <input v-model="users.age" type="number" />
    </div>
    <button type="submit" class="accept button">บันทึก</button>
    <nuxt-link tag="button" :to="'/users'">ยกเลิก</nuxt-link>
    <!-- <button type="submit" class="accept button">ลบ</button> -->
      </form>
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
      console.log('response files : ', this.users)
      axios.put(`http://localhost:8000/api/v1/user/${this.users.id}/`,this.users)
        .then(response => {
          console.log('response files : ', response)
          
          alert("แก้ไขข้อมูลเรียบร้อยแล้ว");
          this.$router.push("/users");
        })
        .catch(err => {
          console.log("err", err);
          alert("แก้ไขข้อมูลล้มเหลว");
        });
    }
  },
  mounted() {
    const checkType = this.$route.params.id.split('=')
    const type = checkType[0]
    const value = checkType[1]
    axios.get(
      `http://localhost:8000/api/v1/user/${this.$route.params.id}`
    ).then(res => {
        this.users = res.data
        console.log("user", res.data)
    }) 
  },
//   async asyncData({ params }) {
//     const checkType = params.id.split('=')
//     const type = checkType[0]
//     const value = checkType[1]
//     const { data } = await axios.get(
//       `http://localhost:8000/api/v1/${type}/${value}`
//     );
//     // console.log("data ", this.users);
//     // this.users = data
//     return { user: data };
//   }
};
</script>