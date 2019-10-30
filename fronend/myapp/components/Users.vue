<template>
  <div class="event-wrapper">
    <div class="table-body">
      <div class="body">
        <nuxt-link class="col" :to="'/users/' + id">
          <div class="col">{{id}}</div>
          <div class="col">{{first_name}}</div>
          <div class="col">{{last_name}}</div>
          <div class="col">{{email}}</div>
          <div class="col">{{gender}}</div>
          <div class="col">{{age}}</div>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["id", "index", "first_name", "last_name", "email", "gender", "age"]
};
</script>

<style lang="scss" scoped>
@import "@/styles/_mixins.scss";
.event-wrapper {
  .table-body {
    display: flex;
    width: 100%;
    padding: 0 24px 0 24px;
    flex-direction: column;
    background-color: $white;
    box-shadow: $box-shadow;
    margin-top: 18px;
    box-shadow: red;
    &:hover {
      border-color: $accent;
    }
    &:hover {
      box-shadow: $hover-shadow;
    }
    a {
      display: flex;
      width: 100%;
      padding: 8px 0;
      color: $text-color;
      border: 1px solid transparent;
      text-decoration:none;
      border-radius: 5px;
      &:hover {
        border-color: $accent;
      }
    }
  }
  .body {
    display: flex;
    flex: 1;

    .col {
      display: flex;
      flex: 1;
      align-items: center;
      justify-content: center;
      &:hover {
      }
    }
    .sub-body {
      display: flex;
      flex: 1;
      padding: 10px 40px;
      margin-top: 8px;
      .col:first-child,
      .col:last-child {
        flex: 0.3;
        // color: $accent;
      }
      .col {
        display: flex;
        flex: 1;
        align-items: center;
        // justify-content: center;
      }
    }
    .table-body-sub {
      display: flex;
      flex-direction: row;
      background-color: $white;
      box-shadow: $box-shadow;
      padding: 10px 32px;
      margin-top: 8px;
    }
    .line {
      margin-top: 8px;
      border: 0;
      border-top: 1px solid #ccc;
    }
  }
}
</style>