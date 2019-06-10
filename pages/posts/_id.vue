<template>
  <v-container>
    <v-breadcrumbs :items="items">
      <template v-slot:divider>
        <v-icon>forward</v-icon>
      </template>
    </v-breadcrumbs>

    <h1>{{ post.id }}</h1>
    <small>The api is a work in progress. These posts will be available soon</small>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  data: () => {
    return {
      post: {
        id: ""
      }
    };
  },
  computed: {
    items: function() {
      const postId = this.post.id
      return [
        {
          text: "Home",
          disabled: false,
          href: "/"
        },
        {
          text: "Posts",
          disabled: false,
          href: "/posts"
        },
        {
          text: postId,
          disabled: true,
          href: `/posts/${postId}`
        }
      ];
    }
  },
  created() {
    this.post.id = this.$route.params.id;
    //TODO: fetch data from api and set data.post
  }
});
</script>

