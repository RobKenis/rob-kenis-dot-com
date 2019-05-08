<template>
  <v-container
    fluid
    grid-list-md
  >
    <v-layout
      row
      align-start
    >
      <v-flex
        xs8
        sm6
        md6
      >
        <featured-content title="Personal" />
      </v-flex>
      <v-flex
        xs8
        sm6
        md6
      >
        <featured-content
          title="Featured"
          link="/posts/jenkins-pipelines/"
          content="Something about Jenkins"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import FeaturedContent from "~/components/FeaturedContent.vue";

export default {
  components: {
    FeaturedContent
  }
};
</script>