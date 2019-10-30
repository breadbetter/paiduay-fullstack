<template>
  <div>
      <form @submit.prevent="updateUser">
    <div>
      <div>ชื่อ</div>
      <input v-model="user.first_name" type="text" />
    </div>
    <div>
      <div>นามสกุล</div>
      <input v-model="user.last_name" type="text" />
    </div>
    <div>
      <div>อีเมล์</div>
      <input v-model="user.email" type="text" />
    </div>
    <div>
      <div>เพศ</div>
      <input v-model="user.gender" type="text" />
    </div>
    <div>
      <div>อายุ</div>
      <input v-model="user.age" type="number" />
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
      users: this.post
        ? { ...this.post }
        : {
            first_name: "",
            last_name: "",
            email: "",
            gender: "",
            age: ""
          }
    };
  },
  methods: {
    updateUser({ params }) {
      axios.put(`http://localhost:8000/api/v1/${params.id}`,this.$route.params.id, this.post)
        .then(response => {
          console.log('response files : ', response)
          alert("แก้ไขข้อมูลเรียบร้อยแล้ว");
        //   this.$router.push("/product");
        })
        .catch(err => {
          console.log("err", err);
          alert("แก้ไขข้อมูลล้มเหลว");
        });
    }
  },
  async asyncData({ params }) {
    const { data } = await axios.get(
      `http://localhost:8000/api/v1/${params.id}`
    );
    console.log("data ", data);
    return { user: data };
  }
};
</script>